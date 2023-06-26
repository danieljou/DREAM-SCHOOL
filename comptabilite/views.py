from django.shortcuts import render, redirect
from .models import *
from main.models import Session, Etudiant
from .forms import *
from django.contrib import messages
from django.shortcuts import get_object_or_404


# Create your views here.



# Comptabilité

def compta_index(request):
    context = {}

    return render(request, 'configurations/dashbord.html', context)

def compta_config(request):
    context = {}
    try:
        session_active = Session.objects.filter(is_active = True)[0]
    except:
        session_active = None

    if session_active:
        echeances = EcheancePaiement.objects.filter(session = session_active)
        context['echeances'] = echeances
        context['session_active'] = session_active
        levels = []
        for level in echeances:
            if not level.niveau.nom in levels:
                levels.append(level.niveau.nom)
        
        levels.sort()
        payment = []
        for level in levels:
            paid = []
            for item in echeances:
                if item.niveau.nom == level:
                    paid.append(item)
            payment.append({'niveau': level, 'paiement':paid})

        context['payment'] = payment

    return render(request, 'configurations/configuration.html', context)

def compta_add_echeance(request):
    context = {}
    form = EcheancePaiementForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            payement = form.save(commit = False)
            try:
                session_active = Session.objects.filter(is_active = True)[0]
            except:
                session_active = None
            if session_active:
                payement.session = session_active
                payement.save()
                messages.success(request, 'échéances enregistrée avec sucess')
                return redirect('compta_config')
            else:
                messages.error(request,'Aucune session \' est active : vous ne pouvez creer une echéances de paiement')

    context['form'] = form
    return render(request, "configurations/add.html", context)


def compta_update_echeance(request, id):
    context = {}
    echeance = get_object_or_404(EcheancePaiement, pk = id)
    form = EcheancePaiementForm(request.POST or None, instance = echeance)
    if request.method == "POST":
        if form.is_valid():
            payement = form.save(commit = False)
            try:
                session_active = Session.objects.filter(is_active = True)[0]
            except:
                session_active = None
            if session_active:
                payement.session = session_active
                payement.save()
                messages.success(request, 'échéances enregistrée avec sucess')
                return redirect('compta_config')
            else:
                messages.error(request,'Aucune session \' est active : vous ne pouvez creer une echéances de paiement')

    context['form'] = form
    return render(request, "configurations/add.html", context)



def compta_delete_echeance(request, id):
    context = {}
    echeance = get_object_or_404(EcheancePaiement, pk = id)
    if request.method == "POST":
        echeance.delete()
        messages.success(request, 'Echéances suprimmée avec sucess')
        return redirect('compta_config')
    
    return render(request, "configurations/delete.html", context)


def compta_payement(request):
    context = {}

    return render(request, 'paiements/index.html', context)

def compta_payement_add_first(request):
    context = {}
    # form = PaymentForm(request.POST or None)
    try:
        session_active = Session.objects.filter(is_active = True)[0]
    except:
        session_active = None
    if session_active:

        eleves = Etudiant.objects.filter(classe__session = session_active )
        context['eleves'] = eleves
        context['session_active'] = session_active

    # context['form'] = form
    return render(request, 'paiements/add.html', context)


def compta_payement_add_second(request, matricule):
    context = {}
    eleve = get_object_or_404(Etudiant, Matricule = matricule)
    context['eleve'] = eleve
    try:
        session_active = Session.objects.filter(is_active = True)[0]
    except:
        session_active = None
    if session_active:
        context['session_active'] = session_active
        echeances = EcheancePaiement.objects.filter(session = session_active , niveau = eleve.classe.classe.niveau)
        context['echeances'] = echeances
        print(echeances)
    # context['form'] = form
    return render(request, 'paiements/add_second.html', context)


def compta_payement_add_third(request, matricule, echeance):
    context = {}
    try:
        session_active = Session.objects.filter(is_active = True)[0]
    except:
        session_active = None
    eleve = get_object_or_404(Etudiant, Matricule = matricule)
    echeancePaiement = get_object_or_404(EcheancePaiement, id = echeance)
    context['eleve'] = eleve
    if session_active:
        context['session_active'] = session_active
    
    if request.method == "POST":
        montant = request.POST['montant']
        try:
            montant = int(montant)
        except:
            messages.error(request, 'une érreur s\'est produite')
            montant = -1
        
        if montant < 0:
            messages.warning(request, 'Le montant entré est négatif')
        else:
            paiement = Payment()
            paiement.eleve = eleve
            paiement.echeance = echeancePaiement
            paiement.montant = montant
            paiement.save()
            messages.success(request, 'Paiement enregistré avec succèss')
            return redirect('compta_paiement_details', matricule)
   
    return render(request, 'paiements/add_third.html', context)



def compta_solvabilite(request):
    context = {}
    try:
        session_active = Session.objects.filter(is_active = True)[0]
    except:
        session_active = None
    if session_active:

        eleves = Etudiant.objects.filter(classe__session = session_active )
        context['eleves'] = eleves
        context['session_active'] = session_active
    return render(request, 'configurations/solvabilite.html', context)

def compta_paiement_details(request, matricule):
    context = {}
    eleve = get_object_or_404(Etudiant, Matricule = matricule)
    context['eleve'] = eleve
    try:
        session_active = Session.objects.filter(is_active = True)[0]
    except:
        session_active = None
    if session_active:
        paiement = Payment.objects.filter(eleve = eleve, eleve__classe__session = session_active)
        context['paiement'] = paiement
        print(paiement)

    return render(request, 'paiements/details.html', context)



# Moratoires

def moratoire_index(request):
    context = {}

    try:
        session_active = Session.objects.filter(is_active = True)[0]
    except:
        session_active = None
    if session_active:
        moratoires = Moratoire.objects.filter(eleve__classe__session = session_active)
    else:
        moratoires = []
    context['moratoires'] = moratoires
    return render(request, 'moratoires/index.html', context)

def moratoire_create(request):
    context= {}
    form = MoratoireForm(request.POST or None)

    context['form'] = form
    return render(request, 'moratoires/create.html', context)