# Splitting logs into files

There is some system that issues logs

The log line has the format:

    hh.mm.ss dd.mm.yyyy [Module_name] [PID:TID] Plain Text

Moreover, Plain Text can be on several lines.

This program splits this log either by date or by module name

Those. run like this (by date):

    python SplitTrace.py --daily <source file name>
    
Or (by module)

    python SplitTrace.py --module <source file name>

The mode of operation is passed as a command line argument
***

If for some reason the line cannot be defined in some file, then it is placed in 

    _Unknown_.log

The module name satisfies the expression:

    [a-zA-Z][a-zA-Z0-9_\.]*

Let there be two lines:

    12.51.34 23.09.2019 [File_Handler] Error dump:
    File Not Found exception
    
They must be placed in one file.

File name by dates:

    <source file name>_<date>.log

File name by modules:

    <source file name>_<module>.log

Implemented progressbar

2 GB file processes in ~13 seconds
