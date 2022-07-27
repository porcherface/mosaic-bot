#################################
# name: generate.py
# author: porcherface

from .bucket import Bucket
from .target import Target

class Generate:
	def __init__(self, output=None, targ=None, buck=None):
		self.target = targ
		self.bucket = buck

if __name__ == "__main__":
	t = Target('/Users/saramilone/ricciobbello/mosaic-bot/images/original/download.jpeg')
	b = Bucket('/Users/saramilone/ricciobbello/mosaic-bot/images/edited')

	g = Generate("collage.png",t , b)