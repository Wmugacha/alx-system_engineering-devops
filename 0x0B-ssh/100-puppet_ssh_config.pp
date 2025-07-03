# Puppet script to create ssh config file
file { '/etc/ssh/ssh_config':
  ensure  => 'file',
  owner   => 'root',
  group   => 'root',
  mode    => '0644',
  content => @(SSHCONFIG),
# Global SSH client settings
Host alx
    HostName 98.98.98.98
    User ubuntu
    IdentityFile ~/.ssh/school
    PreferredAuthentications publickey
    PasswordAuthentication no
| SSHCONFIG
}
