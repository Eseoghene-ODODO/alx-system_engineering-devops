# Using Puppet, create a manifest that kills a process named killmenow.
exec { 'killmenow':
  command => 'pkill killmenow',
  path    => '/usr/bin:/usr/sbin:/bin:/sbin',
  onlyif  => 'pgrep killmenow',
}
