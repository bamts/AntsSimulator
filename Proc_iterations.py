# coding: utf8

"""
Proc_iterations.py - Module containing work, the main routine of the program
import:
-------
time, for file naming
ALL AntsSimulator classes
imported by:
-------------
_Entree
"""

import os
from time import *
from Fourmis import Fourmi
from Colonies import Colonie
from Stimuli import Stimulus
from Taches import Tache
from TypesFourmis import TypeFourmi
from Plots import PlotXFourmis
from Plots import PlotStimFunc
from ImageGenerator import CreateImage
import matplotlib.pyplot as plt

# For later use : from textwrap import *

fileName = ""
lines = ["{}/{}/{}_{}:{}".format(strftime('%d'), strftime('%m'), strftime('%Y'), strftime('%H'), strftime('%M'))]


def work(sti, tac, col, typ, nb, dim, image, music):
    directory = os.getcwd() + "\Resultats"
    sub_directory = directory + "\\s" + str(len(sti)) + "t" + str(len(tac)) + "c" + str(len(col)) + "t"
    global fileName
    fileName = sub_directory + '\\' + str(nb) + "_iterations"
    cpt = 0

    if not os.path.exists(directory):
        os.makedirs(directory)
    if not os.path.exists(sub_directory):
        os.makedirs(sub_directory)

    base_filename = fileName
    while os.path.isfile(fileName + ".txt"):
        cpt += 1
        fileName = base_filename + str(cpt)

    sortie = open(fileName + ".txt", 'a')

    img = None

    if image:
        img = CreateImage()

    lines.append("---------------------")
    lines.append("INITIALISATION")
    lines.append("---------------------")
    lines.append("---------------------")

    lines.append("liste des stimuli initiaux : ")

    for s in sti:
        lines.append("\t"+str(s))
        s.prepare_func(nb)
        if image:
            img.write_stimulus(s)
    if image:
        img.show()
    PlotStimFunc(sti, None)

    lines.append("---------------------")
    lines.append("Liste des taches existantes :")
    for t in tac:
        lines.append(str(t))
    lines.append("---------------------")

    lines.append("Liste des repertoires initiaux par type de fourmi :")

    for tf in typ:
        lines.append(str(tf))

    lines.append("---------------------")

    lines.append("Liste des colonies : ")

    for c in col:
        lines.append(str(c))
        lines.append("---------------------")

        liste = c.get_fourmis
        for f in liste:
            lines.append(str(f))
        lines.append("---------------------")

    lines.append("---------------------")
    lines.append("DEBUT DES ITERATIONS")
    lines.append("---------------------")

    liste_stimuli = sti
    if nb != 0:
        for i in range(nb):
            lines.append("IT{}".format(i))
            lines.append("---------------------")
            for s in liste_stimuli:
                lines.append(str(s))
                s.compute_stimulus(i)

            lines.append("---------------------")
            for c in col:
                lines.append("---------------------")
                if image:
                    img.write_ants(c.get_fourmis, c.get_id)
                for f in c.get_fourmis:
                    lines.append(str(f))
                    if not f.is_busy:
                        choix = f.selection(liste_stimuli, nb)
                        tache = choix[0]
                        decision = choix[1]
                        parmi = {}
                        for x in choix[2]:
                            parmi[x.get_name] = choix[2].get(x)

                        lines.append("choix:{}\n\tdecision:{}|{}".format(f.get_id, tache.get_name, decision, parmi))
                    else:
                        lines.append("travaille:{}\n\tencore:{} iterations".format(f.get_x.get_name, f.get_busy))
                        f.dec_busy()
                        f.inc_tiredness()
                        if image:
                            f.move()

                        for s in liste_stimuli:
                            if s == f.get_x.get_stimulus:
                                s.dec_intensite()

                    f.update_theta()
            for s in liste_stimuli:
                s.push_altered(s.get_intensite, i)
            lines.append("---------------------")
        if image:
            img.show()
    else:
        pass  # todo infinite loop

    lines.append("---------------------")
    lines.append("FIN")

    towrite = "\n".join(lines)
    sortie.writelines(towrite)

    cptPlot = 0
    for c in col:
        for f in c.get_fourmis:
            cptPlot += 1
            cur = open('Fourmis/fourmi{}'.format(f.get_id), 'a')
            for mem in f.get_full_mem:
                cur.writelines(str(mem))
                cur.writelines('\n')
            cur.close()

    PlotStimFunc(sti, [s.get_altered for s in sti], cptPlot, len(tac), nb)

    return sortie


if __name__ == '__main__':
    work([Stimulus()], [Tache()], [Colonie()], [TypeFourmi()], 0, 2)
    print("Fichier : " + fileName + " cree")
