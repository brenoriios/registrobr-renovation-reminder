$delay = New-TimeSpan -Minutes 3
$action = New-ScheduledTaskAction -Execute 'python.exe' -Argument $pwd"\domainReminder.py"
$trigger = New-ScheduledTaskTrigger -AtLogOn
$trigger.Delay = 'PT3M'
$task = Register-ScheduledTask -Action $action -Trigger $trigger -TaskName "TestTask" -Description "Verifica a renovação dos domínios na inicialização do sistema"