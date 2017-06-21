#!/usr/local/bin/python
from snakebite.client import Client

# this line creates the client connection to the HDFS NameNode
# NameNode hostname = localhost, NameNode port = 9000
# these parameters are set in hadoop/conf/core-site.xml under fs.defaultFS
client = Client('localhost', 9000)

# list the content of the HDFS root directory
# note that many methods in snakebite returns generators 
for x in client.ls(['/']):
    print x
