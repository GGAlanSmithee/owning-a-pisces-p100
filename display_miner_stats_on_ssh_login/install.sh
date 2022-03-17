#!/bin/bash

# get and save the login script
wget -O fix_not_found_get_service.sh https://raw.githubusercontent.com/GGAlanSmithee/owning-a-pisces-p100/main/display_miner_stats_on_ssh_login/login_script.sh; chmod a+x /etc/profile.d/login_script.sh
