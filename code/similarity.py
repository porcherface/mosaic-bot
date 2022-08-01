#################################
# name: similarity.py
# author: porcherface

# a is the image matrix as numpy array 2d
# x is the picsel matrix as numpy array 2d

from classes.bucket import Bucket
from classes.target import Target

# NORMALIZATION = 1 / 255 / 255
NORMALIZATION = 1

def Similarity(A, x, size_x, size_y):
	out = 0
	index = 0
	for row in A:
		for item in row:
			out = out + (item - x[index])*(item - x[index])	
			index = index + 1

	print("performed "+str(index)+" summations")
	return out / size_x / size_y 


def Delta(A, x, idx, size_x, size_y):

	# first get i,j for A
	i0 = idx[0] % size_x
	j0 =int( (idx[0] - i0 ) / size_x)

	i1 = idx[1] % size_x
	j1 = int( (idx[1] - i1 ) / size_x)

	deltae =- (A[i0][j0] - x[idx[0]]) * (A[i0][j0] - x[idx[0]]) 
	deltae += (A[i0][j0] - x[idx[1]]) * (A[i0][j0] - x[idx[1]])

	if idx[1]< (size_x*size_y):
		deltae -= (A[i1][j1] - x[idx[1]]) * (A[i1][j1] - x[idx[1]]) 
		deltae += (A[i1][j1] - x[idx[0]]) * (A[i1][j1] - x[idx[0]])


	return deltae / size_x / size_y


if __name__ == "__main__":
	A = Target('/Users/saramilone/ricciobbello/mosaic-bot/images/original/download.jpeg',3,3)
	x = Bucket('/Users/saramilone/ricciobbello/mosaic-bot/images/edited', A.size)
	print(A.matrix)
	print(x.vector)
	S = Similarity(A.matrix,x.vector)
	
	print(S)
