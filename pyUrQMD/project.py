import os
import inputfile


def createProject( p_name, energy, eventsPerJob ) :
	inputfile.writeInputfile( 10, 14.6 )

	p_root = "./" + str(p_name)
	if not os.path.exists(p_root):
	    os.makedirs(p_root)

	inputfile.writeInputfile( 10, 14.6, p_root + "/input1" )
	inputfile.writeInputfile( 10, 14.6, p_root + "/input2" )
	inputfile.writeInputfile( 10, 14.6, p_root + "/input3" )
