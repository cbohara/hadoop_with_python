#!/user/local/bin/python
from snakebite.client import Client

client = Client('localhost', 9000)

for f in client.copyToLocal(['/user/cbohara/book.txt'], '/tmp'):
    print f
