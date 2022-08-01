#################################
# name: bucket.py
# author: porcherface
import numpy
from .picsel import Picsel
import glob
from random import randrange
from copy import deepcopy, copy

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

	def propose(self):
		#out = deepcopy(self)
		#out = self
		#out = copy(self)

		self.i1 = randrange(self.cap)                    
		self.i2 = randrange(self. count)
	

	def swap(self):
		v1 = self.picsel_list[self.i1]
		v2 = self.picsel_list[self.i2]
		self.picsel_list[self.i1] = v2
		self.picsel_list[self.i2] = v1
		v1 = self.vector[self.i1]
		v2 = self.vector[self.i2]
		self.vector[self.i1] = v2
		self.vector[self.i2] = v1


	def get_size(self):
		self.size = self.picsel_list[0].get_size()
		return self.size

'''	def to_matrix(self):
		self.matrix = numpy.array(
'''

if __name__ == "__main__":

	b = Bucket('/Users/saramilone/ricciobbello/mosaic-bot/images/edited',3)
	
	print(b.picsel_list)
	print(b.count)
	print(b.vector)

	b1= b.swap()
	
	print(b.picsel_list)
	print(b.count)
	print(b.vector)

	print(b1.picsel_list)
	print(b1.count)
	print(b1.vector)