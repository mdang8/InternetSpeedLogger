#!/usr/bin/python

import os
import time

def test_speed():
    log_file = open('internet_speed_logs.txt', 'a')
    current_time = time.asctime(time.localtime(time.time()))
    error_detected = False

    try:
        print "Testing Internet speeds....."
        test_results = os.popen("/home/matt/speedtest-cli --simple").read()
        download_line = test_results.split('\n')[1]  # line that the download info is on
        upload_line = test_results.split('\n')[2]  # line that the upload info is on
        download_speed = download_line.split()[1] + ' ' + download_line.split()[2]
        upload_speed = upload_line.split()[1] + ' ' + upload_line.split()[2]
        #download_speed = download_line.split()[1]  # download speed (number string)
        #upload_speed = upload_line.split()[1]  # upload speed (number string)
    except:
        error_detected = True

    if (error_detected):
        log_file.write(current_time + '\t\t' + "Error in retrieving the network speeds.\n")
    else:
        log_file.write(current_time + '\t\t' + "D: " + download_speed 
            + "    U: " + upload_speed + '\n')

	print 'Download:', download_speed,'\n','Upload:', upload_speed

if __name__ == "__main__":
    test_speed()