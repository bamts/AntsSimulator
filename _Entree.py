# coding=utf-8
# import itertools

# from Fourmis import Fourmi

from Parser import Configure

from Proc_iterations import work
import sys
import os

if '-c' in sys.argv:

    if os.path.exists(os.curdir+"\Fourmis"):
        for cur in os.listdir(os.curdir+"\Fourmis"):
            os.remove(os.curdir+"\Fourmis\\"+cur)

    if os.path.exists(os.curdir+"\Tests"):
        for cur in os.listdir(os.curdir+"\Tests"):
            os.remove(os.curdir+"\Tests\\"+cur)

    if os.path.exists(os.curdir+"\Resultats"):
        for dirs in os.listdir(os.curdir+"\Resultats"):
            for cur in os.listdir(os.curdir+"\Resultats\\"+dirs):
                os.remove(os.curdir+"\Resultats\\"+dirs+"\\"+cur)
        for dirs in os.listdir(os.curdir+"\Resultats"):
            os.removedirs(os.curdir+"\Resultats\\"+dirs)


dims_canvas = (100, 100)
"""
s1 = Stimulus("Faim", 0.5, (20, 20, 100, 100))
s2 = Stimulus("LarvesFaim", 0.5, (0, 20, 80, 100))
s3 = Stimulus("Predateur", 0.5, (20, 0, 100, 80))
s4 = Stimulus("Pluie", 0.5, (0, 0, 80, 80))
s1.set_func("UNIF")
# s2.set_func("UNIF")
# s3.set_func("UNIF")
# s4.set_func("UNIF")

s2.set_func("SIN")
s3.set_func("COSIN")
s4.set_func("SQRT")

liste_stimuli = [s1, s2, s3, s4]

t1 = Tache("Foraging", s1)

t2 = Tache("Nourrir les larves", s2)

t3 = Tache("Attaquer", s3)

t4 = Tache("Reparer le nid", s4)

t5 = Tache("Repos", Stimulus(), "fatigue")

liste_taches = [t1, t2, t3, t4, t5]

# On ajoute un type de fourmis : Major
tf1 = TypeFourmi("Major", dict(zip(liste_taches, [0.8, 0.8, 0.2, 0.2, int()])))

# On ajoute un type de fourmis : Minor, une autre manière de faire

tf2 = TypeFourmi("Minor")
tf2.add_tache_to_repertoire(t1, 0.5)
tf2.add_tache_to_repertoire(t2, 0.5)
tf2.add_tache_to_repertoire(t3, 0.8)
tf2.add_tache_to_repertoire(t4, 0.8)
tf2.add_tache_to_repertoire(t5, int())

liste_types = [tf1, tf2]

c1 = Colonie(tf2, 10, _pos=(50, 50))
c2 = Colonie(tf1, 5, tf2, 5)

liste_colonies = [c1, c2]
"""
"""
s1 = Stimulus("Nourriture", 0.5)
s2 = Stimulus("Test", 0.9)
liste_stimuli = [s1, s2]

t1 = Tache("Ravitaillement", [s1])
t2 = Tache("TestTache", [s2])
liste_taches = [t1, t2]

tf = TypeFourmi("Individuel", dict(zip(liste_taches, [0.5, 0.5])), _p=0.3)
liste_types = [tf]

c = Colonie(tf, 3)

liste_colonies = [c]

nbIterations = 100
deltaT = 3
"""
"""
n = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
ns = [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, int()]

liste_stimuli = [Stimulus(x, 0.5) for x in n]

liste_taches = []
for i in liste_stimuli:
    i.set_couverture((0, 0, 100, 100))
    liste_taches.append(Tache(i.get_name, i))

liste_taches.append(Tache("Repos", Stimulus(), "fatigue"))

liste_types = [TypeFourmi("Artiste", dict(zip(liste_taches, ns)), _p=0.6)]
liste_colonies = [Colonie(liste_types[0], 5)]

fic = work(liste_stimuli, liste_taches, liste_colonies, liste_types, 100, dims_canvas, False)
fic.close()

for f in os.listdir(os.curdir+"\Fourmis"):
    fic = open(os.curdir+"\Fourmis\\"+f, 'r')
    m = MusicGenerator.Music(f+".mid")

    m.give_input(fic)
    m.to_midi(1, 96)
"""
put = Configure("Experiments/ASim_Img_4S.conf")
put.parse()
fic = work(*put.initialize())
fic.close()

# todo http://sametmax.com/lencoding-en-python-une-bonne-fois-pour-toute/

