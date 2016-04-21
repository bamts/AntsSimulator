# coding: utf8

"""
Colonies.py - Module containing Colonie class
import:
-------
Class Fourmi from Fourmis module
Class TypeFourmi from TypesFourmis
imported by:
-------------
_Entree module, the main module
Proc_iterations module, for output
"""

from Fourmis import Fourmi
from TypesFourmis import TypeFourmi
import numpy


class Colonie:
    """
        Class that represents an ant's colony
        This contains numbered typed ants

        nbColonies is the variable for handling identifier for Colonie
    """
    nbColonies = 0

    def __init__(self, *_nbfourmispartype, _pos=None):
        """
            Constructor of the class Colonie
            An object of this class contains:
                The number of types of ant it that are represented
                The number of ants of each existing type
                A list containing all its individuals
                The total number of individuals

            :param: _nbfourmispartype: types and corresponding number
                odds are the types
                pairs are the numbers (corresponding to precedent type)
            :type: _nbfourmispartype: list
            :return: The initialized colony with ants that are created depending on _nbfourmispartype

            :Example:

            >>> c=Colonie(TypeFourmi(),1)
            >>> print(c)
            Colonie : 1, contenant: 1 fourmis de type TYPEDEFAULT :
            >>> c=Colonie(TypeFourmi("TType1"),1,TypeFourmi("TType2"),2)
            >>> print(c)
            Colonie : 2, contenant: 1 fourmis de type TType1 : 2 fourmis de type TType2 :
        """
        Colonie.nbColonies += 1
        self.__idColonie = Colonie.nbColonies
        self.__nbTypes = len(_nbfourmispartype) / 2
        self.__nbFourmis = {}
        self.__fourmis = []
        self.__taille = 0
        self.__position = _pos

        if self.__nbTypes != 0:
            for i in range(0, int(self.__nbTypes) * 2, 2):
                self.__nbFourmis[_nbfourmispartype[i]] = _nbfourmispartype[i + 1]
            for i in self.__nbFourmis:
                self.__taille += self.__nbFourmis[i]
                for y in range(0, self.__nbFourmis[i]):
                    if self.__position:
                        f = Fourmi(i, self.__position[0], self.__position[1])
                    else:
                        f = Fourmi(i, int(numpy.random.random()*100), int(numpy.random.random()*100))
                    self.__fourmis.append(f)
        else:
            self.__nbFourmis[TypeFourmi()] = 0

    def __str__(self):

        toreturn = "Colonie : {}, contenant:".format(str(self.__idColonie))
        for i in sorted(self.__nbFourmis.keys()):
            toreturn = "{} {} fourmis de type {} :".format(toreturn, str(self.__nbFourmis.get(i, 0)), i.get_name)

        return toreturn

    def __lt__(self, other):
        return self.__idColonie < other.get_id

    @property
    def get_nb_fourmis(self):
        return self.__taille

    @property
    def get_id(self):
        return self.__idColonie

    def liste_individus(self):
        """Affiche simplement la liste des fourmis d'une colonie"""
        if self.__taille != 0:
            for f in sorted(self.__fourmis):
                print(str(f))
                x = f.get_x
                if x is not None:
                    print(str(x), str(f.get_repertoire[x]))
    @property
    def get_fourmis(self):
        return self.__fourmis


if __name__ == '__main__':

    import doctest
    import os
    import sys
    from time import *

    fileName = "Colonies_{}{}{}_{}{}{}".format(strftime('%d'), strftime('%m'),
                                                   strftime('%Y'), strftime('%H'),
                                                   strftime('%M'), strftime('%S'))
    directory = os.getcwd() + "\\Tests\\"
    if not os.path.exists(directory):
        os.makedirs(directory)

    sys.stdout = open(directory + fileName, 'w')

    doctest.testmod(verbose=True, optionflags=doctest.ELLIPSIS + doctest.NORMALIZE_WHITESPACE)
    sys.stdout.close()

    sys.stdout = sys.__stdout__

    print("Test de la classe Colonie dans le fichier :\n"
          "{}\n".format(fileName))

    fichier_test = open(directory + fileName, 'r')

    lines = fichier_test.readlines()

    if not lines[len(lines)-1].strip() == "Test passed.":
        x = input("Le test a échoué voulez-vous ouvrir le fichier pour résoudre les tests? (O/n)")
        if x == "n":
            print("Merci")
        else:
            os.system("notepad.exe {}".format(directory + fileName))
