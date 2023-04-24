#!/usr/bin/env ruby
# Client configuration file (w/ Puppet)

file { '/root/.ssh/config':
  ensure  => 'present',
  owner   => 'root',
  group   => 'root',
  mode    => '0600',
  content => "
    Host 35.175.132.186
      IdentityFile ~/.ssh/school
      PasswordAuthentication no
  ",
}
