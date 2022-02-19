#!/bin/bash

# run service

sudo systemctl daemon-reload
sudo systemctl disable fix_not_found.service
sudo systemctl stop fix_not_found.service
sudo systemctl start fix_not_found.service
sudo systemctl enable fix_not_found.service