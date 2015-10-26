# A palindromic number reads the same both ways. The
# largest palindrome made from the product of two 2-digit
# numbers is 9009 = 91 99.
#
# Find the largest palindrome made from the product of two
# 3-digit numbers.
#
# ==> 906609

require './toolkit'
include Toolkit

def palindrome?(val)
  val.to_s == val.to_s.reverse
end

max_palindrome = 0
min = 100
max = 999
res = 0

range_generator(min-1, max, true).each do |i|
  range_generator(min-1, i-1, true).each do |j|
    res = i * j
    max_palindrome = res if palindrome?(res) && res > max_palindrome
  end
end

puts max_palindrome
