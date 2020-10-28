#!/bin/bash

PREFIX="js-"

LOG=/var/log/dhcp_hostname.log

# Sync OS time using the host's hardware time
echo $(date +"%m%d%y %H:%M:%S") "Syncing system time with hardware time" >> $LOG
echo "     DEBUG: Date BEFORE sync:" $(date) >> $LOG
hwclock -s
rc=$?
echo "     DEBUG: Date AFTER sync:" $(date)  "hwclock exit status: $rc" >> $LOG


hostname_value=$(curl -s http://169.254.169.254/latest/meta-data/hostname | sed 's/novalocal/jetstreamlocal/')

if [ -z $hostname_value ]; then
    echo "Unable to detemine hostname!" >> $LOG
else
    hostname $hostname_value
    echo $hostname_value > /etc/hostname
fi

