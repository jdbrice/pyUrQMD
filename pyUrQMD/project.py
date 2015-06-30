import os
import inputfile
import subprocess

def createProject( p_name, energy, totalEvents, eventsPerJob = 100 ) :

	p_root = "./" + str(p_name)
	if not os.path.exists(p_root):
	    os.makedirs(p_root)

	for i in range( 0, totalEvents / eventsPerJob  ) :
		inputfile.writeInputfile( eventsPerJob, energy, p_root + "/input" + str(i) + ".urqmd" )

def exportOutputFile( index, path ) : 
	fname = os.path.abspath( os.path.join( path, "ouput" + str(index) + ".f13" ) )
	os.environ[ "ftn13" ] =  fname # standard output with freeze-out info
	print "ftn13 = " + fname

def exportInputFile( index, path, suffix=".urqmd" ) : 
	fname = os.path.abspath( os.path.join( path, "input" + str(index) + suffix ) )
	os.environ[ "ftn09" ] = fname # standard output with freeze-out info
	print "ftn09 = " + fname


def condorProject( p_name, ifsuffix = ".urqmd" ) :
	p_root = "./" + str(p_name)
	for dirname, subdirList, fileList in os.walk( p_root ) :
		for f in fileList :
			if f.startswith( "input" ) and f.endswith( ifsuffix ):
				findex = int(f[ len("input") : -len(ifsuffix) ])
				exportInputFile( findex, dirname )
				exportOutputFile( findex, dirname )
				outFile = "output = " + os.path.join( dirname, "log." + str(findex) + ".log" )
				subprocess.check_call(['condor_submit', '-a', outFile, 'condor.submit'], env=os.environ)


def qsubProject( p_name, ifsuffix = ".urqmd" ) :
	p_root = "./" + str(p_name)
	for dirname, subdirList, fileList in os.walk( p_root ) :
		for f in fileList :
			if f.startswith( "input" ) and f.endswith( ifsuffix ):
				findex = int(f[ len("input") : -len(ifsuffix) ])
				exportInputFile( findex, dirname )
				exportOutputFile( findex, dirname )
				outFile = os.path.join( dirname, "log." + str(findex) + ".log" )
				subprocess.check_call(['qsub', '-o', outFile, 'urqmd.sh'], env=os.environ)


