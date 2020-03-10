import random
from matplotlib import pyplot
from chiper import Chiper
from mode_operation import ModeOperation
import numpy

cipher = Chiper(b"1234567890abcdef")
operation = ModeOperation(cipher, ModeOperation.MODE_ECB)

pt2 = open("test/test12kb", "rb").read()
c = operation.encrypt(pt2)

bins = numpy.linspace(0, 256, 200)

pyplot.hist(bytearray(pt2), bins, alpha=0.5, label='plaintext')
pyplot.hist(bytearray(c), bins, alpha=0.5, label='ciphertext')
pyplot.legend(loc='upper right')
pyplot.show()
