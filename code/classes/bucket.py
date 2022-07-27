#################################
# name: bucket.py
# author: porcherface
import numpy
from .picsel import Picsel
import glob
from random import randrange

class Bucket:

	def __init__(self, path=None, cap = None):
		
		self.picsel_list = []
		self.vector = []
		self.count = 0
		self.cap = cap
		for image in glob.glob(path+"/*.png"):
			self.picsel_list.append(Picsel(image))
			self.count += 1
			self.vector.append(self.picsel_list[-1].pixel)
		self.vector = numpy.asarray(self.vector)
		if cap == None:
			self.cap = self.count

	def swap(self):
		out = self

		i1 = randrange(self.count)                    
		i2 = randrange(self. cap)

		v1 = self.picsel_list[i1]
		v2 = self.picsel_list[i2]
		out.picsel_list[i1] = v2
		out.picsel_list[i2] = v1
		v1 = self.vector[i1]
		v2 = self.vector[i2]
		out.vector[i1] = v2
		out.vector[i2] = v1

		return out


if __name__ == "__main__":

	b = Bucket('/Users/saramilone/ricciobbello/mosaic-bot/images/edited')
	
	print(b.picsel_list)
	print(b.count)
	print(b.vector)
	b1= b.swap()
	print(b1.picsel_list)
	print(b1.count)
	print(b1.vector)