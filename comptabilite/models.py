from django.db import models

# Create your models here.

class EcheancePaiement(models.Model):
    designation = models.CharField(max_length=50)
    date_debut = models.DateTimeField('Date de début')
    date_fin = models.DateTimeField("Date de fin")
    montant = models.PositiveIntegerField()
    session = models.ForeignKey("main.Session", on_delete=models.CASCADE)
    niveau  = models.ForeignKey("main.Niveau", on_delete=models.CASCADE)


class Payment(models.Model):
    montant = models.PositiveIntegerField()
    eleve = models.ForeignKey("main.Etudiant", on_delete=models.CASCADE)
    echeance = models.ForeignKey("EcheancePaiement",  on_delete=models.CASCADE)
    date_paiement = models.DateField('date de paiement',  auto_now_add=True)


class Moratoire(models.Model):
    
    eleve = models.ForeignKey("main.Etudiant", related_name = "Elève", on_delete=models.CASCADE)
    Motif = models.TextField()
    session = models.ForeignKey("main.Session",  on_delete=models.CASCADE)
class Tranche(EcheancePaiement):
    
    moratoire = models.ForeignKey("Moratoire",  on_delete=models.CASCADE)





