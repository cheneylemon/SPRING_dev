#!/usr/bin/env python
import cgi
import cgitb
import os
cgitb.enable()  # for troubleshooting
print "Content-Type: text/html"
print 

data = cgi.FieldStorage()
path = data.getvalue('path')
out = []
for f in os.listdir(path):
	if os.path.exists(path+'/'+f+'/run_info.json'):
		out.append(f)
print ','.join(sorted(out,key=lambda x: x.lower()))
