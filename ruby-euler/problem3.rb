# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143?

# ==> 6857

require './toolkit'
include Toolkit

def factor(n)
  range = (1..((n**0.5)+1)).to_a
  range.select { |i| n % i == 0 }.map { |i| [i, n/i] }.flatten.sort
end

largest_prime = factor(600851475143).select { |f| prime?(f) }.max
puts largest_prime
