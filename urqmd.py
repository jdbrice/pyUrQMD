#!/usr/bin/env python
import pyUrQMD.project as urqmd
import sys

print "Usage:\n", "urqmd project_name comEnergy totalEvents eventsPerJob"

eventsPerJob = 100

if len( sys.argv ) == 4 :
	name = sys.argv[ 1 ]
	energy = sys.argv[ 2 ]
	totalEvents = sys.argv[ 3 ]
else 
	exit()
if len( sys.argv == 5) :
	eventsPerJob = sys.argv[ 4 ]



urqmd.createProject( name, energy, totalEvents, eventsPerJob )


urqmd.condorProject( name )
