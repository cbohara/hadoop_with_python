#!/usr/bin/env python

import sys

curr_word = None
curr_count = 0

# process each key-value pair from the mapper
for line in sys.stdin:
    word, count = line.split("\t")
    count = int(count)

    # if the current word is the same as the previous word increment its count
    if word == curr_word:
        curr_count += count

    # if the current word does not match the previous word, then the previous word will never be seen again
    # because Hadoop sorts the keys before they are presented to the reducer function
    # therefore print word and its count to stdout
    else:
        # during the first iteration curr_word will be None but every other iteration will print to stdout
        if curr_word:
            print '{0}\t{1}'.format(curr_word, curr_count)

        # update the current word
        curr_word = word
        # reset the count to 1
        curr_count = count

# print the last word and count to stdout
if curr_word == word:
    print '{0}\t{1}'.format(curr_word, curr_count)
