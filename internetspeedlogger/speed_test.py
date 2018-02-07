import datetime
import sys
import os
import re


def test_speed():
    # command to print the speed test results in a simple format
    cli_command = '/usr/local/bin/speedtest-cli --simple'
    # creates a timestamp
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    parsed_results = {}

    try:
        results = os.popen(cli_command).read()
        parsed_results = parse_test_results(results)
        parsed_results["timestamp"] = timestamp
    except Exception as e:
        print(str(e))
        sys.exit()

    return parsed_results
    

def parse_test_results(results):
    # regexes for matching each relevant test result value
    ping = re.search('(?<=Ping: )(.*)(?= ms)', results)
    download = re.search('(?<=Download: )(.*)(?= Mbit\/s)', results)
    upload = re.search('(?<=Upload: )(.*)(?= Mbit\/s)', results)
    readings = {
        "ping": ping.group(),
        "download": download.group(),
        "upload": upload.group()
    }

    return readings
