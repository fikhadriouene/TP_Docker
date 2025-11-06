# * L'attribut de classe :
#     * `id` (int) (il sera incrémenté dans le constructeur mais attention il commencera à 31 -> movie.csv)

# * Les attributs :

#   * `titre` (str)
#   * `annee_production` (int)
#   * `genre` (str)
#   * `age_limite` (int)
# * Une méthode spéciale `__str__` qui affichera les informations du film de manière lisible.

import csv

class Movie :
    
    def last_index():
        donnees = []
        with open('data/movies.csv', mode='r', newline='', encoding='utf-8') as fichier:
            lecteur = csv.DictReader(fichier)
            for ligne in lecteur:
                donnees.append(ligne)
        
        print(f"IDENTIFIANT : {int(donnees[-1]["id"])}")
        return (int(donnees[-1]["id"]) + 1)
    
    #nb_movie = last_index()
    
    
    def __init__(self, titre : str, annee_production : int, genre : str, age_limite : int,id : int=-1):
        if id == -1 :
            self.id = Movie.last_index()
        else :
            self.id = id
        # Movie.nb_movie += 1
        #self.id = Movie.nb_movie
        self.titre = titre
        self.annee_production = annee_production
        self.genre = genre
        self.age_limite = age_limite
        
        
        

        
    def __str__(self) :    
        chaine = "===== {self.id} : {self.titre} ======\n annnée de production : {self.annee_production}\n genre : {self.genre} \n âge limite : {self.age_limite}"
        return chaine
        
        