# it3038c-scripts
Javascript code block

Hello

It's me, a Networking student!

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


Lab 3

function getIP{
    (Get-NetIPAddress -InterfaceAlias Ethernet0).ipv4address
    
}
$IP = getIP

$Body = "This machine's IP is {0}." -f $IP
write-host($Body)

$Body += "User is {0}." -f $env:USERNAME
write-host($Body)



$HOSTNAME = "panditpg-win"
$Body += "Hostname is {0}." -f $HOSTNAME
write-host($Body)

$Body += "PowerShell Version is {0}." -f $HOST.Version.Major
write-host($Body)

$Date = Get-Date -UFormat "%A, %B, %d, %Y"
$Body += "Today's date is {0}." -f $Date
write-host($Body)

Send-MailMessage -To "prayag13@gmail.com" -From "prayag13@gmail.com" -Subject "IT3038C Windows Sysinfo" -Body $Body -SmtpServer "Smtp.gmail.com" -port 587 -UseSsl -Credential (Get-Credential)



import datetime
now = datetime.datetime.now()
print ("Current date and time : ")
print (now.strftime("%Y-%m-%d %H:%M:%S))


using System;
using System.Speech.Synthesis;
namespace FirstSynthesis
{
    class program
    {
        static void Main(string[] args)
        {
            // This line will initialize a new instance of the SpeechSynthesizer.
            SpeechSynthesizer synth = new SpeechSynthesizer();

            // This line will configure the audio output.
            synth.SetOutputToDefaultAudioDevice();

            // Speak a string.
            synth.Speak(This code demonstrates a basic use of Speech Synthesizer");
            Console.WriteLine();
            Console.WriteLine("This line of code will press any key to exit...");
            Console.ReadKey();
        }
    }
}
