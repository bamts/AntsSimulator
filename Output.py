from textwrap import TextWrapper as wrap
import numpy
import matplotlib.pyplot as plt

class Records:

    def __init__(self, _type):
        self.__type = _type
        self.__datas = []

    def add_datas(self, _args):
        self.__datas.append(_args)

    def trim(self):
        if self.__type == "f":
            pass


class Writter:

    def __init__(self, _to, _buffer=None):
        self.__output = _to
        self.__buffer = _buffer
        open(self.__output, 'a')

    def __del__(self):
        self.__output.close()
        self.__buffer.clear()

    def set_buffer(self, _buffer):
        self.__buffer = _buffer

    def send(self):
        while self.__buffer is not None:
            self.__output.write(self.__buffer)


class Plotter:

    def __init__(self, _line=None):
        self.__lines = [_line]
        self.__writter = Writter('tmp', self.__lines)

    def append(self, _line):
        self.__lines.append(_line)

    def do(self):

        stop = False
        while not stop:
            pass

res = numpy.zeros((2, 2))
# res[0][0] = 5
# res[1][1] = 6cpt = 0
# for i in range(h):
#     for j in range(w):
#         data[i][j] = cpt
#         cpt += 1

from PIL import Image
import numpy as np

w, h = 100, 100
data = np.zeros((h, w, 3), dtype=np.uint8)
cpt = 0
for i in range(h):
    for j in range(w):
        data[i, j] = [255,255,255]
for i in range(h):
    for j in range(w):
        data[i, j] = [150 + cpt, 0, 0]
    cpt += 10
img = Image.fromarray(data, 'RGB')
img.save('my.png')
