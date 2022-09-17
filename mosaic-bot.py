###########################################################
#                                                         #
#  @name: mosaic-bot                                      #
#  @author: porcherface (github.com/porcherface)          #
#  @created:   Sep 6 2022                                 #
#  @descr:                                                #
#  @warn: this file uses tabs 4 indentation               #
#                                                         #
###########################################################


import os 
import sys
import argparse

sys.path.append(os.path.join(os.path.dirname(__file__), 'code'))

import annealing
from classes.generate import Generate


parser = argparse.ArgumentParser(description='Audio xray xrays audio',
                                    epilog='have fun! :)')

parser.add_argument("target",
					help="absolute or relative path to targetfile")
parser.add_argument("bucket",
					help="absolute or relative path to bucketdir")
parser.add_argument("-o", "--out", default="output.png",
					help="saves to file")
parser.add_argument("-c", "--config", 
					help="custom config file")
parser.add_argument("-v", "--version",action="store_true",
                    help="shows version")
parser.add_argument("-r", "--resize", default="30x30:30x30",
					help="set target:pixel sizes")
parser.add_argument("-s", "--skip", action = "store_true",
					help = "skips the preformatting of original pics. CARE: use this only if you already preformatted")

args = parser.parse_args()

if args.version:
	print("0.0.1")
	sys.exit(0)

targetsize = (args.resize.split(":")[0].split("x")[0], args.resize.split(":")[0].split("x")[1])
pixelsize  = (args.resize.split(":")[1].split("x")[0], args.resize.split(":")[1].split("x")[1])


########
########




#Annealing(targetpath, bucketpath, nrow, ncol, params = None )
(A, xmin) = annealing.Annealing(args.target, args.bucket, int(targetsize[0]), int(targetsize[1]))
g = Generate(args.out,A,xmin)
