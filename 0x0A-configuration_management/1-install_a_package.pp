# This Puppet code installs Flask version 2.1.0 using pip3

package { 'python3-pip':
  ensure => 'present',
}

package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
  virtualenv => 'system',
  owner => 'root',
  require  => Package['python3-pip'],
}
