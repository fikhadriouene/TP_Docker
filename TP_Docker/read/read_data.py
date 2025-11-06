# ### 7. Script de lecture – `read_data.py`

# Dans le dossier `read`, créer le script `read_data.py` qui permettra de lire et filtrer les films depuis le fichier CSV.

# Fonctionnalités attendues :

# 1. Récupérer un film par son titre.
#    * Commiter votre travail & merge.
# 2. Récupérer la liste des films ayant une limite d’âge inférieure ou égale à une valeur donnée.
#    * Commiter votre travail & merge.
# 3. Récupérer la liste des films d’un certain genre.
#    * Commiter votre travail & merge.
# 4. Récupérer la liste des films produits entre deux années données (année de début et année de fin).
#    * Commiter votre travail & merge.
import csv

from models.movie import Movie

def charger_donnees():
    donnees = []
    with open('data/movies.csv', mode='r', newline='', encoding='utf-8') as fichier:
        lecteur = csv.DictReader(fichier)
        for ligne in lecteur:
            donnees.append(ligne)
    return donnees

def film_par_titre(titre :str) :
    lm = charger_donnees()
    for m in lm :
        if m["titre"] == titre :
            mov = Movie(m['id'],m['titre'],m['annee_production'],m['genre'],m['age_limite'])
            print(m)
            return mov

m = film_par_titre("Inception")
m.__str__()
