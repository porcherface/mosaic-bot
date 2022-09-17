##annealing.py

# this python script bruteforces swaps until N iterations are reached. best is saved and shown

from classes.bucket import Bucket
from classes.target import Target
from classes.generate import Generate
from similarity import Similarity, Delta
from random import random
from math import exp

def Annealing(targetpath, bucketpath, nrow, ncol, params = None ): 
	t = 0	
	if params == None:
		TMAX = 50000000
		#TMAX = 1000
		beta = 0.0001
		beta_incr = 1.000001
	else:
		TMAX = params.TMAX
		beta = params.beta
		beta_incr = params.beta_incr


	A = Target(targetpath,nrow,ncol)
	x = Bucket(bucketpath, A.size)

	Smin = Similarity(A.matrix,x.vector, nrow, ncol)
	s = Smin
	xmin = x

	while t < TMAX :
		x.propose()

		indexes = (x.i1, x.i2)

		#for now this works only with nrow = ncol, easy to implement the more general tho


		deltas = Delta(A.matrix,x.vector, indexes, nrow, ncol)

		s1 = s+deltas

		if t%(TMAX/100)==0:
			print(str(int(t/TMAX*100))+r"% complete (beta= "+str(beta)+",    deltas= "+str(deltas)+",    smin= "+str(Smin)+")")
		

		# record best		
		if s1 < Smin:
			xmin = x
			Smin = s1
		
		# accept swap 
		accept = False
		if s1 < s:
			accept = True
		# to avoid unnecessary exp calculations
		elif exp( - beta * deltas)> random():
			accept = True

		if accept == True:
			s = s1
			x.swap()

		t = t + 1
		beta = beta*beta_incr

	return (A, xmin)




if __name__ == "__main__":

	nrow = 33
	ncol = 33


	A = Target('/Users/saramilone/ricciobbello/mosaic-bot/images/targets/drow_portrait.jpeg',nrow,ncol)
	x = Bucket('/Users/saramilone/ricciobbello/mosaic-bot/images/drow_ranger_edit', A.size)

	Smin = Similarity(A.matrix,x.vector, nrow, ncol)
	s = Smin
	xmin = x

	t = 0
	TMAX = 1000000000
	#TMAX = 1000
	beta = 0.00005
	beta_incr = 1.00000001



	while t < TMAX :
		x.propose()

		indexes = (x.i1, x.i2)

		#for now this works only with nrow = ncol, easy to implement the more general tho


		deltas = Delta(A.matrix,x.vector, indexes, nrow, ncol)

		s1 = s+deltas

		if t%(TMAX/100)==0:
			print(str(int(t/TMAX*100))+r"% complete (beta= "+str(beta)+",    deltas= "+str(deltas)+",    smin= "+str(Smin)+")")
		

		# record best		
		if s1 < Smin:
			xmin = x
			Smin = s1
		
		# accept swap 
		accept = False
		if s1 < s:
			accept = True
		# to avoid unnecessary exp calculations
		elif exp( - beta * deltas)> random():
			accept = True

		if accept == True:
			s = s1
			x.swap()

		t = t + 1
		beta = beta*beta_incr

	print(Smin)
	print(x.cap)
	g = Generate('/Users/saramilone/ricciobbello/mosaic-bot/images/out_nonorm.png',A,xmin)
	print("size x: "+str(g.size_x))
	print("size y: "+str(g.size_y))
	print(A.matrix)
	print(x.vector)


