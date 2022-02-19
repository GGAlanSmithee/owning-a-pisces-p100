#!/bin/bash

wget https://raw.githubusercontent.com/GGAlanSmithee/owning-a-pisces-p100/main/fix_not_found/fix_not_found.service -O /lib/systemd/system/fix_not_found.service
wget https://raw.githubusercontent.com/GGAlanSmithee/owning-a-pisces-p100/main/fix_not_found/fix_not_found.py -O /home/pi/hnt/miner/log/fix_not_found.py
sudo chmod 644 /lib/systemd/system/fix_not_found.service
sudo chmod +x /lib/systemd/system/fix_not_found.service