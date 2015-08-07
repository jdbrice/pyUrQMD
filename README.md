## pyUrQMD

A small project for running UrQMD in parallel for production of a lot of events. This is only neccessary because of the random number seed needs to be unique. The UrQMD input file specifies the random seed and the default only updates once per second - not acceptable for submission of jobs in parallel

####Usage:
``` 
usage: pyurqmd.py [-h] proj_name ecm total epj

Creates a slew of input files for submitting UrQMD to a cluster

positional arguments:
  proj_name   project name - just creates a folder with this name and puts
              input files there
  ecm         Center of Mass energy
  total       Total # of events to generate
  epj         # of events per job

optional arguments:
  -h, --help  show this help message and exit
```
This creates a folder project_name/ and puts the urqmd input files there. 

#### Utility scripts

##### condor_submit.py
Submits a folder of input files to Condor, with each input file running a job. This sets the environment variables that fortran uses to capture file handles and then submits to cluster. Use it as a template for submitting to other schedulers.
Usage :
```
condor_submit.py project_name
```

##### UrQMD_to_STARSIM_Event_Record.py
Converts a UrQMD standard output file ( f13 or f14) to the event record format used by STARSIM
Usage :
``` bash
usage: convert.py [-h] [-split SPLIT] [-vX VX] [-vY VY] [-sig_vX SIG_VX]
                  [-sig_vY SIG_VY] [-z_min Z_MIN] [-z_max Z_MAX]
                  input

Converts a UrQMD standard output (f13 or f14) into the (new) STAR TX format.
Can convert all files in a directory if a directory path is given. Otherwise
the given file is converted and written to stdout

positional arguments:
  input           Input filename or directory containing UrQMD standard output
                  files

optional arguments:
  -h, --help      show this help message and exit
  -split SPLIT    Splits into N events per file with the output file having
                  the input filename + .tx suffix
  -vX VX          vX distribution center
  -vY VY          vY distribution center
  -sig_vX SIG_VX  sig_vX for generating Vx distribution
  -sig_vY SIG_VY  sig_vY for generating Vy distribution
  -z_min Z_MIN    z_min for generating Vz distribution, generates a uniform vZ
                  from z_min to z_max
  -z_max Z_MAX    z_max for generating Vz distribution
```