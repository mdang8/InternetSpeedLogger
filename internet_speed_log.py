#!/usr/bin/python

import os
import sys
import time

def test_speed():
    log_file = open('/home/pi/Documents/Internet_Log/internet_speed_logs.txt', 'a')
    current_time = time.asctime(time.localtime(time.time()))

    try:
        print "Testing Internet speeds....."
        test_results = os.popen("/usr/local/bin/speedtest-cli --simple").read()
        download_line = test_results.split('\n')[1]  # line that the download info is on
        upload_line = test_results.split('\n')[2]  # line that the upload info is on
        download_speed = download_line.split()[1] + ' ' + download_line.split()[2]
        upload_speed = upload_line.split()[1] + ' ' + upload_line.split()[2]
    except Exception, e:
        log_file.write(current_time + '\t\t' + "Error: " + str(e) + ' ' + str(len(test_results)) + '\n')
        print str(e)
        sys.exit()

    log_file.write(current_time + '\t\t' + 'D: ' + download_speed 
        + '\t\tU: ' + upload_speed + '\n')
    print 'Download:', download_speed,'\n','Upload:', upload_speed

if __name__ == "__main__":
    test_speed()
