# For : UrQMD 3.4 July 1 2015

# Templates used in the STARSIM Event Record Format
# For example the event record is :
# EVENT: 1 2 1
# VERTEX: 0 0 0 0 1 0 0 2
# TRACK:  8 -0.5197 0.319207 1.1729 1 0 0 211
# TRACK:  9 0.556838 -0.304097 1.29113 1 1 0 -211
# EVENT: 2 2 1
# VERTEX: 0 0 0 0 1 0 0 2
# TRACK:  8 0.385547 0.425939 -0.160369 2 0 0 211
# TRACK:  9 -0.479325 -0.461225 -0.0281709 2 1 0 -211
# EVENT: 3 2 1
# VERTEX: 0 0 0 0 1 0 0 2
# TRACK:  9 -0.494329 -0.34421 -0.264023 3 0 0 -211
# TRACK:  8 0.516517 0.324746 0.0201899 3 1 0 211
# EVENT: 4 2 1
# VERTEX: 0 0 0 0 1 0 0 2
# TRACK:  8 -0.556405 -0.315942 0.566879 4 0 0 211
# TRACK:  9 0.494289 0.329549 0.768293 4 1 0 -211
# etc.


# EVENT: event_id n_tracks n_vertices
# {0} = event_id - Event index starting at 1
# {1} = n_tracks - number of tracks in event
# {2} = n_vertices - number of vertices in event
tEvent = """EVENT: {0} {1} {2}"""

# VERTEX: x y z t vertex_id process parent_track n_daughters ,
# {0} = x - vX
# {1} = y - vY
# {2} = z - vZ
# {3} = t - Time of collision
# {4} = vertex_id - Vertex index starting at 1
# {5} = process - Physical process Index - always set to 0
# {6} = parent_track - Parent Track Index ( 0 for primary vertex )
# {7} = n_daughters - Number of daughter tracks from this vertex
tVertex = """VERTEX: {0} {1} {2} {3} {4} {5} {6} {7}"""

# TRACK: ge_pid px py pz track_id start_vertex stop_vertex eg_pid
# {0} = ge_pid - GEANT Particle ID ( see http://www.star.bnl.gov/public/comp/simu/gstar/Manual/particle_id.html )
# {1} = px - x momentum
# {2} = py - y momentum
# {3} = pz - z momentum
# {4} = track_id - Track Index ( starting at 1 )
# {5} = start_vertex - where track is born
# {6} = stop_vertex - vertex where track ends ( 0 for a track that does not end in this event)
# {7} = eg_pid - Event Generator PID
tTrack = """TRACK: {0} {1:f} {2:f} {3:f} {4} {5} {6} {7}"""


import os
import numpy as np

# Purpose :
# 1. Read UrQMD Event Header
# 2. Generate Random Vertex
# Read UrQMD Track Header
# Read Track - lookup PDGID?

class UrQMDEvent :
	index = 1
	nVertices = 1
	nTracks = 0

	def __init__(self, nIndex):
		self.index = nIndex
	def read_2_03( self, fIn, cLine ) :
		for i, line in enumerate( fIn ) :
			if i >= cLine and i < cLine + 16:
				print line 

	def read_3_4( self, fIn, cLine ) :
		#fIn.seek(0, 0)
		for i, line in enumerate( fIn, 0 ) :
			if i < 19:
				if i == 17 :
					data = line.split()
					self.nTracks = data[ 0 ]
			if i == 18 :
				break
		return 19;

def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1


ptypes = []
def geantID( ityp, iso3, charge ) :
	

	rnd = np.random.random_sample()

	#pions
	if ityp == 101 and charge == 0 :
		return 7
	if ityp == 101 and charge == 1 :
		return 8
	if ityp == 101 and charge == -1 :
		return 9

	#Kaons
	if abs(ityp) == 106 and charge == 0 :
		if rnd < 0.5 :
			return 16
		else :
			return 10
	if ityp == 106 and charge == 1 :
		return 11
	if ityp == -106 and charge == -1 :
		return 12

	
	#protons
	if ityp == 1 and charge == 1:
		return 14
	if ityp == -1 and charge == -1 :
		return 15
	if ityp == 1  and charge == 0 :
		return 13
	if ityp == -1  and charge == 0 :
		return 25

	#Sigma
	if ityp == 40 and charge == 1:
		return 19
	if ityp == 40 and charge == -1 :
		return 21
	if ityp == -40 and charge == 1:
		return 29
	if ityp == -40 and charge == -1 :
		return 27
	if ityp == 40  and charge == 0 :
		return 20
	if ityp == -40  and charge == 0 :
		return 28

	# Xi
	if ityp == 49 and charge == 0 :
		return 22 
	if ityp == -49 and charge == 0 :
		return 30
	if ityp == 49 and charge == -1 :
		return 23 
	if ityp == -49 and charge == 1 :
		return 31 

	#Lambda
	if ityp == 27 :
		return 18
	if ityp == -27 :
		return 26

	#Omega
	if ityp == 55 and charge == -1 :
		return 24
	if ityp == -55 and charge == 1 :
		return 32

	#Eta
	if ityp == 102 :
		return 17

	ptypes.append( ityp )
	return -1




