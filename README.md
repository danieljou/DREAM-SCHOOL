# DREAM SCHOOL - Système de gestion scolaire utilisant Django

DREAM SCHOOL est un système de gestion scolaire basé sur le web, construit en utilisant le framework web Django. Il fournit une interface conviviale pour gérer les tâches administratives de l'école, y compris les informations sur les élèves et les enseignants, la présence, les notes, les horaires, et plus encore.

## Installation

Pour commencer avec DREAM SCHOOL, suivez les étapes ci-dessous:

### Prérequis

Avant d'installer DREAM SCHOOL, assurez-vous d'avoir les logiciels suivants installés sur votre système:

- Python 3.x
- gestionnaire de paquets pip
- framework web Django

### Étape 1: Cloner le référentiel

Tout d'abord, clonez le référentiel DREAM SCHOOL depuis GitHub en utilisant la commande suivante:

```
git clone https://github.com/danieljou/dream-school.git
```

### Étape 2: Créer un environnement virtuel

Il est recommandé de créer un environnement virtuel pour installer les dépendances de DREAM SCHOOL. Cela garantit que les dépendances ne sont pas installées globalement sur votre système et ne sont pas en conflit avec d'autres projets.

Pour créer un environnement virtuel, exécutez les commandes suivantes:

```
cd dream-school
mkvirtualenv env
```

### Étape 3: Activer l'environnement virtuel

Activez l'environnement virtuel en utilisant la commande suivante:

```
workon env
```

### Étape 4: Installer les dépendances

Installez les dépendances requises pour DREAM SCHOOL en utilisant la commande suivante:

```
pip install -r requirements.txt
```

### Étape 5: Migrer la base de données

Migrez le schéma de la base de données en utilisant la commande suivante:

```
python manage.py migrate
```

### Étape 6: Créer un superutilisateur

Créez un compte de superutilisateur pour accéder à l'interface d'administration de DREAM SCHOOL en utilisant la commande suivante:

```
python manage.py createsuperuser
```

### Étape 7: Exécuter le serveur de développement

Démarrez le serveur de développement en utilisant la commande suivante:

```
python manage.py runserver
```

Vous pouvez maintenant accéder à DREAM SCHOOL à `http://localhost:8000/` dans votre navigateur web.

## Conclusion

Félicitations ! Vous avez réussi à installer DREAM SCHOOL sur votre système. Vous pouvez maintenant explorer les fonctionnalités du système de gestion scolaire et le personnaliser selon vos besoins. Si vous rencontrez des problèmes lors du processus d'installation, veuillez consulter la documentation officielle de Django ou le référentiel GitHub de DREAM SCHOOL pour obtenir de l'aide.
