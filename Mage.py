from Personnage import Personnage


class Mage(Personnage):
    def __init__(self, pseudo: str, niveau: int = 1):
        super().__init__(pseudo, niveau)  # toujours utiliser cette formulation si utilisation de property
        self.initiative = niveau * 6 + 4
        self.vie = niveau * 5 + 10
        self.__mana = niveau * 5

    def __str__(self):
        return f"Le Mage {super().__str__()}"

    def soin(self):
        self.__vie = self.__niveau * 5 + 10
        self.__initiative = self.__niveau * 6 + 4

    def degat(self) -> int:
        if self.__mana < 0:
            self.__mana -= 4
            return self.__niveau + 3
        else:
            return self.__niveau
