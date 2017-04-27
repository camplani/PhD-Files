#!/bin/bash
echo "Here the script is starting"
echo "Hello $USER!"
echo "I'm checking ARP_module simulation"
cd ../simulation/ethernet_lib/ARP_module/ 
pwd=`pwd`
echo I am here: $pwd
simulation=`make simulation | tee my_new_log.log`
parsing=`pyhton parse.py`
set -e
echo "I'm going back to the script directory"
cd ~/git/atlas-lar-ldpb-firmware/ABBA/scripts/