#!/user/local/bin/python
from snakebite.client import Client

client = Client('localhost', 9000)

# text() automatically uncompress and display gzip and bzip2 files
for line in client.text(['/user/cbohara/book.txt']):
    print line
