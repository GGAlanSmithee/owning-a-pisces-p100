# owning-a-pisces-p100

Things used for my Pisces P100

## DISCLAIMER

WARNING! USE THESE SCRIPTS ON YOUR OWN RISK! I DON'T ACCEPT ANY RESPONSIBILITY ON ANY DAMAGED CAUSED!

## LICENSE

[MIT](./LICENSE)

## fix_not_found

`wget -O - https://raw.githubusercontent.com/GGAlanSmithee/owning-a-pisces-p100/main/fix_not_found/install.sh | bash`

Credit goes to [@herrtakacs](https://github.com/herrtakacs) for providing this script as a service.

Registers a service which is run immediately as well as run on startup. It perform the following steps:

1. scan the `error.log` for "not_found" issues
2. attempt to fix them by manually refreshing the peers with their respective ids
3. write to a new log `/home/pi/hnt/miner/log/fix_not_found.log`
