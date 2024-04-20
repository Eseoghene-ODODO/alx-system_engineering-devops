# This Puppet code installs Flask version 2.1.0 using pip3

package { 'python3-pip':
  ensure => 'present',
}

python::pip { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
  require  => Package['python3-pip'],
}
