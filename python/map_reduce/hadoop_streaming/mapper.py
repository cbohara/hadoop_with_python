#!/usr/local/bin/python
import sys

# read each line from stdin
for line in sys.stdin:
     # get the words in each line
     words = line.split()
     # generate the count for each word
     for word in words:
        # write the key-value pair (word, 1) to stdout to be processed by reducer
        print '{0}\t{1}'.format(word, 1)
