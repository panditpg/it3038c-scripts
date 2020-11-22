function getIP {
    (Get-NetIPAddress -InterfaceAlias Ethernet0).ipv4address
}
function sayhello {
    Write-Host("Hello, user!")
}