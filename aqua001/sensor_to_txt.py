ports = ['/dev/ttyUSB0','/dev/ttyACM0','/dev/ttyUSB1','NULL']
from serial import Serial
import time
import datetime
import sys
from datetime import datetime
from time import sleep
import mymodule
import string
import phant
import mymodule
import urllib
import urllib2
import logging
import pdb

logtime = str(datetime.now().strftime('%Y%m%d'))
logging_date=logtime

lgr = logging.getLogger('Sensor')
lgr.setLevel(logging.DEBUG) # log all escalated at and above DEBUG
fh = logging.FileHandler('/home/pi/projects/scripts/log/%ssensor.csv'%logtime)
fh.setLevel(logging.DEBUG) # ensure all messages are logged to file
frmt = logging.Formatter('%(asctime)s,%(name)s,%(levelname)s,%(message)s')
fh.setFormatter(frmt)
lgr.addHandler(fh)


f = open("/etc/hostname","r") #opens file with name of "test.txt"
myhostname = f.read().replace('\n', '')
for p in ports:
	try:
		print "trying port: "+p
		if (p=='NULL'):
        		print "getting off"
			sys.exit()
		ser = Serial(p, 9600)
		break
	except:
		print "error connecting...aborting" + p
		#sys.exit()
time.sleep(4)
#dummy message
while True:
 #check if it's new day, if yes create new file
        logtime = str(datetime.now().strftime('%Y%m%d'))
        if (logging_date<>logtime):#time for mew log file
                logging_daye=logtime
                lgr.removeHandler(fh)
                fh = logging.FileHandler('/home/pi/projects/scripts/log/%ssensor.csv'%logtime)
                fh.setLevel(logging.DEBUG) # ensure all messages are logged to file
                frmt = logging.Formatter('%(asctime)s,%(name)s,%(levelname)s,%(message)s')
                fh.setFormatter(frmt)
                lgr.addHandler(fh)

	mytime = str(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        shorttime=str(datetime.now().strftime('%H%M%S'))
	try:
		x=ser.readline()
		print "x="+x
		foo = x.split(",")
		if len(foo)==8:
#			print foo
			tm= "%s,%s,%s,%s,%s,%s,%s,%s,%s" %(mytime,foo[0],foo[1],foo[2],foo[3],foo[4],foo[5],foo[6],foo[7].replace('\n', ''))
#		        print 'tm',tm
	        	try:
		                with open("/home/pi/projects/scripts/sensor.txt", "w") as text_file:
					   lgr.info(tm)
					   print "logeed line added"
                                           text_file.write(tm)
                		text_file.close()
		        except:
        		        print "cannot open file for writting"
	except:
		print "device not ready"
	time.sleep(10)

#end of loop
