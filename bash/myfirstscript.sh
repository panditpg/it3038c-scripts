#!/bin/bash
#This script will output the IP address and hostname of a machine

a=$(ip a | grep 'dynamic ens192' | awk '{print $2}')
echo  $a







