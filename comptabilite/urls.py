from django.urls import path
from .views import *


urlpatterns = [

   path("", compta_index, name="comptabilite"),
   path("configurations", compta_config, name="compta_config"),
   path("add", compta_add_echeance, name="compta_add_echeance"),
   path("update/<id>", compta_update_echeance, name="compta_update_echeance"),
   path("delete/<id>", compta_delete_echeance, name="compta_delete_echeance"),
   path("paiements/", compta_payement, name="compta_payement"),
   path("paiements/creer", compta_payement_add_first, name="compta_payement_add_first"),
   path("paiements/creer/<matricule>", compta_payement_add_second, name="compta_payement_add_second"),
   path("paiements/creer/<matricule>/<echeance>", compta_payement_add_third, name="compta_payement_add_third"),
   path("solvabilites/", compta_solvabilite, name="compta_solvabilite"),
   path("paiements/<matricule>/", compta_paiement_details, name="compta_paiement_details"),
   path("moratoires/", moratoire_index, name="moratoire_index"),
   path("moratoires/créer", moratoire_create, name="moratoire_create"),

   
   
   
   

]  
