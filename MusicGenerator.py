import re

names = ["A", "B", "C", "D", "E", "F", "G"]

#  todo http://somascape.org/midi/tech/mfile.html

def nameToNote(_name="C", _level=4):
    """
    :param _level: highness of the note
    :param _name: name of the note
    :return: the midi code coresponding to the note
    """
    use = _name
    if use == "Repos":
        use = "C"

    notes = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
    return 12*(_level+1)+notes.index(use)


class Music:
    """
        Class containing a method to write midi files from strings input
    """
    def __init__(self, _nomFic="test"):
        self.__track = None
        self.__name = _nomFic

    def give_input(self, _input):
        table = _input.readlines()
        cur = ""
        for line in table:
            if "Repos" not in line.split(',')[1]:
                cur += line.split(',')[1].split('\'')[1] + "-"
        self.__track = cur[:-1]

    def to_midi(self, _nbt, _PPQ):
#=int(input("Combien de pistes ?\n"))
#=int(input("Tempo ?\n"))
        filetest = open(self.__name, "wb")
        header = ["\x4d", "\x54", "\x68", "\x64", "\x00", "\x00", "\x00", "\x06", "\x00", "\x01"]
        for x in header:
            filetest.write(bytes((ord(x),)))

        nbtracks = _nbt
        PPQ = _PPQ
        tempPTick = 60000 / (90 * PPQ)

        filetest.write(nbtracks.to_bytes(2, byteorder='big'))
        filetest.write(PPQ.to_bytes(2, byteorder='big'))

        stringtracks = self.__track

        if stringtracks is None:
            for i in range(nbtracks):
                stringtracks.append(input("Vous allez maintenant ecrire des pistes simples (A=La,B=Si,C=Do,D=Re,E=Mi,F=Fa,G=Sol) avec des '-'\
             entre chaque \n note et des '.' pour un octave en dessous des '+' pour un au dessus\n"))

        for i in range(nbtracks):
            MTrk = ["\x4d", "\x54", "\x72", "\x6b"]
            for y in MTrk:
                filetest.write(bytes((ord(y),)))

            # sizeoftrack = nombre de lettres
            sizeoftrack = len(self.__track.split('-'))
            filetest.write((sizeoftrack*4*2+4).to_bytes(4, byteorder='big'))

            for piece in stringtracks.split('-'):
                tempLevel = 4
                tempTimeStamp = 16*tempPTick
                cptTmpBlk = int(tempPTick)
                tempCanal = 144+i+1
                note = piece.strip("!,.+:")

                tempTimeStamp *= max(1, 2*piece.count('!'))
                tempTimeStamp /= max(1, 2*piece.count(','))

                tempCanal += i-1

                tempLevel -= piece.count('.')
                tempLevel += piece.count('+')

                cptTmpBlk += piece.count(':')
                filetest.write(int(tempTimeStamp).to_bytes(1, byteorder='big'))
                filetest.write(tempCanal.to_bytes(1, byteorder='big'))

                temp = nameToNote(note, tempLevel)

                filetest.write(temp.to_bytes(1, byteorder='big'))
                filetest.write(0x60.to_bytes(1, byteorder='big'))

                if cptTmpBlk > 4:
                    filetest.write(0x81.to_bytes(1, byteorder='big'))
                    filetest.write(((cptTmpBlk*0x1f) % 0x81).to_bytes(1, byteorder='big'))

                else:
                    filetest.write((cptTmpBlk*0x1f).to_bytes(1, byteorder='big'))
                    filetest.write((tempCanal-16).to_bytes(1, byteorder='big'))

                filetest.write(temp.to_bytes(1, byteorder='big'))
                filetest.write(0x00.to_bytes(1, byteorder='big'))

            End = ["\x00", "\xff", "\x2f", "\x00"]
            for z in End:
                filetest.write(bytes((ord(z),)))

        filetest.close()



