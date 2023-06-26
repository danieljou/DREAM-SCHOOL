from django import forms
from .models import *

from django.forms import (
    CheckboxInput,TextInput,ModelForm,EmailInput, 
    NumberInput, DateInput, 
    BooleanField, Select, FileInput,
    Textarea,
    
)


class EcheancePaiementForm(forms.ModelForm):
    
    class Meta:
        model = EcheancePaiement
        exclude = ('session', )
        widgets = {
             'date_debut' : TextInput(
                attrs = {
                   
                    'type':"date"
                }
            ),
            'date_fin' : TextInput(
                attrs = {
                   
                    'type':"date"
                }
            ),
        }


class PaymentForm(forms.ModelForm):

    class Meta:
        model = Payment
        exclude = ('date_paiement',)

class MoratoireForm(forms.ModelForm):

    class Meta:
        model = Moratoire
        session_active = None
        try:
            session_active = Session.objects.filter(is_active = True)[0]
        except:
            session_active = None
        Student = []
        if session_active:
            Student = Etudiant.objects.filter(classe__session = session_active)
       
        widgets = {
            'eleve' : Select(
                choices = Student,
                attrs = {
                    'class': 'form-select'
                }
            ),
        }
        exclude = ('session',)
