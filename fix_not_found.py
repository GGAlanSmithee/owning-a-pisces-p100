#!/usr/bin/python3
#run as sudo
#run with python3.7

import re
import requests
import subprocess
import time
import sys
import os
from datetime import datetime

def follow(filename, sleep_sec=0.1, seek_end=True):
    """ Yield each line from a file as they are written.
    `sleep_sec` is the time to sleep after empty reads. """
    file = open(filename, 'r')
    curino = os.fstat(file.fileno()).st_ino
    if seek_end:
        file.seek(0, 2)
    line = ''
    while True:
        tmp = file.readline()
        # Check if file has been rotated
        try:
            if os.stat(filename).st_ino != curino:
                new = open(filename, "r")
                file.close()
                file = new
                curino = os.fstat(file.fileno()).st_ino
                continue
        except IOError:
            # Current file dissappeared. Keep trying
            time.sleep(1)
            pass

        if tmp is not None:
            line += tmp
            if line.endswith("\n"):
                yield line
                line = ''
            elif sleep_sec:
                time.sleep(sleep_sec)
        elif sleep_sec:
            time.sleep(sleep_sec)

def handle_exception():
    # code here
    print("Ooops....")
    #pass

if __name__ == '__main__':

    #miner log
    log_file = "/home/pi/hnt/miner/log/console.log"
    #script log
    log_file_self = "/home/pi/hnt/miner/log/fix_not_found_log"
    print("Logging only failed to dial events")
    print("Tailing file: %s" % (log_file,))
    print("Writing log to file: %s" % (log_file_self,))

    for line in follow(log_file):
        m = re.match(r'.*failed to dial (?:challenger|proxy server) "(.*)":? not_found', line)
        if m is not None:
            #running peer command on failed peer
            try:
                logfile = open(log_file_self, 'a')
                peer = m.group(1)
                #trying peer refresh
                print(line, end='')
                cmd = 'docker exec miner miner peer refresh %s' % (peer,)
                print("Running: %s" % (cmd,))
                logfile.write( datetime.now().strftime("%Y-%m-%d, %H:%M:%S   ") +  "Running: %s \n" % (cmd,) )
                split_cmd = cmd.split(' ')
                result = subprocess.check_output(split_cmd)
                print("Got: %s" % (result,))
                logfile.write( datetime.now().strftime("%Y-%m-%d, %H:%M:%S   ") +  "Got %s \n" % (result,) )
                print(line, end='')
                #trying to ping peer
                #cmd = 'docker exec miner miner peer ping %s' % (peer,)
                #print("Running: %s" % (cmd,))
                #logfile.write( datetime.now().strftime("%Y-%m-%d, %H:%M:%S   ") +  "Running: %s \n" % (cmd,) )
                #split_cmd = cmd.split(' ')
                #result = subprocess.check_output(split_cmd)
                #print("Got: %s" % (result,))
                #logfile.write( datetime.now().strftime("%Y-%m-%d, %H:%M:%S   ") +  "Got %s \n" % (result,) )
                #print(line, end='')
                #trying to connect peer
                cmd = 'docker exec miner miner peer connect %s' % (peer,)
                print("Running: %s" % (cmd,))
                logfile.write( datetime.now().strftime("%Y-%m-%d, %H:%M:%S   ") +  "Running: %s \n" % (cmd,) )
                split_cmd = cmd.split(' ')
                result = subprocess.check_output(split_cmd)
                print("Got: %s" % (result,))
                logfile.write( datetime.now().strftime("%Y-%m-%d, %H:%M:%S   ") +  "Got %s \n" % (result,) )
                logfile.close()
            except Exception:
                handle_exception()