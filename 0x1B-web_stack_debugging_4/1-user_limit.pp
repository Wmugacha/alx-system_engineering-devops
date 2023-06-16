# Rectify holberton user process limit

exec { 'change-os-configuration-for-holberton-user':
  command => 'ulimit -n 1024',
  user    => 'root',
  creates => '/tmp/holberton_configuration_changed',
  require => File['/etc/security/limits.conf'],
}

# Ensure the limits.conf file exists
file { '/etc/security/limits.conf':
  ensure => present,
}

file_line { 'holberton_limits':
  path    => '/etc/security/limits.conf',
  line    => 'holberton hard nofile 1024',
  require => File['/etc/security/limits.conf'],
}
