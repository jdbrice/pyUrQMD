#!/usr/bin/env python
import pyUrQMD.project as urqmd
import sys
import argparse

parser = argparse.ArgumentParser( description="Creates a slew of input files for submitting UrQMD to a cluster" );
parser.add_argument( "proj_name", help="project name - just creates a folder with this name and puts input files there" )
parser.add_argument( "ecm", help="Center of Mass energy" )
parser.add_argument( "total", help="Total # of events to generate" )
parser.add_argument( "epj", help="# of events per job" )

args = parser.parse_args()

name = args.proj_name
energy = float(args.ecm)
totalEvents = int(args.total)
eventsPerJob = int(args.epj)

urqmd.createProject( name, energy, totalEvents, eventsPerJob )
