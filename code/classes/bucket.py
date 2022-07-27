#################################
# name: bucket.py
# author: porcherface
from picsel import Picsel
import glob

class Bucket:

	def __init__(self, path=None):
		
		self.picsel_list = []
		self.count = 0
		for image in glob.glob(path+"/*.png"):
			self.picsel_list.append(Picsel(image))
			self.count += 1


if __name__ == "__main__":

	b = Bucket('/Users/saramilone/ricciobbello/mosaic-bot/images/edited')
	
	print(b.picsel_list)
	print(b.count)