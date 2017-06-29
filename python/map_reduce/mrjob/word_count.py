#!/usr/local/bin/python3
from mrjob.job import MRJob

# MRWordCount inherits from MRJob the methods that define the steps of the MapReduce job
class MRWordCount(MRJob):
    # hadoop accepts unstructured data and transforms to key, value pair
    # in this example, (key, value) is (line number, words in line)

    # mapper function takes in (line number, words in line) and 
    # pairs each word with a count of 1 (word, 1)

    # input - key (line number), value (string of words in line)
    # in this example the mapper ignores the input key (hence _)
    # output - generator of tuples (word, 1)
    def mapper(self, _, line):
        for word in line.split():
            yield(word, 1)

    # hadoop shuffle will combine the values for each key 
    # ex: (jack, [1, 1])

    # reducer function takes in (key, some sort of iterator)
    # in this example (word, [list of counts])

    # input - key, iterator of values
    # reducer sums the values in the list to 
    # output - (word, count)
    def reducer(self, word, counts):
        yield(word, sum(counts))


if __name__ == "__main__":
    # need this line in order for application to work
    # by default mrjob writes output to stdout
    MRWordCount.run()
