# Puppet manifest to install Flask from pip3

exec { 'pip3':
    command => '/usr/bin/sudo apt-get -y install python3-pip'
}

package { 'flask':
    ensure   => '2.1.0',
    name     => 'flask',
    provider => 'pip3',
    require  => Exec['pip3']
}
