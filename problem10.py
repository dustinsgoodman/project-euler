'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

==> 142913828922
'''
from toolkit import *

n = 2000000
primes = sieve(n)
prime_sum = 2 + sum(primes)

print prime_sum
