# coding=utf8


"""
Fourmis.py - Module containing Fourmi class
import:
-------
Class Tache from Taches module
random module, for selection
Class Stimulus from Stimuli module
Class TypesFourmis from TypeFourmi module
imported by:
-------------
Colonies module
Proc_iterations module, for output
"""

import random
import os
from TypesFourmis import TypeFourmi
from Stimuli import Stimulus
from Taches import Tache
import numpy as np


class Fourmi:
    """
        Class that represents an ant
        A Stimulus corresponds (mostly) to external change in the environment
        nbFourmi is the variable for handling identifier for Fourmi
    """
    nbFourmis = 0

    def __init__(self, _type_fourmi=TypeFourmi(), _posX=50, _posY=50):
        """
        Constructor of the class Fourmi
        An object of this class contains:
            A type
            An initial repertory set as the one of the type of this ant
            A count of tiredness
            The current task of the ant, initialized as None
            A counter of busyness, corresponding to time left before ant is ready
            The memory of the ant, for keeping track of tasks done before

        :param _type_fourmi a Type of ants
        """
        Fourmi.nbFourmis += 1
        self.__idFourmi = Fourmi.nbFourmis
        self.__typeFourmi = _type_fourmi
        self.__repertoire = _type_fourmi.get_repertoire_init
        self.__fatigue = 0  # TODO use this parameter
        self.__X = None
        self.__busy = 0
        self.__memory = []
        self.__fileName = os.getcwd() + "\\Fourmis\\fourmi{}".format(self.__idFourmi)
        self.__posX = _posX
        self.__posY = _posY
        self.__fullMemory = []
        self.__energy = 0

    def __str__(self):
        to_return = "Fourmi{}:\n{}\n".format(str(self.__idFourmi), str(self.__typeFourmi))
        return to_return

    def __lt__(self, other):
        """
        For sorting the ants via the identifier
        :param other:
        :return:
        """
        return self.__idFourmi < other.get_id

    @property
    def get_id(self):
        return self.__idFourmi

    @property
    def get_coords(self):
        return self.__posX, self.__posY

    @property
    def get_full_mem(self):
        return self.__fullMemory

    @property
    def get_type(self):
        return self.__typeFourmi

    @property
    def get_x(self):
        return self.__X

    @property
    def get_fatigue(self):
        return self.__fatigue

    @property
    def get_repertoire(self):
        return self.__repertoire

    @property
    def is_busy(self):
        return self.__busy > 0

    @property
    def get_busy(self):
        return self.__busy

    def inc_tiredness(self):
        self.__fatigue += 1

    def dec_busy(self):
        self.__busy -= 1

    def update_theta(self):
        """
        For each task in repertory, if the task has been done recently lower its thresholds else increase it
        Uses learning 'xi' and forgetting 'phi' parameters of self's type for modulating the evolution of the threshold
        :return: Modifies the thresholds for self and clears memory
        """
        xi = self.__typeFourmi.get_xi
        phi = self.__typeFourmi.get_phi

        for t in self.__repertoire:
            if t.get_name != "TACHEDEFAUT":
                cur = self.__repertoire[t]
                if t == self.__X:
                    cur -= xi
                else:
                    cur += phi
                self.__repertoire[t] = sorted([0, cur, 1.0])[1]  # bounded value of cur

    def selection(self, _liste_stimulus, exp_duration):
        """
        Choose depending of the intensity of all perceived stimulus which action to do next

        :param _liste_stimulus: the intensity of each perceived stimulus
        :return: a Tuple : (choice, value, T)
            choice is the chosen action to do next
            value is the random throw that lead to the decision
            T tasks witt thresholds
        """

        val = 0
        T = {}
        result = None
        if self.__energy == 0:
            self.__energy = int(np.random.random()*exp_duration)
            for rep in self.__repertoire:
                if rep == "Repos":
                    result = rep, 1.
        else:
            for rep in self.__repertoire:
                # Pour chaque tâche du répertoire
                for sti in _liste_stimulus:
                    mat_couverture = list(sti.get_couverture)
                    if mat_couverture[0] <= self.__posX and mat_couverture[1] <= self.__posY:
                        if mat_couverture[2] > self.__posX and mat_couverture[3] > self.__posY:
                            # Pour tous les stimuli
                            if sti == rep.get_stimulus:
                                # si le stimulus stimule cette tâche sa valeur d'intensité est ajoutée à val
                                val = sti.get_intensite

                if val > 0:
                    T[rep] = val**2/(val**2+self.__repertoire[rep])

                val = 0

            result = weighted_choice(T)

        self.__X = result[0]

        self.__busy = self.working()
        self.__fullMemory.append((result[0].get_id, result[0].get_name, self.__busy))
        self.__fullMemory.append((result[0].get_id, result[0].get_name, 1))

        return result[0], result[1], T

    def working(self):
        """
        Use p, the probability of stopping current task to randomly get the time of the next decision
        Should be called right after selection of next action
        :return: cpt, an integer meaning the time left working on current task
        """
        # todo = self.__x[0].get_function
        p = self.__typeFourmi.get_p
        cpt = 0
        while 1:
            cpt += 1
            res = random.random()
            if res < p:
                break
        return cpt

    def move(self):
        # if posX - gravityX < 0 => don't go left else don't go right
        # if posY- gravityY < 0 => don't go downward else don't go upward
        forbiddenX = []
        forbiddenY = []

        stim = self.__X.get_stimulus

        if stim != Stimulus():
            if self.__posX < stim.get_gravity[0]:
                forbiddenX.append(-1)
            else:
                forbiddenX.append(1)

            if self.__posY < stim.get_gravity[1]:
                forbiddenY.append(-1)
            else:
                forbiddenY.append(1)

            if stim.get_name == "Repos":
                forbiddenX.append([-1, 1])
                forbiddenY.append([-1, 1])

        choice = [round(np.random.random()*2)-1, round(np.random.random()*2)-1]
        print(str(choice) + "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        if choice[0] not in forbiddenX:
            self.__posX = sorted([0, self.__posX+choice[0], 100])[1]  # todo remplacer 100 par taille réelle du canvas
        if choice[1] not in forbiddenY:
            self.__posY = sorted([0, self.__posY+choice[1], 100])[1]

        self.__energy -= 1


def weighted_choice(choices):
    """
    Function that chose one of the keys of the list in parameter function of its value
    Consists of a uniform random launch between 0 and the sum of values and summing values in decreasing order
        until it gets higher than the random launch
    :param choices:  a list of values keyed by things you need
    """
    total = sum(w for w in choices.values())
    r = random.uniform(0, total)
    upto = 0
    for c in choices.keys():
        upto += choices[c]
        if upto > r:
            return c, r
    return None  # if we get here, it's an error
