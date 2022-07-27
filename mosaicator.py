# mosaicator.py


# a toy model and brainstorming snippet

# we will surely need numpy

import numpy as np
import os
import glob

# x is the pixel bucket
x = []


# some useful methods would be

# this is more an anti similarity, 
# has out=0 for total equivalence and 
# out>0 for partial similarity

def Similarity(A, x):

	index = 0
	out = 0

	if (len(A) > len(x)):
		print("value has more elements than bucket")
		raise RuntimeError

	
	for i in A:
		for j in i:
			out = out + (j - x[index])*(j - x[index])	
			index = index + 1

	return out/index

'''
def deltaS(A, x, swapper, S):

	#out = out + nuovi - vecchi

	#vecchi 
	i = swapper[0] % len(A)
	j =  swapper[0] - i 

	if 
	vecchi = A[i][j]

'''


if __name__ == "__main__":

	print("Testing Similarity")

	a = np.zeros((50,50,1) )
	x = np.zeros(10000)
	y = np.ones(10000)
	z = 255*y 

	print("between zeros and zeros: "+str(Similarity(a, x) )) 
	print("between zeros and ones: "+str(Similarity(a, y) ))
	print("between black and white"+str(Similarity(a, z) ))


	





