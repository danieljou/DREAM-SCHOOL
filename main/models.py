from django.db import models
from django.utils.text import slugify
from datetime import datetime

# Create your models here.


class Session(models.Model):
    nom = models.CharField("Nom de la session", max_length=50)
    is_active = models.BooleanField('Session active',default = False)
    def __str__(self):
        return self.nom


class Niveau(models.Model):
    nom = models.CharField("Nom du niveau", max_length=50)
    code = models.CharField("Code du niveau", unique = True,  max_length=50)
    slug = models.SlugField(unique = True)

    def __str__(self):
        return self.nom
    
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Niveau'
        verbose_name_plural = 'Niveaux'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.nom)
        super(Niveau, self).save(*args, **kwargs)

class SalleDeClasse(models.Model):
    nom = models.CharField("Nom de la salle de classe", max_length=50)
    code = models.CharField("Code de la salle de classe", max_length=50, unique = True)
    niveau = models.ForeignKey("Niveau", on_delete=models.CASCADE)

    def __str__(self):
        return self.code

class Matiere(models.Model):
    nom = models.CharField("Nom de la matière", max_length=50)
    code = models.CharField("Code de la matière", max_length=50)

    def __str__(self):
        return self.nom

class MatiereCoef(models.Model):
    coef = models.PositiveIntegerField("Coéficient")
    matiere = models.ForeignKey("Matiere", on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.matiere } - COEF - {self.coef}'

class ClasseSession(models.Model):
    

    classe = models.ForeignKey("SalleDeClasse",  on_delete=models.CASCADE)
    session = models.ForeignKey("Session",  on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.classe} - {self.session}'

    def get_total_eleves(self):

        return Etudiant.objects.filter(classe = self).count()
    def get_eleves(self):
        return Etudiant.objects.filter(classe = self)



class Etudiant(models.Model):
    Matricule = models.CharField(max_length=25, unique = True)
    Nom = models.CharField(max_length=50)
    Prenom = models.CharField("Prénom", max_length=50, blank=True, null=True)
    SEXE_CHOICES = [
        ("Masculin",'Masculin'),
        ('Féminin', 'Féminin')
    ]
    Sexe = models.CharField(choices = SEXE_CHOICES, max_length=50)
    Date_naiss = models.DateField("Date de naissance",)
    Lieu_naiss = models.CharField("Lieu de naissance", max_length=50)
    Quartier = models.CharField( max_length=50)
    Photo = models.ImageField(upload_to='image_eleves', blank=True, null=True)
    Nom_parent = models.CharField("Non du parents / Tuteur", max_length=50)
    Telephone = models.CharField("Téléphone", max_length=9)
    classe = models.ForeignKey("ClasseSession",  on_delete=models.SET_NULL, blank=True, null=True)


    def __str__(self):
        return f'{self.Nom} {self.Prenom}'

    def getAge(self):
        today = datetime.now().year
        print(today)

        return today - self.Date_naiss.year









    



