# * L'attribut de classe :
#     * `id` (int) (il sera incrémenté dans le constructeur mais attention il commencera à 31 -> movie.csv)

# * Les attributs :

#   * `titre` (str)
#   * `annee_production` (int)
#   * `genre` (str)
#   * `age_limite` (int)
# * Une méthode spéciale `__str__` qui affichera les informations du film de manière lisible.


class Movie :
    def __init__(self, id :int, titre : str, annee_production : int, genre : str, age_limite : int):
        self.id = 31
        self.titre = titre
        self.annee_production = annee_production
        self.genre = genre
        self.age_limite = age_limite
        
    def __str__(self) :
        print()
        print(f"===== {self.titre} ======")
        print(f"année de production : {self.titre}")
        print(f"genre : {self.titre}")
        print(f"âge limite : {self.titre}")
        print()
        
        
        