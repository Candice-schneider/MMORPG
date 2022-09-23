from Personnage import Personnage


class Joueur():
    def __init__(self, nom: str, nb: int):
        self.__nom = nom
        self.__nb = nb
        self.__liste = [None for k in range(self.__nb)]
        #liste = [Personnage(str([i])) for i in range(nb)]

    def __str__(self):
        return f"le joueur {self.__nom} a {self.__nb} personnages: {[k for k in self.__liste]}"

    @property
    def liste(self):
        return self.__liste

    def ajout_perso(self, p: Personnage):
        i = 0
        while i<len(self.__liste):
            if self.__liste[i] == None:
                self.__liste[i]  = p
                break
            else:
                i+=1
        if i>=len(self.__liste):
            print("il y a déjà le maximum de personnages possible pour ce joueur")

    def get_perso_num(self, n:int):
        if n < len(self.__liste):
            print(self.liste[n])
            return self.__liste[n] #problème ici !!
        else:
            print("ce personnage n'existe pas")

    def get_perso_pseudo(self, p: str):
        for p in self.__liste:
            if p.pseudo == p:
                return p

    def get_perso(self, perso:Personnage):
        for p in self.__liste:
            if p == perso:
                return p

    def del_perso_num(self, n: int):
        if n < len(self.__liste):
            #print(self.liste[n])
            del(self.__liste[n])
            return self.__liste
        else:
            print("ce personnage n'existe pas")

    def del_perso_pseudo(self, p: str):
        for p in self.__liste:
            if p.pseudo == p:
                del(p)

    def del_perso(self, perso:Personnage):
        for p in self.__liste:
            if p == perso:
                del(p)