class UrQMDTrack : 
	GPID = -1
	px = -1.0
	py = -1.0
	pz = -1.0
	stopv = 0
	EGPID = -1

	def read_3_4( self, fIn, cLine, nTracks ) : 
		#fIn.seek(0, 0)
		for i, line in enumerate( fIn, 0 ) :
			data = line.split()
		
			charge = self.GPID = data[ 11 ]

			# TODO: PDGID lookup from GPID and charge
			# itype+ iso3 + charge identify plc
			# need to build lookup table to geant plc id
			self.GPID = geantID( int(data[9]), int(data[10]), int(data[11]) )
			self.px = float(data[ 5 ])
			self.py = float(data[ 6 ])
			self.pz = float(data[ 7 ])
			self.EGPID = data[ 9 ]
			break;
		

# Samples a z Vertex
# gaussian in x and y
# flat in z
def rndVertex( x, sx, y, sy, zMin, zMax ) :
	vX = sx * np.random.randn() + x
	vY = sy * np.random.randn() + y
	vZ = np.random.random_sample( ) * (zMax - zMin) + zMin
	return ( vX, vY, vZ )



def nextOutputFile( basename ) :
	found = False;
	index = 0;
	while False == found :
		if os.path.isfile( basename + str(index) + ".tx" ) :
			found = False;
		else :
			found = True;
			return basename + str(index) + ".tx"
		index += 1;


OUTPUT_BASE_NAME = "urqmd_";

def convert( finput, split = -1 ) :

	split = int(split)
	fLength = file_len( finput )
	fInput = open( finput )
	
	if split > 1 :
		foutput = nextOutputFile( os.path.join( os.path.dirname(finput), OUTPUT_BASE_NAME) );
		print finput, "-->", foutput
		fOutput = open( foutput, 'w' )


	eof = False
	iEvent = 1
	currentLine = 0
	while eof == False :
		
		#Event 
		cEvent = UrQMDEvent( iEvent )
		currentLine += cEvent.read_3_4( fInput, currentLine );
		currentLine += int(cEvent.nTracks)
		if split > 1 :
			fOutput.write( tEvent.format( cEvent.index, cEvent.nTracks, cEvent.nVertices ) + "\n" )
		else :
			print tEvent.format( cEvent.index, cEvent.nTracks, cEvent.nVertices )

		# Vertex
		vX, vY, vZ = rndVertex( 0, 1.0, -0.89, 1.0, -30, 30 )
		vT = 0
		if split > 1 :
			fOutput.write( tVertex.format( vX, vY, vZ, vT, 1, 0, 0, cEvent.nTracks ) + "\n" )
		else :
			print tVertex.format( vX, vY, vZ, vT, 1, 0, 0, cEvent.nTracks )

		# Tracks
		for iTrack in range( 0, int(cEvent.nTracks) ) :
			cTrack = UrQMDTrack()
			cTrack.read_3_4( fInput, int(currentLine + iTrack), cEvent.nTracks)
			if split > 1 :
				fOutput.write( tTrack.format( cTrack.GPID, cTrack.px, cTrack.py, cTrack.pz, iTrack + 1, 1, 0, cTrack.EGPID ) + "\n" )
			else :
				print tTrack.format( cTrack.GPID, cTrack.px, cTrack.py, cTrack.pz, iTrack + 1, 1, 0, cTrack.EGPID )

		iEvent = iEvent + 1;

		if currentLine >= fLength :
			eof = True
			break

		# push to next file if we are splitting
		if split > 1 and iEvent > split :
			foutput = nextOutputFile( os.path.join( os.path.dirname(finput), OUTPUT_BASE_NAME) )
			print finput, "-->", foutput
			fOutput.close();
			fOutput = open( foutput, 'w' )
			iEvent = 1

		
	fInput.close()
	if split > 1 :
		fOutput.close()


