# it3038c-scripts
'''javascript
Javascript code block

### Hello
##### It's me, a Netwoking student!

Lab 2

#!/bin/bash
#This script email user, IP, date, and hostname
    content="User $USER"
    emailaddress="panditpgmail.uc.edu"
    today=$(date +"%H:%M:%S")
    ip=$(ip a | grep 'dynamic ens192' | awk '{print $2}')
    content="ip $ip, User $USER, date $today, host $HOSTNAME, machine $MACHTYPE"
    echo $content
    mail -s "IT3038C Linux IP" $emailaddress <<< $(echo -e $content)


