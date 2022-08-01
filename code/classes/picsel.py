#################################
# name: picsel.py
# author: porcherface


from PIL import Image
class Picsel:

	def __init__(self, filename = None):
		if filename == None:
			self.name = ""
			self.index = -1
			self.pixel = -1
			self.variance = -1
			return

		self.name = filename.split("/")[-1]
		self.filename = filename
		splitted = self.name.split("_")
		
		self.index = int(splitted[0])
		self.pixel = int(splitted[1])
		self.variance = int(splitted[2])

	def get_size(self):
		self.size = Image.open(self.filename).size

		self.res_x = self.size[0]
		self.res_y = self.size[1]

		return self.size

	def get_image(self):
		return Image.open(self.filename)
		
if __name__ == "__main__":

	p = Picsel()
	print(p.name)
	print(p.index)
	print(p.pixel)
	
	p = Picsel("/Users/saramilone/ricciobbello/mosaic-bot/images/edited/000_116_.png")
	print(p.name)
	print(p.index)
	print(p.pixel)
	p.get_size()
	print(p.res_x)
	print(p.res_y)