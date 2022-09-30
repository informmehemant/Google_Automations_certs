#!/usr/bin/env python3

data = input("This will come from STDIN: ")
print("Now we write it to STDOUT: " + data)
raise ValueError("Now we generate an error to STDERR")

"""file discriptors like 2> is redirecting STDERR, 0 and 1 are the descriptors for SCDIN and SCDOUT."""
