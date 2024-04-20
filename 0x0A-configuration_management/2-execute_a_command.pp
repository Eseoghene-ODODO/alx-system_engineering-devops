# Using Puppet, create a manifest that kills a process named killmenow.
exec { 'killmenow':
  command => 'pkill -i killmenow',
  onlyif  => 'pgrep -i killmenow',
}
