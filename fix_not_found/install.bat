#!/bin/bash

wget -O fix_not_found_register_service.bat https://raw.githubusercontent.com/GGAlanSmithee/owning-a-pisces-p100/main/fix_not_found/fix_not_found_register_service.bat; chmod a+x fix_not_found_register_service.bat
wget -O fix_not_found_run_service.bat https://raw.githubusercontent.com/GGAlanSmithee/owning-a-pisces-p100/main/fix_not_found/fix_not_found_run_service.bat; chmod a+x fix_not_found_run_service.bat
sudo ./fix_not_found_register_service.bat
sudo ./fix_not_found_run_service.bat