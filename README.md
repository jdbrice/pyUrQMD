## pyUrQMD

A small project for running UrQMD in parallel for production of a lot of events. This only seems neccessary because of the random number seed needs to be unique. The UrQMD input file specifies the random seed and the default only updates once per second - not acceptable for submission of jobs in parallel

####Usage:
```
urqmd.py project_name com_energy total_events events_per_job
```


#### Utility scripts

##### UrQMD_to_STARSIM_Event_Record.py
Converts a UrQMD standard output file ( f13 or f14) to the event record format used by STARSIM