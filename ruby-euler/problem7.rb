# By listing the first six prime numbers:
# 2, 3, 5, 7, 11, and 13, we can see that the
# 6th prime is 13.
#
# What is the 10,001st prime number?
#
# ==> 104743

def prime?(num)
  return false if num % 2 == 0
  range = (3..((num**0.5)+1).to_i).step(2).to_a
  return false if range.any? { |i| num % i == 0 }
  true
end

count = 1
i = 3
while true do
  count += 1 if prime?(i)
  break if count == 10001
  i += 2
end
puts i
