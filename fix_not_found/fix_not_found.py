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
    pass

if __name__ == '__main__':

    #miner log
    log_file = "/home/pi/hnt/miner/log/console.log"
    #script log
    log_file_self = "/home/pi/hnt/miner/log/fix_not_found.log"
    logfile = open(log_file_self, 'a')
    logfile.write(datetime.now().strftime("%Y-%m-%d, %H:%M:%S\n"))
    logfile.write("Logging failed to dial events\n")
    logfile.write("Tailing file: %s\n" % (log_file,))
    logfile.write("Writing log to file: %s\n" % (log_file_self,))
    logfile.close()

    for line in follow(log_file):
        m = re.match(r'.*failed to dial (?:challenger|proxy server) "(.*)":? not_found', line)
        if m is not None:
            #running peer commands on failed peer
            try:
                logfile = open(log_file_self, 'a')
                peer = m.group(1)
                #trying peer refresh
                cmd = 'docker exec miner miner peer refresh %s' % (peer,)
                logfile.write( datetime.now().strftime("%Y-%m-%d, %H:%M:%S   ") +  "Running: %s \n" % (cmd,) )
                split_cmd = cmd.split(' ')
                result = subprocess.check_output(split_cmd)
                logfile.write( datetime.now().strftime("%Y-%m-%d, %H:%M:%S   ") +  "Got %s \n" % (result,) )
                #trying to ping peer
                #logfile.write( datetime.now().strftime("%Y-%m-%d, %H:%M:%S   ") +  "Running: %s \n" % (cmd,) )
                #split_cmd = cmd.split(' ')
                #result = subprocess.check_output(split_cmd)
                #logfile.write( datetime.now().strftime("%Y-%m-%d, %H:%M:%S   ") +  "Got %s \n" % (result,) )
                #trying to connect peer
                cmd = 'docker exec miner miner peer connect %s' % (peer,)
                logfile.write( datetime.now().strftime("%Y-%m-%d, %H:%M:%S   ") +  "Running: %s \n" % (cmd,) )
                split_cmd = cmd.split(' ')
                result = subprocess.check_output(split_cmd)
                logfile.write( datetime.now().strftime("%Y-%m-%d, %H:%M:%S   ") +  "Got %s \n" % (result,) )
                logfile.close()
            except Exception:
                handle_exception()