import csv
from models.movie import Movie

def charger_donnees():
    donnees = []
    with open('data/movies.csv', mode='r', newline='', encoding='utf-8') as fichier:
        lecteur = csv.DictReader(fichier)
        for ligne in lecteur:
            donnees.append(ligne)
    return donnees


# **Ajouter un film**

#    * Demander les informations nécessaires à l’utilisateur.
#    * Créer un objet `Movie`.
#    * Ajouter ce film dans le fichier `movies.csv`.
#    * Commiter votre travail & merge.

    
def ajouter_film_liste(liste_movie : list) :
    
    titre = input("Quel est le titre du film : ")
    annee_production = input("Quel est l'année de production : ")
    genre = input("quel est le genre du film : ") 
    age_limite = input("Quel est l'âge limite pour le film : ")
    
    # m = [int(liste_movie[-1]["id"])+1,mov.titre,str(mov.annee_production),mov.genre,mov.age_limite]
    # liste_movie.append(m)
    
    m = Movie(titre,annee_production,genre,age_limite)
    nouvelle_ligne = [Movie.last_index(), m.titre, m.annee_production, m.genre, m.age_limite]
    #nouvelle_ligne = [int(liste_movie[-1]["id"])+1, titre, annee_production, genre, age_limite]
    print(nouvelle_ligne)
   
    try :
        with open("data/movies.csv", mode="a", newline="", encoding="utf-8") as fichier:
            ecrivain = csv.writer(fichier)
            ecrivain.writerow(nouvelle_ligne)
    except :
        print ("erreur écriture")
    else :     
        print("ajout réalisé avec succès")

def rechercher_movie(liste_movie : list, id : int) -> Movie :
    for m in liste_movie :
        if int(m["id"]) == id : 
            return m

def afficher_csv() :
    lm = charger_donnees()
    for m in lm :
        mov = Movie(m["titre"],m["annee_production"],m["genre"],m["age_limite"],m["id"])
        mov.__str__()

def supprimer_dans_liste(lm : list,id : int) :
    for i,m in enumerate(lm) :
        if int(m["id"]) == id :
            del lm[i]


def modifier_movie(id : int) :
    lm =charger_donnees()
    afficher_csv()
    id_movie = input("Quel est l'identifiant du film à modifier : ")
    rechercher_movie(lm,id)
    n_titre = input("Nouveau titre du film à modifier : ")
    n_annee = input("Nouvelle année du film à modifier : ")
    n_genre = input("Nouveau genre du film à modifier : ")
    n_age = input("Nouvel age limite du film à modifier : ")
    #m_tmp = Movie(n_titre,n_annee,n_genre,n_age)   
    d_movie = {"id" : id_movie,"titre" : n_titre, "annee_production" : n_annee, "genre" : n_genre, "age_limite" : n_age}
    
    supprimer_dans_liste(lm,id)

    #print(f"d_movie : {d_movie}")
    
    for i, m in enumerate(lm) :
        if int(id_movie) == i :
            print("avant modif : ", lm[i])
            lm[i] = d_movie
            print("après modif : ", lm[i])
    
    champs = ["id","titre","annee_production","genre","age_limite"]
    with open("data/movies.csv", mode="w", newline="", encoding="utf-8") as fichier:
           ecrivain = csv.DictWriter(fichier,fieldnames=champs)
           ecrivain.writeheader()
           ecrivain.writerows(lm)
    
def supprimer_movie(id : int) :
    lm = charger_donnees()
    supprimer_dans_liste(lm,id)
    
    champs = ["id","titre","annee_production","genre","age_limite"]
    with open("data/movies.csv", mode="w", newline="", encoding="utf-8") as fichier:
        ecrivain = csv.DictWriter(fichier,fieldnames=champs)
        ecrivain.writeheader()
        ecrivain.writerows(lm)
    print("suppression réalisée avec succès")
        
    
#lm = charger_donnees()

#print(Movie.last_index())

#m = Movie("yyy",1977,"gg",45)
#print(lm)
# afficher_csv()
#ajouter_film_liste(lm)
#print(rechercher_movie(lm,22))

supprimer_movie(22)