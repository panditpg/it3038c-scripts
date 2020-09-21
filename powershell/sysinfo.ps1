function getIP {
    (Get-NetIPAddress -InterfaceAlias Ethernet0).ipv4address
}

$IP = getIP

$Body = "This machine's IP is {0}." -f $IP

write-host($Body)


$Body += "User is {0}." -f $env:USERNAME
Write-Host($Body)

$HOSTNAME = "panditpg-win"
$Body += "Hostname is {0}." -f $HOSTNAME
Write-Host($Body)

$Body += "PowerShell Version is {0}." -f $HOST.Version.Major
Write-Host($Body)


$Date = Get-Date -UFormat "%A, %B %d, %Y"
$Body += "Today's date is {0}." -f $Date
write-host($Body)

#Send-MailMessage -To "botheaj@ucmail.uc.edu" -From "panditpg@mail.uc.edu" -Subject "IT3038C Windows Sysinfo" -Body $Body -SmtpServer "Smtp.office365.com" -port 587 -UseSsl -Credential (Get-Credential)
Send-MailMessage -To "prayag13@gmail.com" -From "prayag13@gmail.com" -Subject "IT3038C Windows Sysinfo" -Body $Body -SmtpServer "Smtp.gmail.com" -port 587 -UseSsl -Credential (Get-Credential)