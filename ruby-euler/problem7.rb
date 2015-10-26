# By listing the first six prime numbers:
# 2, 3, 5, 7, 11, and 13, we can see that the
# 6th prime is 13.
#
# What is the 10,001st prime number?
#
# ==> 104743

require './toolkit'
include Toolkit

count = 1
i = 3
while true do
  count += 1 if prime?(i)
  break if count == 10001
  i += 2
end
puts i
