import os
import sys
import mydb
import pdb
import datetime
import sys
from datetime import datetime

path = '/home/pi/projects/scripts/log/'
logtime = str(datetime.now().strftime('%Y%m%d'))
print logtime
for file in os.listdir(path):
        if (file.find("csv")>-1):
                if (file.find(logtime)>-1):
                        print "todays log, not touching " +file
                else:
                        print "Will be uploaded and deleted " + file
#                       pdb.set_trace()
			msg = "~/Dropbox-Uploader/dropbox_uploader.sh upload %s%s /log/ " %(path,file)
			print msg
                        os.system(msg)
			os.remove(path+file)
