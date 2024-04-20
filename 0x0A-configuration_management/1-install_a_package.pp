# This Puppet code installs Flask version 2.1.0 using pip3

package { 'python3-pip':
  ensure => 'present',
}

python::pip { 'flask':
  ensure     => 'present',
  pkgname    => 'flask',
  version    => '2.1.0',
  require    => Package['python3-pip'],
}
