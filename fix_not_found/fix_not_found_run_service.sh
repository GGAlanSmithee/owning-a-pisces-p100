#!/bin/bash

# run service
sudo systemctl daemon-reload
sudo systemctl start fix_not_found.service
sudo systemctl enable fix_not_found.service