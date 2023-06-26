from django.shortcuts import render, redirect

from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.template.loader import render_to_string
from django.contrib import messages

# Create your views here.

from .forms import *
from .models import *

def index(request):


    return render(request,'index.html')


# Gestion des sessions (année scolaire)
def session(request):
    context = {}
    try:
        session_active = Session.objects.filter(is_active = True)[0]
    except:
        session_active = 'Aucune session n\'est active pour le momment' 
    context['sessions'] = Session.objects.all()
    context['session_active'] = session_active


    return render(request, 'gestion/session/session.html', context)

def createSession(request):
    form = SessionForm(request.POST or None)
    context = {}
    context['form'] = form
    if request.method == "POST":
        if form.is_valid():
            session = form.save()
            if session.is_active:
                try:
                    session_active = Session.objects.filter(is_active = True)[0]
                    session_active.is_active = False
                    session_active.save()

                except:
                    pass
            return redirect('session')

    return render(request, 'gestion/session/form.html' , context)

def updatesession(request, id):
    session = get_object_or_404(Session, pk = id)
    context = {}
    form = SessionForm(request.POST or None, instance = session)
    context['form'] = form

    if request.method == "POST":
        if form.is_valid():
            session = form.save()
            if session.is_active:
                try:
                    session_active = Session.objects.filter(is_active = True)
                    for item in session_active:
                        item.is_active = False
                        item.save()
                    session.save()
                    return redirect('session')
                        

                except:
                    return redirect('session')
                finally:
                    pass
            
        else:
            messages.error(request,'Une erreur est survenue')

            return redirect('session')
    return render(request, 'gestion/session/form.html' , context)


def deletesession(request, id):
    session = get_object_or_404(Session, pk = id)
    context =   {}
    context['session'] = session
    if request.method == "POST":
        messages.success(request, 'la session à été supprimée avec succèss')
        session.delete()
        return redirect('session')

    return render(request, 'gestion/session/delete.html', context)







# Gestion des niveau (année scolaire)
def niveaux(request):
    context = {}
    context['niveaux'] = Niveau.objects.all()
    return render(request, 'gestion/niveaux/niveau.html', context)

def createniveau(request):
    form = NiveauForm(request.POST or None)
    context = {}
    context['form'] = form
    if request.method == "POST":
        if form.is_valid():
            session = form.save()
            return redirect('niveau')

    return render(request, 'gestion/niveaux/form.html' , context)

def updateniveau(request, id):
    niveau = get_object_or_404(Niveau, pk = id)
    context = {}
    form = NiveauForm(request.POST or None, instance = niveau)
    context['form'] = form

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('niveau')
    return render(request, 'gestion/niveaux/form.html' , context)


def deleteniveau(request, id):
    session = get_object_or_404(Session, pk = id)
    context =   {}
    context['session'] = session
    if request.method == "POST":
        messages.success(request, 'la session à été supprimée avec succèss')
        session.delete()
        return redirect('session')

    return render(request, 'gestion/session/delete.html', context)



# Gestion des salles de classes 
def salles(request):
    context = {}
    context['salles'] = SalleDeClasse.objects.all()
    return render(request, 'gestion/salles/salles.html', context)

def createsalle(request):
    form = SalleDeClasseForm(request.POST or None)
    context = {}
    context['form'] = form
    if request.method == "POST":
        if form.is_valid():
            session = form.save()
            return redirect('salles')

    return render(request, 'gestion/salles/form.html' , context)

def updatesalle(request, id):
    classe = get_object_or_404(SalleDeClasse, pk = id)
    context = {}
    form = SalleDeClasseForm(request.POST or None, instance = classe)
    context['form'] = form

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('salles')
    return render(request, 'gestion/salles/form.html' , context)


def deletesalle(request, id):
    salle = get_object_or_404(  SalleDeClasse  , pk = id)
    context =   {}
    context['salle'] = salle
    if request.method == "POST":
        messages.success(request, 'la salle de classe à été supprimée avec succèss')
        salle.delete()
        return redirect('salles')

    return render(request, 'gestion/salles/delete.html', context)







# Gestion des salles de classes  et des session
def salles_session(request):
    context = {}
    context['salles'] = ClasseSession.objects.all()
    try:
        session_active = Session.objects.filter(is_active = True)[0]
    except:
        session_active = 'Aucune session n\'est active pour le momment'
    context['session_active'] = session_active 
    return render(request, 'gestion/salles_session/salles.html', context)

def createsalle_session(request):
    form = ClasseSessionForm(request.POST or None)
    context = {}
    context['form'] = form
    if request.method == "POST":
        if form.is_valid():
            session = form.save()
            return redirect('salles_session')

    return render(request, 'gestion/salles_session/form.html' , context)

