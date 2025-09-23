# kills a process named killmenow

exec{'kills_a_process_named_killmenow':
    command  => '/bin/pkill killmenow',
    path     => ['/bin', '/usr/bin'],
    provider => 'shell',
    onlyif   => '/bin/pgrep killmenow',
}
