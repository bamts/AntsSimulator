# coding: utf8

"""
Taches.py - Module containing Tache class
import:
-------
Class stimulus from Stimuli module
imported by:
-------------
_Entree module, the main module
Proc_iterations module, for output
Fourmis module
Colonies module
TypesFourmis module
"""

from Stimuli import Stimulus


class Tache:
    """
    Class that represent a task
    Tasks are linked with stimuli
    Tasks are things that ants may have to do to maintain the colony
    nbTaches is the variable for handling identifier for Tache
    """

    nbTaches = 0

    def __init__(self, _nom_tache="TACHEDEFAUT", _stimulus=Stimulus(), _function=None):
        """
            Constructor of the class Tache
            An object of this class contains:
                A Name
                Its triggering stimulus
            The more stimuli that trigger this task are intense, the more ants will tend to do this task
        """
        Tache.nbTaches += 1
        self.__func = _function
        self.__idTache = Tache.nbTaches
        self.__nomTache = _nom_tache
        self.__stimulus = _stimulus

    def __str__(self):
        return " : {} \n\t{}\n\t".format(self.__nomTache, self.__stimulus)

    def __hash__(self):
        return hash(self.__nomTache)

    def __eq__(self, other):
        if type(other) == type(self):
            return self.__nomTache == other.get_name
        else:
            return self.__nomTache == other

    def __lt__(self, other):
        mine = self.__stimulus.get_intensite
        its = other.get_stimulus.get_intensite
        return mine < its

    @property
    def get_id(self):
        return self.__idTache

    @property
    def get_function(self):
        return self.__func

    @property
    def get_name(self):
        return self.__nomTache

    @property
    def get_stimulus(self):
        return self.__stimulus

    def set_stimulus(self, _stimulus):
        self.__stimulus = _stimulus

    def set_name(self, _nom):
        self.__nomTache = _nom

