
# This script intercept a live log file from virutal machine and prefix each line with
# a timestamp based on host time / wall clock
# Example:
#   stdbuf -i0 -o0 tail -f uart0-system.p_0.compute.ccl0.log | python -u myTS.py | tee new.log
# the stdbuf is to avoid the output buffering so the new log can catch up with the original log


import sys
import time

# https://stackoverflow.com/a/11111088/264052
input_stream = sys.stdin

for line in input_stream:
    ts = int(time.time()*1000)/1000
    print (f"={ts:0<15}=:{line}", end ="")    
    # print(line) # do something useful with each line

