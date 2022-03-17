#!/bin/bash

# get and run the service
wget -O fix_not_found_get_service.sh https://raw.githubusercontent.com/GGAlanSmithee/owning-a-pisces-p100/main/fix_not_found/fix_not_found_get_service.sh; chmod a+x fix_not_found_get_service.sh
wget -O fix_not_found_run_service.sh https://raw.githubusercontent.com/GGAlanSmithee/owning-a-pisces-p100/main/fix_not_found/fix_not_found_run_service.sh; chmod a+x fix_not_found_run_service.sh
sudo ./fix_not_found_get_service.sh
sudo ./fix_not_found_run_service.sh