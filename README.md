# port-scan

Used to scan the port that are open.
You can use:
 - python port-scan.py host port
to only scan one port

 - python port-scan.py all host min_port max_port
to see the state of all ports between min_port and max_port

 - python port-scan.py open host min_port max_port
to only see the open ports between min and max

 - python port-scan.py listen host min_port max_port
to print the changes in ports that are opened and closed

To run the program you need socket, sys, and colorama with a python compatible.
Please report any bug to me so that I can correct it.
