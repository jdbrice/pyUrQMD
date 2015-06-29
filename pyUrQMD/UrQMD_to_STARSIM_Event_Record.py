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
tTrack = """TRACK: {0} {1} {2} {3} {4} {5} {6} {7}"""



# Read UrQMD Event Header
# Generate Random Vertex?
# Read UrQMD Track Header
# Read Track - lookup PDGID?

class UrQMDEvent :
	index = 1
	nVertices = 0
	nTracks = 0

	def __init__(self):
		index = 1
	def read_2_03( self, fIn, cLine ) :
		for i, line in enumerate( fIn ) :
			if i >= cLine and i < cLine + 16:
				print line 


fInput = open( "151.f13" )

cEvent = UrQMDEvent()
currentLine = 0

cEvent.read_2_03( fInput, currentLine );




fInput.close()

