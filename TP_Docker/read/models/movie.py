# * L'attribut de classe :
#     * `id` (int) (il sera incrémenté dans le constructeur mais attention il commencera à 31 -> movie.csv)

# * Les attributs :

#   * `titre` (str)
#   * `annee_production` (int)
#   * `genre` (str)
#   * `age_limite` (int)
# * Une méthode spéciale `__str__` qui affichera les informations du film de manière lisible.


class Movie :
    

    
    def last_index():
        donnees = []
        with open('read/data/movies.csv', mode='r', newline='', encoding='utf-8') as fichier:
            lecteur = csv.DictReader(fichier)
            for ligne in lecteur:
                donnees.append(ligne)
        
        return donnees[-1]["id"] +1
    
    def __init__(self, titre : str, annee_production : int, genre : str, age_limite : int):
         
        self.id = Movie.last_index()
        self.titre = titre
        self.annee_production = annee_production
        self.genre = genre
        self.age_limite = age_limite
        Movie.nb_movie += 1
        

        
    def __str__(self) :
        print()
        print(f"===== {self.id} : {self.titre} ======")
        print(f"année de production : {self.titre}")
        print(f"genre : {self.titre}")
        print(f"âge limite : {self.titre}")
        print()
        
        
