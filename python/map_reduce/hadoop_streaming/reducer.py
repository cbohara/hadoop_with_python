#!/usr/local/bin/python
import sys

curr_word = None
curr_count = 0

# process each key-value pair from the mapper
for line in sys.stdin:
    # get the key and value from the current line
    word, count = line.split('\t')
    # convert the count to an int
    count = int(count)

    # if the current word is the same as the previous word, increment its count
    if word == curr_word:
        curr_count += count
    # otherwise print the word count to stdout
    else:
        # write the word and its occurances as key-value to stdout
        if curr_word:
            print '{0}\t{1}'.format(curr_word, curr_count)
        # update curr_word and continue traversing through input file
        curr_word = word
        curr_count = count

# output the count for the last word
if curr_word == word:
    print '{0}\t{1}'.format(curr_word, curr_count)
