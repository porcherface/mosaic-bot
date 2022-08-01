#################################
# name: target.py
# author: porcherface

from PIL import Image
import numpy

class Target:

	def __init__(self, filename=None, res_x = 50, res_y = 50):
		self.image = Image.open(filename)
		self.res_x = res_x
		self.res_y = res_y
		self.size = res_y*res_x
		self.resized = 	self.image.resize((res_x,res_y))
		self.matrix = numpy.asarray(self.resized.convert('L'))
	
	def get_variance_matrix(self):
		pass




	def show(self):
		self.image.show()
		self.resized.show()

if __name__ == "__main__":

	t = Target('/Users/saramilone/ricciobbello/mosaic-bot/images/original/download.jpeg')
	#t.show()
	print(t.matrix)