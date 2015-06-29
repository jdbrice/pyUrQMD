import os
import random
import sys


def writeInputfile( nEvents, energy, fname="inputfile" ):
	# Uses /dev/urandom - random enough for cryptographic uses
	r = random.SystemRandom()
	rndSeed = r.randint(0, sys.maxint)

	## A simple template for UrQMD input file
	template = """#Generated
pro 197 79
tar 197 79

nev {0}
imp -14

ecm {1}
tim 200 200

eos 0

rsd {2}

#f13
f14
f15
f16
f19
f20 

xxx"""
	 
	with open(fname, 'w') as ifile: 
		ifile.write( template.format( nEvents, energy, rndSeed ) )

if __name__ == "__main__":
	if len( sys.argv ) < 3 :
		print "Usage:\n", "urqmdInput.py nEvents comEnergy"
		exit()

	UrQMDInputFile( sys.argv[ 1 ], sys.argv[ 2 ] )