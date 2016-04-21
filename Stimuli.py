import numpy
import math

"""
Stimuli.py - Module containing Stimulus class
import:
-------
None
imported by:
-------------
_Entree module, the main module
Proc_iterations module, for output
Fourmis module
Taches module
"""


def sin(taille):
    toReturn = []
    for i in range(taille):
        toReturn.append((math.sin(i/10.0)+1)/2)
    return toReturn


def cosin(taille):
    toReturn = []
    for i in range(taille):
        toReturn.append((math.cos(i)+1)/2)
    return toReturn


def unif(taille):
    toReturn = []
    for i in range(taille):
        toReturn.append(numpy.random.random())
    return toReturn


def sqrt(taille):
    toReturn = []
    for i in range(taille):
        toReturn.append(math.sqrt(i)/(math.sqrt(taille)))
    return toReturn


class Stimulus:
    """
        Class that represents a stimulus type
        A Stimulus corresponds (mostly) to external change in the environment
        Here we can make its intensity evolve in time to simulate the increase of the need to respond to it
        nbStimulus is the variable for handling identifier for Stimulus
    """
    nbStimulus = 0

    def __init__(self, _nom_stimulus="STIMULUSDEFAULT", _intensite=0.0, _couverture=None, _gravity=None):
        """
            Constructor of the class Stimuli
            An object of this class contains:
                A name
                An initial intensity
                Intensity should always be bounded by minIntensite and maxIntensite

            :param _nom_stimulus: The name of the stimulus
            :type _nom_stimulus: str
            :param _intensite: intensity of the stimulus
            :type _intensite: float
        """
        self.__prepared = []
        self.__altered = []
        self.__minIntensite = 0.01
        self.__maxIntensite = 0.99
        Stimulus.nbStimulus += 1
        self.__idStimulus = Stimulus.nbStimulus
        self.__nomStimulus = _nom_stimulus
        self.__intensite = _intensite
        self.__function = None
        self.__color = None
        self.__couverture = _couverture
        if _couverture:
            if _gravity:
                self.__gravity_centerX = _gravity[0]
                self.__gravity_centerY = _gravity[1]
            else:
                self.__gravity_centerX = (_couverture[2] - _couverture[0])/2 + _couverture[0]  # todo parametre en % couv
                self.__gravity_centerY = (_couverture[3] - _couverture[1])/2 + _couverture[1]
        else:
            self.__gravity_centerY = None
            self.__gravity_centerX = None

    def __str__(self):
        return "Stimulus: {}|{} intensite: {}".format(str(self.__idStimulus), self.__nomStimulus, str(self.__intensite))

    def __eq__(self, other):
        return other.get_name == self.__nomStimulus

    @property
    def get_id(self):
        return self.__idStimulus

    @property
    def get_color(self):
        return self.__color

    @property
    def get_altered(self):
        return self.__altered

    @property
    def get_couverture(self):
        return self.__couverture

    @property
    def get_func(self):
        return self.__function

    @property
    def get_name(self):
        return self.__nomStimulus

    @property
    def get_intensite(self):
        return self.__intensite

    @property
    def get_prepared_values(self):
        if self.__prepared:
            return self.__prepared

    @property
    def get_gravity(self):
        return self.__gravity_centerX, self.__gravity_centerY

    def push_altered(self, intensite, i):
        self.__altered.insert(i, intensite)

    def set_intensite(self, _intensite):
        self.__intensite = _intensite

    def set_couverture(self, _couv):
        self.__couverture = _couv

    def set_color(self, color):
        self.__color = color

    def dec_intensite(self):
        if self.__intensite - 10/100 > self.__minIntensite:
            self.__intensite -= 10/100
        else:
            self.__intensite = self.__minIntensite

    def inc_intensite(self):
        if self.__intensite + 50/100 < self.__minIntensite:
            self.__intensite += 50/100
        else:
            self.__intensite = self.__maxIntensite

    def compute_stimulus(self, t):
        if self.__prepared:
            self.__intensite = sorted([self.__minIntensite, self.__prepared[t], self.__maxIntensite])[1]

    def set_func(self, _nom, *_args):
        if _nom == "UNIF":
            self.__function = unif

        if _nom == "SIN":
            self.__function = sin

        if _nom == "COSIN":
            self.__function = cosin

        if _nom == "SQRT":
            self.__function = sqrt

    def prepare_func(self, _time):
        toReturn = []
        if self.__function:
            fun = self.__function
            toReturn = fun(_time)
        self.__prepared = toReturn
        return toReturn

