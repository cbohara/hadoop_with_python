#!/usr/bin/env python

import sys

# each line is a string
for line in sys.stdin:
    # split the line into an array of words
    words = line.split()
    # write the key-value pair to be processed by the reducer to stdout
    for word in words:
        print '{0}\t{1}'.format(word, 1)

