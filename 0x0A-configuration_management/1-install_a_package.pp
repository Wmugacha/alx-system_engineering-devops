# Puppet manifest to install Flask from pip3

exec { 'pip3':
    command => '/usr/bin/sudo apt-get -y install python3-pip'
}

exec { 'flask':
    command => '/usr/bin/pip3 install Flask',
    require => Exec['pip3']
}
