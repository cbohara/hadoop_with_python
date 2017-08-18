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

######################################################
MapReduce framework notes
http://ercoppa.github.io/HadoopInternals/
######################################################

YARN Resource Manager = 1 per cluster = master
    know where slaves are located
    know how many resources each slave has
    runs Resource Scheduler = decides how to assign resources

YARN Node Managers = many per cluster = slaves
    each Node Manager offers resources to the cluster
    the Resource Scheduler decides how to use the slave's capacity
    each Container is a fraction of the Node Manager capacity and is used by client for running programs

Application Master
    responsible for execution of a single application
    it asks for containers to the Resource Manager
    executes programs on container

application startup process:
submit app to YARN Resource Manager (on master node) >
Resource Manager allocates a container (fraction of node)  >
Resource Manager contacts the related Node Manager > 
Node Manager launches a container >
contaienr executes the Application Master




######################################################
Chapter 2 - MapReduce with Hadoop Streaming and Python
######################################################

Hadoop Streaming allows MapReduce programs to be ran with any executable or script
can write mapper and reducer in Python scripts instead of using Java

mapper and reducer are executable files that read input line by line from stdin and write output to stdout

test word count locally first
$ echo 'jack be nimble jack be quick' | ./mapper.py | sort -t 1 | ./reducer.py

##############################################################################
Notes from Hadoop documentation
https://hadoop.apache.org/docs/r1.2.1/streaming.html
##############################################################################


both mapper and reducer are executables that read the input from stdin (line by line) and emit output to stdout
Hadoop streaming utility will create MapReduce job > submits job to cluster > monitor progress


the number of files inside the input directory is used to decide the number of Map Tasks of a job

mappers
Hadoop launches mapper executable as a process
input file > mapper executable > converts input file into lines + executes task on each line
mapper.py collects line oriented outputs from stdout > converts each line into key/value pair
Hadoop collects key/value pair output


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

$HADOOP_HOME/bin/hadoop jar /Users/hduser/tools/hadoop-2.7.3/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar -files mapper.py,reducer.py -mapper mapper.py -reducer reducer.py -input /user/hduser/input.txt -output /user/hduser/output/

mr job
    python mr_job.py input.txt -r [inline | local | hadoop | emr]
        inline = default = single Python process
        local = pseudodistributed mode
        hadoop = run on Hadoop cluster
        emr = https://pythonhosted.org/mrjob/guides/emr-quickstart.html

    python mr_job.py -r hadoop hdfs://my_home/input.txt
        

###############
Chapter 3 - Pig
###############

pig -x local
uses single local machine

cat pig_output/*
allows me to view the HDFS output on local machine

########
TOKENIZE
########

splits a string contained in a tuple
into a bag of words with each word in a single tuple


A  = LOAD 'data' AS (f1:chararray);

DUMP A;
(Here is the first string.)
(Here is the second string.)
(Here is the third string.)

X = FOREACH A GENERATE TOKENIZE(f1);

DUMP X;
({(Here),(is),(the),(first),(string.)})
({(Here),(is),(the),(second),(string.)})
({(Here),(is),(the),(third),(string.)})

#######
FLATTEN
#######

for tuples - flatten substitutes the fields of a tuple in place of the tuple
    ex: (a, (b, c)) > GENERATE $0, FLATTEN($1) > (a, b, c)

for bags - un-nest a bag to create new tuples
    ex: ({(b, c), (d, e)}) > GENERATE FLATTEN($0) > (b,c), (d, e)

