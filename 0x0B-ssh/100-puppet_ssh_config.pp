#!/usr/bin/env ruby
# Client configuration file (w/ Puppet)

file { '/home/root/.ssh/config':
  ensure  => file,
  owner   => 'root,
  group   => root',
  mode    => '0644',
  content => "
    Host 35.175.132.186
      IdentityFile ~/.ssh/school
      PasswordAuthentication no
  ",
}
