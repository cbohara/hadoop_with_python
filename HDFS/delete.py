#!/usr/bin/env python
from snakebite.client import Client

client = Client('localhost', 9000)

# recurse=True is equivalent to rm -rf so be careful!
for p in client.delete(['/foo', '/another'], recurse=True):
    print p
