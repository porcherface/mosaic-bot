#################################
# name: similarity.py
# author: porcherface

# a is the image matrix as numpy array 2d
# x is the picsel matrix as numpy array 2d

from classes.bucket import Bucket
from classes.target import Target


def Similarity(A, x):
	out = 0
	index = 0
	for row in A:
		for item in row:
			out = out + (item - x[index])*(item - x[index])	
			index = index + 1

	return out / index


if __name__ == "__main__":
	A = Target('/Users/saramilone/ricciobbello/mosaic-bot/images/original/download.jpeg',3,3)
	x = Bucket('/Users/saramilone/ricciobbello/mosaic-bot/images/edited', A.size)

	S = Similarity(A.matrix,x.vector)
	
	print(S)
