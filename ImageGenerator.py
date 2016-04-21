import numpy
import matplotlib.pyplot as plt
from time import *

fileName = "Image{}{}{}_{}{}{}".format(strftime('%d'), strftime('%m'),
                                       strftime('%Y'), strftime('%H'),
                                       strftime('%M'), strftime('%S'))


class CreateImage:
    cpt = 0

    def __init__(self, _dimms=(101, 101)):
        self.__dimmentions = _dimms
        self.res = numpy.zeros(self.__dimmentions)

    def write_ants(self, _ants, _col):
        for f in _ants:
            print(f.get_coords)  # for DEBUG
            if f.get_x:
                if f.get_x.get_name != "TACHEDEFAUT":
                    self.res[f.get_coords[0], f.get_coords[
                        1]] = f.get_x.get_stimulus.get_id  # todo Utiliser couleur du stimulus
            else:
                self.res[f.get_coords[0], f.get_coords[1]] = _col

    def write_stimulus(self, _stimulus):
        g = _stimulus.get_gravity
        couv = _stimulus.get_couverture
        color = _stimulus.get_id

        for i in range(couv[0], couv[2]):
            self.res[i, couv[1]] = color  # = ________________
            self.res[i, couv[3]] = color  # = ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯
        for j in range(couv[1], couv[3]):
            self.res[couv[0], j] = color  # = | ----
            self.res[couv[2], j] = color  # = ---- |

        self.res[g] = color

    def show(self):
        CreateImage.cpt += 1
        # f = open("test{}".format(CreateImage.cpt),'w')
        # f.write(str(self.res))
        plt.imshow(self.res)
        plt.savefig("test{}.jpg".format(CreateImage.cpt))


if __name__ == '__main__':
    im = CreateImage()
    plt.imshow(im.show())  # Needs to be in row,col order

    plt.savefig('test.jpg')
