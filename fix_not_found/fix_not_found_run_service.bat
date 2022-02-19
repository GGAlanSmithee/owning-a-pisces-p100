#!/bin/bash

sudo systemctl stop fix_not_found.service
sudo systemctl disable fix_not_found.service
sudo rm -f /home/pi/hnt/miner/log/fix_not_found.log
sudo systemctl start fix_not_found.service
sudo rm -f /lib/systemd/system/fix_not_found.service
sudo rm -f /home/pi/hnt/miner/log/fix_not_found.py