#!/usr/bin/env python
import pyUrQMD.UrQMD_to_STARSIM_Event_Record as utoer
import argparse
import os

parser = argparse.ArgumentParser( description="Converts a UrQMD standard output (f13 or f14) into the (new) STAR TX format. Can convert all files in a directory if a directory path is given. Otherwise the given file is converted and written to stdout" );
parser.add_argument( "input", help="Input filename or directory containing UrQMD standard output files" )
parser.add_argument("-split", help="Splits into N events per file with the output file having the input filename + .tx suffix" )
parser.add_argument("-vX", help="vX distribution center", default=0.0 )
parser.add_argument("-vY", help="vY distribution center", default=0.0 )
parser.add_argument("-sig_vX", help="sig_vX for generating Vx distribution", default=0.1 )
parser.add_argument("-sig_vY", help="sig_vY for generating Vy distribution", default=0.1 )
parser.add_argument("-z_min", help="z_min for generating Vz distribution, generates a uniform vZ from z_min to z_max", default=0-30.0 )
parser.add_argument("-z_max", help="z_max for generating Vz distribution", default=30.0 )

args = parser.parse_args();

print "Generating Vertex Distribution for each event"
print "\tVxy center at = (", args.vX, ",", args.vY, ")"
print "\tVxy sigma = (", args.sig_vX, ",", args.sig_vY, ")"
print "\tVz distribution (", args.z_min, ",", args.z_max, ")"

if os.path.isfile( args.input ) and ( args.input.endswith( ".f13" ) or args.input.endswith( ".f14" )  ):
	utoer.convert( args.input, args.split )
	exit()
elif os.path.isdir( args.input ) :
	for dirName, subdirList, fileList in os.walk(args.input):
		for f in fileList :
			if f.endswith( ".f13" ) or f.endswith( ".f14" ) :
				utoer.convert( os.path.join( dirName, f), args.split );
	exit()

print "Invalid input"
print "Must be a .f13 or .f14 file or a directory containing them"

	