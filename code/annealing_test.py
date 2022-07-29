##annealing.py

# this python script bruteforces swaps until N iterations are reached. best is saved and shown

from classes.bucket import Bucket
from classes.target import Target
from classes.generate import Generate
from similarity import Similarity
from random import random
from math import exp



if __name__ == "__main__":
	A = Target('/Users/saramilone/ricciobbello/mosaic-bot/images/targets/gradient.jpg',20,20)
	x = Bucket('/Users/saramilone/ricciobbello/mosaic-bot/images/fakes', A.size)

	Smin = Similarity(A.matrix,x.vector)
	s = Smin
	xmin = x

	t = 0
	TMAX = 1000000
	#TMAX = 1000
	beta = 0.0001
	beta_incr = 1.00001



	while t < TMAX :
		x1 = x.swap()
		s1 = Similarity(A.matrix,x1.vector)

		if t%(TMAX/100)==0:
			print(str(int(t/TMAX*100))+r"% complete (beta= "+str(beta)+",    s= "+str(s1)+",    smin= "+str(Smin)+")")
		

		# record best		
		if s1 < Smin:
			xmin = x1
			Smin = s1
		
		# accept swap 
		accept = False
		if s1 < s:
			accept = True
		# to avoid unnecessary exp calculations
		elif exp( - beta * (s1-s))> random():
			accept = True

		if accept == True:
			x = x1
			s = s1
		t = t + 1
		beta = beta*beta_incr

	print(Smin)
	print(x.cap)
	g = Generate('/Users/saramilone/ricciobbello/mosaic-bot/images/out_nonorm.png',A,xmin)
	print("size x: "+str(g.size_x))
	print("size y: "+str(g.size_y))
	print(A.matrix)
	print(x.vector)


