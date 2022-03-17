# owning-a-pisces-p100

Things used for my Pisces P100

## DISCLAIMER

WARNING! USE THESE SCRIPTS ON YOUR OWN RISK! WE DO NOT ACCEPT ANY RESPONSIBILITY FOR ANY DAMAGED CAUSED!

## LICENSE

[MIT](./LICENSE)

## fix_not_found

### Install

`wget -O - https://raw.githubusercontent.com/GGAlanSmithee/owning-a-pisces-p100/main/fix_not_found/install.sh |sudo bash`

### Uninstall

`wget -O - https://raw.githubusercontent.com/GGAlanSmithee/owning-a-pisces-p100/main/fix_not_found/uninstall.sh |sudo bash`

### Explanation

Registers a service which is run immediately as well as run on startup. It perform the following steps:

1. scan the `error.log` for "not_found" issues
2. attempt to fix them by manually refreshing the peers with their respective ids
3. write to a new log `/home/pi/hnt/miner/log/fix_not_found.log`

Credit goes to https://github.com/HeliumDIY/helium_workarounds for creating the original script, and to [@herrtakacs](https://github.com/herrtakacs) for providing the script as a service.

## display_miner_stats_on_ssh_login

### Install

`wget -O - https://raw.githubusercontent.com/GGAlanSmithee/owning-a-pisces-p100/main/display_miner_stats_on_ssh_login/install.sh |sudo bash`

### Uninstall

`wget -O - https://raw.githubusercontent.com/GGAlanSmithee/owning-a-pisces-p100/main/display_miner_stats_on_ssh_login/uninstall.sh |sudo bash`

### Explanation

Registers a script which is executed on ssh login and shows current CPU temperature and disk usage.