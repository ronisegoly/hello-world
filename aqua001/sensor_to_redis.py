import time
import datetime
import sys
from datetime import datetime
from time import sleep
import mymodule
import string
#import phant
import urllib
import urllib2
import pdb
#pdb.set_trace()

f = open("/etc/hostname","r") #opens file with name of "test.txt"
myhostname = f.read().replace('\n', '')


mytime = str(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
shorttime=str(datetime.now().strftime('%H%M%S'))
try:
	with open("/home/pi/projects/scripts/sensor.txt", "r") as text_file:
        	x= text_file.read()
      		text_file.close()
except Excpetion, s:
	print 'unable to open file' + str(s)

foo = x.split(",")
if len(foo)>7:
	print 'foo',foo
	try:
		mymodule.r.hmset(myhostname, {'time':str(foo[0]), 'V1':str(foo[1]),'V2':str(foo[2]),'V3':str(foo[3]),'V4':str(foo[4]),'V5':str(foo[5]),'V6':str(foo[6]),'V7':str(foo[7]),'V8':str(foo[8])})
		print 'redis demo set'
	except Excpetion, s:
		print "error using redis" + str(s)

