#!/bin/bash

# clean up everything
sudo systemctl stop fix_not_found.service
sudo systemctl disable fix_not_found.service
sudo rm /lib/systemd/system/fix_not_found.service
sudo rm /home/pi/hnt/miner/log/fix_not_found.py
sudo rm /home/pi/hnt/miner/log/fix_not_found.log
