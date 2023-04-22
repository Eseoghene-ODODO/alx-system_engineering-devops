#!/usr/bin/env bash
# Client configuration file (w/ Puppet)
file { '/home/ubuntu/.ssh/config':
  ensure  => file,
  owner   => 'ubuntu',
  group   => 'ubuntu',
  mode    => '0644',
  content => "
    Host ubuntu@100.25.38.184
      IdentityFile ~/.ssh/school
      PasswordAuthentication no
  ",
}
