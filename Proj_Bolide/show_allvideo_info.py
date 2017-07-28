####################################################################
# Test script : show_allvideo_info.py                              
# Purpose : Print Video Format, Video Resolution, Video Fps      
# Author : Leo Lo (llo1@logitech.com)
# Version : v0.01
# Date : 2017/07/28
####################################################################

### Import Library path
import sys
print(sys.path)
sys.path.insert(0,"C:/Py_Automation_System/lib")
print(sys.path)


### Import Packages
from logi_commonlib import *


print_lib("I am Leo!!!")

### Variables
video_fmt = "MJPG"
video_resolu = "1920x1080"
video_fps = 30
#jobfile_csv = sys.argv[1]

#video_fmt = sys.argv[1]
#video_resolu = sys.argv[2]
#video_fps = int(sys.argv[3])

### Subroutines

def readcsv(csv_file):

    # Open csv file
    # Read csv file for each line to a list
    # Return the list
    return 0


### Main Function
try:    
    print("show_allvideo_info.py : (%s,%s,%s)" %(video_fmt,video_resolu,video_fps))

except Exception as msg:
    print("[Error] : %s" %msg)

finally: # No matter exception occurs or not, this line will always excutes
    print("[Info] : %s" %"Test Done!")
    
