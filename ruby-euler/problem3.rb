# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143?

# ==> 6857

def factor(n)
  range = (1..((n**0.5)+1)).to_a
  range.select { |i| n % i == 0 }.map { |i| [i, n/i] }.flatten.sort
end

def prime?(num)
  return false if num % 2 == 0
  range = (3..((num**0.5)+1).to_i).step(2).to_a
  return false if range.any? { |i| num % i == 0 }
  true
end

largest_prime = factor(600851475143).select { |f| prime?(f) }.max
puts largest_prime
