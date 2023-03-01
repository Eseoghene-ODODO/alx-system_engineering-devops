#!/usr/bin/env ruby
puts ARGV[0].scan(/\[from:([\w\D]*?)\] \[to:([\w\D]*?)\] \[flags:([\w\D]*?)\]/).join(",")
