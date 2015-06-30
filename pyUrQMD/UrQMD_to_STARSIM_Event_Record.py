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


# EVENT:  n  ntracks  nvertices
# {0} = n - Event index starting at 1
# {1} = ntracks - number of tracks in event
# {2} = nvertices - number of vertices in event
tEvent = """EVENT: {0} {1} {2}"""

# VERTEX:  x  y  z  t  nv  nproc  nparent  ndaughters ,
# {0} = x - vX
# {1} = y - vY
# {2} = z - vZ
# {3} = t - Time of collision
# {4} = nv - Vertex index starting at 1
# {5} = nproc - Physical process Index - always set to 0
# {6} = nparent - Parent Track Index ( 0 for primary vertex )
# {7} = ndaughters - Number of daughter tracks from this vertex
tVertex = """VERTEX: {0} {1} {2} {3} {4} {5} {6} {7}"""

# TRACK:  GPID  px  py  py nev  ntr  stopv PDGPID
# {0} = GPID - GEANT Particle ID ( see http://www.star.bnl.gov/public/comp/simu/gstar/Manual/particle_id.html )
# {1} = px - x momentum
# {2} = py - y momentum
# {3} = pz - z momentum
# {4} = nev - Event index
# {5} = ntr - Track Index ( starting at 0 of course )
# {6} = stopv - vertex where track ends ( 0 for a track that does not end in this event)
# {7} = PDGPID - Particle Data Group Particle ID ( see http://pdg.lbl.gov/2002/montecarlorpp.pdf )
tTrack = """TRACK: {0} {1:f} {2:f} {3:f} {4} {5} {6} {7}"""


import sys
import numpy as np

# Read UrQMD Event Header
# Generate Random Vertex?
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
				#print line 
		return currentLine + 19

def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

class UrQMDTrack : 
	GPID = -1
	px = -1.0
	py = -1.0
	pz = -1.0
	stopv = 0
	PDGPID = 0

	def read_3_4( self, fIn, cLine, nTracks ) : 
		#fIn.seek(0, 0)
		for i, line in enumerate( fInput, 0 ) :
			data = line.split()
			self.GPID = data[ 9 ]
			self.px = float(data[ 5 ])
			self.py = float(data[ 6 ])
			self.pz = float(data[ 7 ])
			break;
		

# Samples a z Vertex
# gaussian in x and y
# flat in z
def rndVertex( x, sx, y, sy, zMin, zMax ) :
	vX = sx * np.random.randn() + x
	vY = sy * np.random.randn() + y
	vZ = np.random.random_sample( ) * 60 - 30
	return ( vX, vY, vZ )


fLength = file_len( sys.argv[1] )


fInput = open( sys.argv[1] )

eof = False
iEvent = 1
currentLine = 0
while eof == False :
	
	#Event 
	cEvent = UrQMDEvent( iEvent )
	currentLine = cEvent.read_3_4( fInput, currentLine );
	currentLine += int(cEvent.nTracks)
	print tEvent.format( cEvent.index, cEvent.nTracks, cEvent.nVertices )

	# Vertex
	vX, vY, vZ = rndVertex( 0, 1.0, -0.89, 1.0, -30, 30 )
	vT = 0
	print tVertex.format( vX, vY, vZ, vT, 1, 0, 0, cEvent.nTracks )

	# Tracks
	for iTrack in range( 0, int(cEvent.nTracks) ) :
		cTrack = UrQMDTrack()
		cTrack.read_3_4( fInput, int(currentLine + iTrack), cEvent.nTracks)
		print tTrack.format( cTrack.PDGPID, cTrack.px, cTrack.py, cTrack.pz, cEvent.index, iTrack, cTrack.stopv, cTrack.GPID )

	iEvent = iEvent + 1;
	if currentLine >= fLength :
		eof = True
		break

fInput.close()

