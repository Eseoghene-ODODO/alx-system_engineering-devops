# This Puppet code installs Flask version 2.1.0 using pip3

package { 'python3-pip':
  ensure => 'installed',
}

exec { 'install-flask':
  command => 'pip3 install flask==2.1.0',
  provider => 'pip3',
  path => ['/usr/bin'],
  require  => Package['python3-pip'],
}
