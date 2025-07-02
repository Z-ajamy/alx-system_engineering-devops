# This manifest uses the pkill command to kill a process named 'killmenow'

exec { 'kill-killmenow-process':
  command => 'pkill killmenow',
  path    => ['/usr/bin', '/bin'],
}