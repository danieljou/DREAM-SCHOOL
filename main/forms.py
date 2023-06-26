from django import forms
from .models import *


from django.forms import (
    CheckboxInput,TextInput,ModelForm,EmailInput, 
    NumberInput, DateInput, 
    BooleanField, Select, FileInput,
    Textarea,
    
)


class SessionForm(forms.ModelForm):
    
    class Meta:
        model = Session
        fields = "__all__"


class SalleDeClasseForm(forms.ModelForm):
    
    class Meta:
        model = SalleDeClasse
        fields = "__all__"


class ClasseSessionForm(forms.ModelForm):
    
    class Meta:
        model = ClasseSession
        fields = "__all__"

class MatiereForm(forms.ModelForm):
    
    class Meta:
        model = Matiere
        fields = "__all__"

class MatiereCoefForm(forms.ModelForm):
    
    class Meta:
        model = MatiereCoef
        fields = "__all__"


class NiveauForm(forms.ModelForm):
    
    class Meta:
        model = Niveau
        exclude = ('slug',)



class EtudiantForm(forms.ModelForm):
    
    class Meta:
        model = Etudiant
        fields = "__all__"

        widgets = {
            'Sexe' : Select(
                attrs = {
                    'class': 'form-select'
                }
            ),
            'classe' : Select(
                attrs = {
                    'class': 'form-select'
                }
            ),
            'Date_naiss' : TextInput(
                attrs = {
                   
                    'type':"date"
                }
            ),
        }