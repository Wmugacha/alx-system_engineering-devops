# Rectify holberton user process limit

file_line { 'holberton_limits':
  ensure => present,
  path   => '/etc/security/limits.conf',
  line   => ['holberton hard nofile 4096', 'holberton soft nofile 4096'],
  match  => '^holberton',
}
