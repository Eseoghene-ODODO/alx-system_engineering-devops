# Using Puppet, create a file in /tmp.e
file { '/tmp/school':
  content => 'I love Puppet',
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0744',
}
