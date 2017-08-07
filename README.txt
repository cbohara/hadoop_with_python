################################################################
MapReduce example from Hadoop: The Definitive Guide by Tom White
################################################################

we want to determine the maximum temperature for a given year

the raw weather station data is one line of test which contains the year and a temp reading

0067011990999991950051507004...9999999N9+00001+99999999999...
0043011990999991950051512004...9999999N9+00221+99999999999...
0043011990999991950051518004...9999999N9-00111+99999999999...

raw input data is presented to map function as key-value pair with the key being the line number

(0, 0067011990999991950051507004...9999999N9+00001+99999999999...)
(1, 0043011990999991950051512004...9999999N9+00221+99999999999...)
(2, 0043011990999991950051518004...9999999N9-00111+99999999999...)

mapper function will grab the year and the temperature from each line and output the result as a key-value pair

(1950, 0)
(1950, 22)
(1950, −11)
(1949, 111)
(1949, 78)

the Hadoop framework will then sort these key-value pairs and combine based on the key 
    all key-value pairs are sorted before being presented to the reducer function
    all key-value pairs sharing the same key are sent to the same reducer 
        

(1949, [111, 78])
(1950, [0, 22, −11])

reducer function will iterate through the values and find the maximum temp

(1949, 111)
(1950, 22)


################
Hadoop Streaming
################

allows MapReduce programs to be ran with any executable or script
can write mapper and reducer in Python scripts instead of using Java

mapper and reducer are executable files that read input line by line from stdin and write output to stdout

test word count locally first
$ echo 'jack be nimble jack be quick' | ./mapper.py | sort -t 1 | ./reducer.py


