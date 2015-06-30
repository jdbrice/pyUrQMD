#!/usr/bin/env python
import pyUrQMD.UrQMD_to_STARSIM_Event_Record as utoer
import sys

if len( sys.argv ) >= 2 :
	utoer.convert( sys.argv[1] )
else :
	print "Usage:\nconvert.py input_name > output_name"