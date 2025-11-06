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

def film_par_age(age_limite :int) :
    lm = charger_donnees()
    l_film = []
    for m in lm :
        if int(m["age_limite"]) <= age_limite :
            #mov = Movie(m['id'],m['titre'],m['annee_production'],m['genre'],m['age_limite'])
            t = [m["id"],m["titre"],m["annee_production"],m["genre"],m["age_limite"]]
            l_film.append(t)

    return l_film

def film_par_genre(genre :str) :
    lm = charger_donnees()
    l_film = []
    for m in lm :
        print(i)
        if m["genre"] == genre :
            #mov = Movie(m["id"],m["titre"],m["annee_production"],m["genre"],m["age_limite"])
            t = [m["id"],m["titre"],m["annee_production"],m["genre"],m["age_limite"]]
            l_film.append(t)
    return l_film

def film_par_entre_dates(date1 : int, date2 : int) :
    lm = charger_donnees()
    l_film = []
    for m in lm : 
        if int(m["annee_production"]) >= date1 and int(m["annee_production"]) <= date2  :
            t = [m["id"],m["titre"],m["annee_production"],m["genre"],m["age_limite"]]
            l_film.append(t)
    return l_film

print(film_par_entre_dates(1977,2000))

