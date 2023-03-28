# Puppet manifest to kill a process.

exec { 'killprocess':
    command => '/usr/bin/pkill killmenow'
}
