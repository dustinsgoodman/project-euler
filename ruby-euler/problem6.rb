# The sum of the squares of the first ten natural numbers is,

# 1^2 + 2^2 + ... + 10^2 = 385

# The square of the sum of the first ten natural numbers is,

# (1 + 2 + ... + 10)^22 = 55^22 = 3025

# Hence the difference between the sum of the squares of the
# first ten natural numbers and the square of the sum is
# 3025 - 385 = 2640.

# Find the difference between the sum of the squares of the
# first one hundred natural numbers and the square of the sum.

# ==> 25164150

def sum_of_nums(n)
  n * (n + 1) / 2
end

def sum_of_squares(n)
  n * (n + 1) * (2 * n + 1) / 6
end

n = 100
puts sum_of_nums(n) ** 2 - sum_of_squares(n)
