#!/usr/bin/env python
from snakebite.client import Client

client = Client('localhost', 9000)

# specifying create_parent=True is the equivalent of mkdir -p
for p in client.mkdir(['/foo/bar', '/another'], create_parent=True):
    print p
