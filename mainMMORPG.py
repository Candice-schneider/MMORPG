import sys
from Personnage import Personnage
from Mage import Mage
from Guerrier import Guerrier
from Joueur import Joueur


def main():
    p1 = Personnage('perso1')
    p2 = Personnage('perso2', niveau=2)
    print(p1)
    print(p2)

    p1.combat(p2)
    if p1.vie > p2.vie and p1.vie > 0:
        print(f"{p1.pseudo} a gagné")
    elif p1.vie < p2.vie and p2.vie > 0:
        print(f"{p2.pseudo} a gagné")
    else:
        print(f"{p1.pseudo} et {p2.pseudo} sont tous les deux morts.")

    g1 = Guerrier(pseudo='guerrier')
    print(g1)

    m1 = Mage(pseudo='mage')
    print(m1)

    m1.combat(g1)
    if m1.vie > g1.vie and m1.vie > 0:
        print(f"{m1.pseudo} a gagné, il lui reste {m1.vie} points de vie")
    elif m1.vie < g1.vie and g1.vie > 0:
        print(f"{g1.pseudo} a gagné, il lui reste {g1.vie} points de vie")
    else:
        print(f"{m1.pseudo} et {g1.pseudo} sont tous les deux morts.")

    print("********\n\n\n")
    j1 = Joueur('joueur1', 3)
    j1.ajout_perso(m1)
    j1.ajout_perso(g1)
    j1.ajout_perso(p2)
    j1.ajout_perso(p1)
    j1.get_perso_num(1)
    j1.del_perso_num(1)
    print([(str(k)) for k in j1.liste])
    return 0


if __name__ == '__main__':
    sys.exit(main())
