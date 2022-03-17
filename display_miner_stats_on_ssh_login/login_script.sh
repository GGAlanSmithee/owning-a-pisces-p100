#!/bin/bash

# display CPU temp
cpu=$(</sys/class/thermal/thermal_zone0/temp)
echo "CPU Temperature: $((cpu/1000))C"

# display disk usage
used=$(df -Ph | grep '/dev/root' | awk {'print $5'})
echo "Disk usage: $used"