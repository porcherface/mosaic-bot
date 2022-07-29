#################################
# name: generate.py
# author: porcherface

from .bucket import Bucket
from .target import Target
from PIL import Image
class Generate:
	def __init__(self, output=None, targ=None, buck=None):
		self.target = targ
		self.bucket = buck

		self.size_x = targ.res_x * buck.get_size()[0]
		self.size_y = targ.res_y * buck.get_size()[1]

		self.out = Image.new(mode="L", size=(self.size_x, self.size_y))

		counter = 0
		pos_x = 0
		pos_y = 0

		for pic in self.bucket.picsel_list[0:self.bucket.cap]: 
			self.out.paste(pic.get_image(), (pos_x, pos_y))
			counter += 1
			
			pos_y+=buck.get_size()[1]
			if pos_y>=self.size_y:
				pos_y = 0
				pos_x += buck.get_size()[0]
	
		self.out.save(output)

if __name__ == "__main__":
	t = Target('/Users/saramilone/ricciobbello/mosaic-bot/images/original/download.jpeg')
	b = Bucket('/Users/saramilone/ricciobbello/mosaic-bot/images/edited')

	g = Generate("collage.png",t , b)

	print("size x: "+str(g.size_x))
	print("size y: "+str(g.size_y))