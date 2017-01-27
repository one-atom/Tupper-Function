# coding: utf-8
import sys
import os
from PIL import Image
import numpy
from pylab import *

filename = sys.argv[1]
print filename
im = numpy.array(Image.open(filename).convert('L'),'f')
im = numpy.array(im < 122.5,dtype=int)
height, width = im.shape[0], im.shape[1]
#print height, width

a = []
for i in xrange(0, width):
	for j in xrange(0, height):
		a.append(im[height - 1 - j, i])
bi = eval('0b'+"".join(map(lambda x: str(x), a)))
n = bi * height

command = "n = %d;\n ArrayPlot[Table[Boole[1/2 < Floor[Mod[Floor[y/%d] 2^(-%d Floor[x] - Mod[Floor[y], %d]), 2]]], {y, n, n + %d}, {x, %d, -2, -1}], PixelConstrained -> True, Frame -> False, ImageSize -> 500, PlotRange -> {All, All}]" % (n, height, height, height, height - 1, width - 1)
print command

