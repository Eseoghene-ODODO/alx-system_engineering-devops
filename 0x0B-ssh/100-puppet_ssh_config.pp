#!/usr/bin/env bash
# Client configuration file (w/ Puppet)
file { '/home/<your-username>/.ssh/config':
  ensure  => file,
  owner   => '<your-username>',
  group   => '<your-group>',
  mode    => '0644',
  content => "
    Host <server-ip-address>
      IdentityFile ~/.ssh/school
      PasswordAuthentication no
  ",
}
