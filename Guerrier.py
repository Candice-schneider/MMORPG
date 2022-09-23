from Personnage import Personnage


class Guerrier(Personnage):
    def __init__(self, pseudo: str, niveau: int = 1):
        super().__init__(pseudo, niveau)
        self.initiative = niveau * 8 + 4
        self.vie = niveau * 4 + 6

    def __str__(self):
        return f"Le Guerrier {self.pseudo} est de niveau {self.niveau}, il a {self.vie}" \
               f" point(s) de vie et a {self.initiative} initiative(s)"

    def soin(self) -> None:
        self.__vie = self.__niveau*8+4
        self.__initiative = self.__niveau*4+6

    def degat(self) -> int:
        return self.__niveau*2
