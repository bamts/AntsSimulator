# coding: utf8

"""
TypesFourmis.py - Module containing TypeFourmi class
import:
-------
Class tache from Taches module
imported by:
-------------
_Entree module, the main module
Proc_iterations module, for output
Fourmis module
Colonies module
"""

from Taches import Tache


class TypeFourmi:
    """
        Class that represent an ant's(class: Fourmi) type
        Each ant own a type, which corresponds its usual behavior
        nbTypes is the variable for handling identifier for TypeFourmi
    """
    nbTypes = 0

    def __init__(self, _nomtype="TYPEDEFAULT", _repertoire=None, _phi=0.2, _xi=0.4, _p=0.2):
        """
        Constructor of the class TypeFourmi
        An object of this class contains:
            A type name
            A base task repertory
            This repertory is the initial one for all ant of this type
        The repertory should never be empty, as ants are allowed to do nothing at all,
        then when initializing a TypeFourmi repertoire is set

        :param _nomtype: The name of the type
        :type _nomtype: str
        :param _repertoire: Tasks with thresholds
        :type _repertoire: dict
        :param _phi: Forgetting rate
        :type _phi: float
        :param _xi: Learning rate
        :type _xi: float
        :param _p: Probability of stopping current action
        :type _p: float
        :return: An instance of TypeFourmi
        :rtype: TypeFourmi

        :Example:

        >>> t=TypeFourmi("TEST_TYPE")
        >>> t.add_tache_to_repertoire(Tache("TEST_TASK"), 0.5)
        >>> print(str(t))
        TEST_TYPE, Phi=1.0, Xi=10.0:
        ----------
            TACHEDEFAUT: 0
            TEST_TASK: 0.5
        >>> tache1 = Tache("Se pavaner")
        >>> tache2 = Tache("Imposer le respect")
        >>> typeAlpha = TypeFourmi("TYPE_ALPHA",dict(zip([tache1, tache2],[0.5, 0.5])), 0.4, )
        >>> print(str(typeAlpha))
        TYPE_ALPHA, Phi=0.4, Xi=10.0:
        -----------
            Se pavaner: 0.5
            Imposer le respect: 0.5
            TACHEDEFAUT: 0

        """
        TypeFourmi.nbTypes += 1
        self.__idType = TypeFourmi.nbTypes

        self.__nomType = _nomtype

        # Si le parametre repertoire n'est pas donné par defaut,
        #  il peut etre donnée avec la fonction addTachesToRepertoire
        #  dans ce cas on le laisse à vide

        if not _repertoire:
            _repertoire = {}
        self.__repertoire = _repertoire
        self.__repertoire[Tache()] = 0
        self.__Phi = float(_phi)
        self.__Xi = float(_xi)
        self.__p = _p

    def __str__(self):
        """For display"""
        toreturn = ["{}, Phi={}, Xi={}:\n".format(self.__nomType, self.__Phi, self.__Xi)]

        for i in range(0, self.__nomType.__len__() + 1):
            toreturn.append('-')

        for rep in self.__repertoire:
            toreturn.append("\n\t{}: {}".format(rep.get_name, str(self.__repertoire[rep])))
        return "".join(toreturn)

    def __lt__(self, other):
        return self.__idType < other.get_id

    @property
    def get_id(self):
        return self.__idType

    @property
    def get_phi(self):
        return self.__Phi

    @property
    def get_xi(self):
        return self.__Xi

    @property
    def get_name(self):
        return self.__nomType

    def add_tache_to_repertoire(self, _tache, _seuil):
        self.__repertoire[_tache] = _seuil

    @property
    def get_repertoire_init(self):
        return self.__repertoire

    @property
    def get_p(self):
        return self.__p


if __name__ == '__main__':
    import doctest
    import os
    import sys
    from time import *

    fileName = "TypesFourmis_{}{}{}_{}{}{}".format(strftime('%d'), strftime('%m'),
                                                   strftime('%Y'), strftime('%H'),
                                                   strftime('%M'), strftime('%S'))
    directory = os.getcwd() + "\\Tests\\"
    if not os.path.exists(directory):
        os.makedirs(directory)

    sys.stdout = open(directory + fileName, 'w')

    doctest.testmod(verbose=True, optionflags=doctest.ELLIPSIS + doctest.NORMALIZE_WHITESPACE)
    sys.stdout.close()

    sys.stdout = sys.__stdout__

    print("Test de la classe TypeFourmis dans le fichier :\n"
          "{}\n".format(fileName))

    fichier_test = open(directory + fileName, 'r')

    lines = fichier_test.readlines()

    if not lines[len(lines)-1].strip() == "Test passed.":
        x = input("Le test a échoué voulez-vous ouvrir le fichier pour résoudre les tests? (O/n)")
        if x == "n":
            print("Merci")
        else:
            os.system("notepad.exe {}".format(directory + fileName))

