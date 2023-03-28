file { 'school':
    ensure  => 'present',
    path    => '/tmp/school',
    owner   => 'www-data',
    group   => 'www-data',
    mode    => '0644',
    content => 'I love Puppet'
}
