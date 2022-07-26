## bruteforcer.py

# this python script bruteforces swaps until N iterations are reached. best is saved and shown

from classes.bucket import Bucket
from classes.target import Target
from classes.generate import Generate
from similarity import Similarity


if __name__ == "__main__":
	A = Target('/Users/saramilone/ricciobbello/mosaic-bot/images/original/download.jpeg',3,3)
	x = Bucket('/Users/saramilone/ricciobbello/mosaic-bot/images/edited', A.size)

	Smin = Similarity(A.matrix,x.vector)
	xmin = x

	t = 0
	TMAX = 1000000
	while t < TMAX :
		x = x.swap()
		s = Similarity(A.matrix,x.vector)

		if t%(TMAX/100)==0:
			print(str(int(t/TMAX*100))+r"% complete")
			
		if s < Smin:
			xmin = x
			Smin = s
			print("found a better one")
		t = t + 1

	print(Smin)

	g = Generate('/Users/saramilone/ricciobbello/mosaic-bot/images/out.png',A,x)