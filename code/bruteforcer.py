## bruteforcer.py

# this python script bruteforces swaps until N iterations are reached. best is saved and shown

from classes.bucket import Bucket
from classes.target import Target
from similarity import Similarity


if __name__ == "__main__":
	A = Target('/Users/saramilone/ricciobbello/mosaic-bot/images/original/download.jpeg',3,3)
	x = Bucket('/Users/saramilone/ricciobbello/mosaic-bot/images/edited', A.size)

	S = Similarity(A.matrix,x.vector)
	
	print(S)
