from django.urls import path
from .views import *


urlpatterns = [
   path('',index, name='home'),

   # GESTION DES ANNEE SCOLAIRES

   path("session/", session, name="session"),
   path("session/createSession/", createSession, name="createSession"),
   path("session/updatesession/<id>", updatesession, name="updatesession"),
   path("session/deletesession/<id>", deletesession, name="deletesession"),

    # GESTION DES NIVEAUX D'ETUDES

   path("niveaux/", niveaux, name="niveau"),
   path("niveaux/createniveau/", createniveau, name="createniveau"),
   path("niveaux/updateniveau/<id>", updateniveau, name="updateniveau"),
   path("niveaux/deleteniveau/<id>", deleteniveau, name="deleteniveau"),

   # GESTION DES SALLES DE CLASSES

   path("salles/", salles, name="salles"),
   path("salles/createsalle/", createsalle, name="createsalle"),
   path("salles/updatesalle/<id>", updatesalle, name="updatesalle"),
   path("salles/deletesalle/<id>", deletesalle, name="deletesalle"),


     # GESTION DES SALLES DE CLASSES

   path("salles_session/", salles_session, name="salles_session"),
   path("salles_session/createsalle_session/", createsalle_session, name="createsalle_session"),
   path("salles_session/updatesalle_session/<id>", updatesalle_session, name="updatesalle_session"),
   path("salles_session/deletesalle_session/<id>", deletesalle_session, name="deletesalle_session"),
   path("salles_session/detailssalle_session/<id>", detailssalle_session, name="detailssalle_session"),

 # GESTION DES MATIERES

   path("matieres/", matieres, name="matieres"),
   path("matieres/creatematiere/", creatematiere, name="creatematiere"),
   path("matieres/updatematiere/<id>", updatematiere, name="updatematiere"),
   path("matieres/deletematiere/<id>", deletematiere, name="deletematiere"),

   # GESTION DES MATIERES

   path("matieres_coef/", matieres_coefs, name="matieres_coef"),
   path("matieres_coefs/creatematiere_coef/", creatematiere_coef, name="creatematiere_coef"),
   path("matieres_coefs/updatematiere_coef/<id>", updatematiere_coef, name="updatematiere_coef"),
   path("matieres_coefs/deletematiere_coef/<id>", deletematiere_coef, name="deletematiere_coef"),


   path("profile/", profile, name="profile"),


   path("eleves/", eleves, name="eleves"),
   path("eleves/add", AddEleve, name="eleveAdd"),
   path("eleves/details/<matricule>", eleveDetails, name="eleveDetails"),
   path("eleves/update/<matricule>", eleveUpdate, name="eleveUpdate")



]  
