#################################
# name: picsel.py
# author: porcherface

class Picsel:

	def __init__(self, filename = None):
		if filename == None:
			self.name = ""
			self.index = -1
			self.pixel = -1
			return

		self.name = filename.split("/")[-1]
		splitted = self.name.split("_")
		
		self.index = int(splitted[0])
		self.pixel = int(splitted[1])



if __name__ == "__main__":

	p = Picsel()
	print(p.name)
	print(p.index)
	print(p.pixel)
	
	p = Picsel("000_116_.png")
	print(p.name)
	print(p.index)
	print(p.pixel)
	