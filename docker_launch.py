#!/usr/bin/python2

import commands as sp
import cgi

print("content-type: text/html")
print("")


form  = cgi.FieldStorage()

imgname = form.getvalue("imagename")
dname = form.getvalue("dockername")


cmd="sudo docker run -dit --name {} {}".format(dname, imgname)

output = sp.getstatusoutput(cmd)

if output[0] == 0:
	print("docker os launched ...")
else:
	print("error")
