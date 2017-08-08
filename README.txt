##############################################################################
Notes from MRJob documentation
https://pythonhosted.org/mrjob/guides/concepts.html#hadoop-streaming-and-mrjob
##############################################################################

MapReduce 
    job splits input data set into independent chunks
    processed by map tasks in a completely parallel manner
    framework sorts the output of the map tasks
    input to reduce tasks

master node = scheduling job tasks to the worker nodes
worker nodes = execute the tasks

as the job author, you write map, combine, and reduce functions that are submitted to the job tracker for execution

mapper
    takes single key-value as input
    returns 0 or more key-value pairs

framework sorts by key

combiner
    takes a key and subset of key values
    returns 0 or more key-value pairs
    optimizations that run immediately after each mapper
    used to decrease total data transfer

reducer
    takes the key and complete set of values for that key
    return 0 or more key-value pairs as output

after the reducer is done, 
    if there are more steps > individual results arbitrarily assigned to mappers for further processing
    otherwise results are sorted and made available to stdout

Hadoop streaming
    Hadoop is primarily designed to work with Java code
    supports other languages via Hadoop streaming
    jar opens subprocess to your code > sends its input via stdin > gathers results via stdout

    input raw text > mapper > key1\tvalue1\nkey1\tvalue2\nkey2\tvalue2\n > 
    hadoop shuffles and sorts by key >
    sends same key-value to same combiner/reducer as ("key1", [value1, value2]) > 
    combiner/reducer stdout "key1", value1+value2

mr job
    python mr_job.py input.txt -r [inline | local | hadoop | emr]
        inline = default = single Python process
        local = pseudodistributed mode
        hadoop = run on Hadoop cluster
        emr = https://pythonhosted.org/mrjob/guides/emr-quickstart.html

    python mr_job.py -r hadoop hdfs://my_home/input.txt
        


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
