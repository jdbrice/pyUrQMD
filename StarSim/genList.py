#!/usr/bin/env python

import argparse
parser = argparse.ArgumentParser( description="generates a list with each line 'string:i' -  (a to b) inclusive" );
parser.add_argument( "a", help="first value" )
parser.add_argument( "b", help="last value" )

args = parser.parse_args();

with open( 'current.list', 'w' ) as f :
	for i in range( int(args.a), int(args.b) + 1 ) :
	    f.write( "string:{0}\n".format( i ) )