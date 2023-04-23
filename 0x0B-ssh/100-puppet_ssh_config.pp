#!/usr/bin/env ruby
# Client configuration file (w/ Puppet)
require 'net/ssh'

ssh_key = File.read("#{ENV['HOME']}/.ssh/school")
ssh_host = '100.25.201.12'
ssh_user = 'ubuntu'

Net::SSH.start(ssh_host, ssh_user, keys: [ssh_key]) do |ssh|
  # do something over SSH connection
end
