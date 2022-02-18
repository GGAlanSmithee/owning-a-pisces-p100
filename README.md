# owning-a-pisces-p100
things used for my Pisces P100

## fix_not_found.py

1. scans the `error.log` for "not_found" issues
2. attempt to fix them by manually refreshing the peers with their respective ids
3. write to a new log `fix_not_found_log.log`

Run instructions

1. `wget -O fix_not_found.py 
https://raw.githubusercontent.com/GGAlanSmithee/owning-a-pisces-p100/main/fix_not_found.py; chmod a+x fix_not_found.py` download the script
2. `sudo nohup python3.7 -u fix_not_found_v2.py &` runs the script in the background and outputs the process id (used to later stop it)

* `sudo kill PID` if you later want to kill the process
* `ps ax | grep python` if you lost the process ID, you can get it with this command
