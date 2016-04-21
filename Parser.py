from Colonies import Colonie
from TypesFourmis import TypeFourmi
from Stimuli import Stimulus
from Taches import Tache
from Proc_iterations import work

class Configure:

    def __init__(self, _filename):

        self.__filename = _filename
        self.__lines = None
        self.__curSection = None
        self.__parsed = {}

    def parse(self):

        file = open(self.__filename, "r")

        self.__lines = file.readlines()

        for line in self.__lines:

            if "[" in line:
                self.__curSection = line.split("[")[1].split("]")[0]
                self.__parsed[self.__curSection] = {}
            else:
                cur = line.split("=")
                self.__parsed[self.__curSection][cur[0]] = cur[1]

    def initialize(self):

        liste_stimuli = []
        liste_taches = []
        liste_types = []
        liste_colonies = []
        nbIt = 0
        dim = None
        music = False
        img = False

        result = self.__parsed

        for p in result.get("params"):
            if p == "img":
                img = (result["params"][p].strip() == "True")
            if p == "music":
                music = (result["params"][p].strip() == "True")
            if p == "dim":
                cur = result["params"][p].split(",")
                dim = (int(cur[0].strip()), int(cur[1].strip()))
            if p == "it":
                nbIt = int(result["params"][p].strip())

        for sti in result.get("stimuli"):
            tmp = result["stimuli"][sti].split(';')
            s = Stimulus(sti, 0.5, (int(tmp[0]), int(tmp[1]), int(tmp[2]), int(tmp[3])), (int(tmp[6].split(',')[0]),
                                                                                          int(tmp[6].split(',')[1])))
            s.set_func(tmp[4].strip())
            s.set_color(tmp[5])
            liste_stimuli.append(s)

        for tac in result.get("taches"):
            cur = Stimulus()
            tmp = result["taches"][tac].strip()
            for s in liste_stimuli:
                if s.get_name == tmp:
                    cur = s
            t = Tache(tac, cur)
            liste_taches.append(t)
        liste_taches.append(Tache("Repos", Stimulus(), "fatigue"))

        for typ in result.get("types"):
            tmp = result["types"][typ].split(',')
            tmpt = []
            tmplt = []
            for cur in tmp:
                tmpt.append(float(cur.split("-")[1].strip()))
                for tache in liste_taches:
                    if cur.split("-")[0] == tache:
                        tmplt.append(tache)

            ty = TypeFourmi(typ, dict(zip(tmplt, tmpt)))
            liste_types.append(ty)

        for col in result.get("colonies"):
            tmp = result["colonies"][col].split(';')
            tot = []

            for cur in tmp:
                typ, nb = cur.split(",")
                for t in liste_types:
                    if t.get_name == typ:
                        tot.append(t)
                tot.append(int(nb))

            liste_colonies.append(Colonie(*tot))

        return liste_stimuli, liste_taches, liste_colonies, liste_types, nbIt, dim, img, music

    def create(self):
        pass




