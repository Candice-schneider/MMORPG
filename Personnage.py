class Personnage:
    def __init__(self, pseudo: str, niveau: int = 1, vie: float = 1, initiative: int = 1):
        self.__pseudo = pseudo
        self.__niveau = niveau
        self.__vie = vie
        self.__initiative = initiative
        if self.__niveau != 1:
            self.__vie = self.__niveau
            self.__initiative = self.__niveau

    def __str__(self) -> str:
        return f"Le joueur {self.__pseudo} est au niveau {self.__niveau}. " \
               f"Il a {self.__vie} points de vie et {self.__initiative} initiative"

    @property
    def vie(self):
        return self.__vie

    @property
    def niveau(self):
        return self.__niveau

    @property
    def initiative(self):
        return self.__initiative

    @property
    def pseudo(self):
        return self.__pseudo

    @vie.setter
    def vie(self, v: int):
        self.__vie = v

    @niveau.setter
    def niveau(self, n: int):
        self.__niveau = n

    @initiative.setter
    def initiative(self, i: int):
        self.__initiative = i

    @pseudo.setter
    def pseudo(self, p: str):
        self.__pseudo = p

    def attaque(self, other):
        """le joueur avec le plus d'initiative commence, si l'autre a encore
        des points de vie alors il attaque à son tour. si les deux personnages
        ont le même nombre d'initiative, alors ils attaquent en même temps."""
        if self.initiative > other.initiative:
            other.vie -= self.degats()
            if other.vie > 0:
                self.vie -= other.degats()

        elif self.initiative < other.initiative:
            self.vie -= other.degats()
            if self.vie > 0:
                other.vie -= self.degats()

        else:
            print(f"et son adversaire l'attaque simultanément")
            other.vie -= self.degats()
            self.vie -= other.degats()

    def combat(self, other) -> None:
        """succession de plusieurs attaques"""
        l = [other, self]
        print(f"***** début du combat entre {self.pseudo} et {other.pseudo} *****")
        while other.vie > 0 and self.vie > 0:
            l[0].attaque(l[1])
            print(f"\n{l[1].pseudo} attaque {l[0].pseudo}")
            l.append(l.pop(0))
            print(f"\t{l[0].pseudo} a {l[0].vie} point(s) de vie")
            print(f"\t{l[1].pseudo} a {l[1].vie} point(s) de vie")

    def soigner(self) -> None:
        if self.__vie < self.__niveau:
            self.__vie = self.__niveau
        else:
            print("ce personnage a encore trop de points de vie")  # juste au cas où pour vérifier

    def degats(self) -> int:
        return self.__niveau
