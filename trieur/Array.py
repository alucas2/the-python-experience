import pygame as pyg

SCR_W = 1024
SCR_H = 600
FRAMERATE = 60
FENETRE = pyg.display.set_mode((SCR_W, SCR_H))
KHRONO = pyg.time.Clock()
FONT = pyg.font.SysFont("Arial", 20)
PLAYER = pyg.midi.Output(0)
PLAYER.set_instrument(5)
NOTE_MIN = 21
NOTE_MAX = 109

COLOR_BG = (0, 0, 0)
COLOR_BAR = (255, 255, 255)
COLOR_HIGHLIGHT = (255, 0, 0)

def mapValue(val, min1, max1, min2, max2):
    n = (val - min1)/(max1 - min1)
    return n*(max2 - min2) + min2

class ArrayElement:
    def __init__(self, value, array):
        self._value = value
        self._array = array

    def getValue(self):
        self._array._draw()
        return self._value

    def __eq__(self, other):
        self._array._draw()
        return self._value == other._value

    def __lt__(self, other):
        self._array._draw()
        return self._value < other._value

    def __gt__(self, other):
        self._array._draw()
        return self._value > other._value

    def __ne__(self, other):
        return not self == other

    def __le__(self, other):
        return not self > other

    def __ge__(self, other):
        return not self < other


class Array:
    def __init__(self, iterable):
        global SCR_W, SCR_H, FENETRE
        self.max = max(iterable)
        self.size = len(iterable)
        SCR_H = 600
        SCR_W = self.size
        while SCR_W <= 1920: SCR_W *= 2
        while SCR_W > 1920: SCR_W //= 2
        FENETRE = pyg.display.set_mode((SCR_W, SCR_H))
        self.drawRate = 0
        self.drawCount = self.drawRate
        self.highlight = set()
        self.mustQuit = False
        self.array = [ArrayElement(i, self) for i in iterable]
        self.note = 0

    #renvoie un élément: cette opération ne coûte rien
    def __getitem__(self, i):
        self.highlight.add(i)
        return self.array[i]

    #assigne un valeur à un élément
    def __setitem__(self, i, element):
        self.highlight.add(i)
        self.array[i] = element
        self._draw()

    #échange deux éléments et affiche
    def swap(self, i, j):
        self.highlight.add(i)
        self.highlight.add(j)
        tmp = self.array[i]
        self.array[i] = self.array[j]
        self.array[j] = tmp
        self._draw()

    #affiche
    def _draw(self):
        if self.drawCount == 0 and not self.mustQuit:
            KHRONO.tick_busy_loop(FRAMERATE)
            for e in pyg.event.get():
                if e.type == pyg.QUIT: self.mustQuit = True
            FENETRE.fill(COLOR_BG)
            w = SCR_W / self.size
            h = SCR_H / self.max
            m = self.max
            for i in range(self.size):
                v = self.array[i]._value
                pyg.draw.rect(FENETRE, COLOR_BAR, (i*w, (m-v)*h, w, v*h))
            for i in self.highlight:
                v = self.array[i]._value
                pyg.draw.rect(FENETRE, COLOR_HIGHLIGHT, (i*w, (m-v)*h, w, v*h))
            pyg.display.flip()
            self.drawCount = self.drawRate
            val = self.array[self.highlight.pop()]._value
            PLAYER.note_off(self.note, 127)
            self.note = int(mapValue(val, 0, self.size, NOTE_MIN, NOTE_MAX))
            PLAYER.note_on(self.note, 127)

        else:
            self.drawCount -= 1
        self.highlight.clear()