def updatesalle_session(request, id):
    classe = get_object_or_404(ClasseSession, pk = id)
    context = {}
    form = SalleDeClasseForm(request.POST or None, instance = classe)
    context['form'] = form

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('salles_session')
    return render(request, 'gestion/salles_session/form.html' , context)


def deletesalle_session(request, id):
    salle = get_object_or_404(  ClasseSession  , pk = id)
    context =   {}
    context['salle'] = salle
    if request.method == "POST":
        messages.success(request, 'la salle de classe à été supprimée avec succèss')
        salle.delete()
        return redirect('salles_session')

    return render(request, 'gestion/salles_session/delete.html', context)


def detailssalle_session(request, id):
    salle = get_object_or_404(  ClasseSession  , pk = id)
    context =   {}
    context['salle'] = salle

    
    return render(request, 'gestion/salles_session/details.html', context)






# Gestion des salles de classes 
def matieres(request):
    context = {}
    context['matieres'] = Matiere.objects.all()
    return render(request, 'gestion/matieres/matiere.html', context)

def creatematiere(request):
    form = MatiereForm(request.POST or None)
    context = {}
    context['form'] = form
    if request.method == "POST":
        if form.is_valid():
            session = form.save()
            return redirect('matieres')

    return render(request, 'gestion/matieres/form.html' , context)

def updatematiere(request, id):
    classe = get_object_or_404(Matiere, pk = id)
    context = {}
    form = MatiereForm(request.POST or None, instance = classe)
    context['form'] = form

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('matieres')
    return render(request, 'gestion/matieres/form.html' , context)


def deletematiere(request, id):
    matiere = get_object_or_404(Matiere  , pk = id)
    context =   {}
    context['matiere'] = matiere
    if request.method == "POST":
        messages.success(request, 'la matiere de classe à été supprimée avec succèss')
        matiere.delete()
        return redirect('matieres')

    return render(request, 'gestion/matieres/delete.html', context)














# Gestion matieres et coefs
def matieres_coefs(request):
    context = {}
    context['matiere_coefs'] = MatiereCoef.objects.all()
    return render(request, 'gestion/matiere_coef/matieres_coef.html', context)

def creatematiere_coef(request):
    form = MatiereCoefForm(request.POST or None)
    context = {}
    context['form'] = form
    if request.method == "POST":
        if form.is_valid():
            session = form.save()
            return redirect('matieres_coef')

    return render(request, 'gestion/matiere_coef/form.html' , context)

def updatematiere_coef(request, id):
    classe = get_object_or_404(MatiereCoef, pk = id)
    context = {}
    form = MatiereCoefForm(request.POST or None, instance = classe)
    context['form'] = form

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('matieres_coef')
    return render(request, 'gestion/matiere_coef/form.html' , context)


def deletematiere_coef(request, id):
    matiere_coef = get_object_or_404(MatiereCoef  , pk = id)
    context =   {}
    context['matiere_coef'] = matiere_coef
    if request.method == "POST":
        messages.success(request, 'la matiere_coef de classe à été supprimée avec succèss')
        matiere_coef.delete()
        return redirect('matieres_coef')

    return render(request, 'gestion/matiere_coef/delete.html', context)




# GESTION DES ELEVES

def eleves(request):
    context = {}
    context['eleves'] = Etudiant.objects.all()


    return render(request, "gestion_eleves/index.html", context)


def AddEleve(request):
    context = {}
    form = EtudiantForm(request.POST or None, request.FILES or None)
    context['form'] = form
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'Elève enregistré avec succès')
            return redirect('eleves')
        else:
            messages.warning(request, 'Verifiez tous les champs')



    return render(request, "gestion_eleves/form.html", context)

def eleveDetails(request, matricule):
    context = {}
    etudiant = get_object_or_404(Etudiant, Matricule = matricule)
    context['etudiant'] = etudiant



    return render(request, "gestion_eleves/details.html", context)

def eleveUpdate(request, matricule):
    context = {}
    etudiant = get_object_or_404(Etudiant, Matricule = matricule)
    context['etudiant'] = etudiant
    form = EtudiantForm(request.POST or None, request.FILES or None, instance  =etudiant)
    context['form'] = form
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'Elève modifié avec succès')
            return redirect('eleves')
        else:
            messages.warning(request, 'Verifiez tous les champs')
    return render(request, "gestion_eleves/form.html", context)



    return render(request, "gestion_eleves/details.html", context)









def profile(request):
    context = {}

    return render(request, 'registration/profile.html', context)