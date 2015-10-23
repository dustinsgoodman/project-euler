# 2520 is the smallest number that can be divided
# by each of the numbers from 1 to 10 without any
# remainder.
#
# What is the smallest positive number that is
# evenly divisible by all of the numbers from 1
# to 20?
#
# ==> 232792560

def gcd(a, b)
  return a if b == 0
  gcd(b, a % b)
end

def lcm(a, b)
  return a if a % b == 0
  return b if b % a == 0
  a * b / gcd(a, b)
end

div = 1
(2..21).to_a.each { |i| div = lcm(i, div) }
puts div
