$Machines = 'panditpg-win'

#foreach ($machine in $Machines) {
#   $RCounters = Get-Counter -ListSet = -ComputerName $machine
#   write-host("There are {0} counters on {1}" -f $RCounters.count, $machine)
#}

foreach ($machine in $Machines) {
    $pt = (Get-Counter -Counter "\Processor(_Total)\% Processor Time" -SampleInterval 1 -MaxSamples 10).CounterSamples.CookedValue
    $sample = 1
    foreach ($p in $pt) {
        "Sample {2}: CPU is at {0}% on {1}" -f [int]$p, $machine, $sample | Out-File -Append C:\logs\cpu.log
        $sample++
    }
}