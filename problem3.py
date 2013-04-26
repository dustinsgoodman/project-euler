'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?

==> 6857
'''
from toolkit import *

factors = factor(600851475143)
max = 0
for factor in factors:
    if isPrime(factor) and factor > max:
        max = factor

print max

