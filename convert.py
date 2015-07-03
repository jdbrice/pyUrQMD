#!/usr/bin/env python
import pyUrQMD.UrQMD_to_STARSIM_Event_Record as utoer
import argparse
import os

parser = argparse.ArgumentParser( description="Converts a UrQMD standard output (f13 or f14) into the (new) STAR TX format. Can convert all files in a directory if a directory path is given. Otherwise the given file is converted and written to stdout" );
parser.add_argument( "input", help="Input filename or directory containing UrQMD standard output files" )
parser.add_argument("--split", help="Saves output for each input file to an output file with the same name + .tx suffix" )

args = parser.parse_args();


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

	