#!/usr/bin/env python
import pyUrQMD.project as urqmd
import sys

print "Usage:\n", "qsub.py project_name"

eventsPerJob = 100

if len( sys.argv ) >= 2 :
	name = sys.argv[ 1 ]
else :
	exit()

urqmd.qsubProject( name )
