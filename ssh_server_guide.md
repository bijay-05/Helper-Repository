## Checking status of ssh in ubuntu
$ps aux | grep ssh

## using telent to the SSH port
$telnet localhost 22

## SSH service status
$ sudo systemctl status sshd
$ service sshd status

## Stopping SSH
$sudo systemctl stop sshd
$sudo service sshd stop

## Starting SSH
$sudo systemctl start sshd
$sudo service sshd start

## Enabling and disabling SSH
$sudo systemctl disable sshd
$sudo systemctl enable sshd
