import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# x = [v for v in range(10000)]
# y = [np.random.random()*(np.random.random()) for v in x]
#
# plt.plot(x, y)
# print(x, y, sep="\n")
#
# plt.show()

def PlotXFourmis(_nbTaches=0, _nbFourmis=0, _time=0):

    files = []
    for f in range(_nbFourmis):
        files.append(open("Fourmis/fourmi{}".format(f+1), 'r'))

    cpt = 0
    names = {}
    for file in files:
        cpt += 1
        y = []
        for line in file.readlines():
            for x in range(int(line.split(',')[2].strip(')\n'))):
                val = int(line.split(',')[0].strip('('))
                y.append(val)
                names[val] = (line.split('\'')[1])

        plt.subplot(_nbFourmis+1, 1, cpt)
        plt.axis([0, _time, 0, _nbTaches + 2])
        plt.ylabel("fourmi{}      ".format(cpt), rotation="horizontal", horizontalalignment="right")
        _c = "blue"
        if cpt > 4:
            _c = "red"
        plt.plot(range(len(y)), y, "o", color=_c)

        plt.grid()
        file.close()
    patchs = []
    for n in names:
        patchs.append(mpatches.Patch(label="{}:{}".format(n, str(names.get(n)))))
    plt.legend(handles=patchs)
    plt.show()


def PlotStimFunc(liste_stimulus, altered, cptPlot=None, lentac=None, nb=None):
    if not altered:
        cpt = 0
        for s in liste_stimulus:
            if s.get_func:
                cpt += 1
                y = s.get_prepared_values

                plt.subplot(len(liste_stimulus)+1, 1, cpt)
                plt.ylabel(s.get_name, rotation="horizontal", horizontalalignment="right")

                plt.plot(range(len(y)), y)

                plt.grid()
        plt.show()
    else:
        cpt = 0
        for s in liste_stimulus:
            if s.get_func:
                y = s.get_prepared_values
                z = altered[cpt]
                cpt += 1

                plt.subplot(len(liste_stimulus)+1, 1, cpt)
                plt.ylabel(s.get_name, rotation="horizontal", horizontalalignment="right")

                plt.plot(range(len(y)), y)

                plt.plot(range(len(z)), z, 'r')
                plt.grid()

        plt.figure()
        PlotXFourmis(lentac, cptPlot, nb)

        plt.show()

