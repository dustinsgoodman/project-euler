########Project Euler Toolkit#########
'''
This is a package of commonly used functions for Project Euler.
Functions included:

  gcd(x,y) 
    - find greatest common denominator
    - inputs: two integers
  lcm(x,y) 
    - find least common multiple
    - inputs: two integers

  factor(n) 
    - returns ordered list of factors
    - inputs: value
  primeFactorization(n, primes) 
    - returns list of prime factors
    - inputs: value and list of possible prime values

  isPrime(n) 
    - test if n is a prime number
    - input: integer
  boolSieve(n) 
    - returns a boolean list of primes
    - input: integer
  sieve(n) 
    - finds values of primes from a call to boolSieve
    - input: integer

  sumOfNums(n) 
    - calculates sum of values 1 + 2 + ... + n
    - input: integer
  sumOfSquares(n) 
    - calculates sum of 1^2 + 2^2 + ... + n^2
    - input: integer
  combinations(n, k)
    - based on the combinatorix theory combinations whose formula is n!/[k!(n-k)!]
    - input: two integers

  factorial(n)
    - calculates N! = N*(N-1)*....*3*2*1
    - input: integer
  fib(n)
    - calculate first n fibonacci terms using golden ratio
    - input: integer

  isPalindrome(n)
    - test if string or number is palindrome
    - input: string or integer
  isLeapYear(n)
    - test if year is a leap year
    - input: integer
'''

def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)

def lcm(a,b):
    if a%b == 0:
        return a
    elif b%a == 0:
        return b
    else:
        return a*b / gcd(a,b)


def factor(n):
    facts = [j for i in xrange(1,int(n**.5)+1) if n%i == 0 for j in [i, n/i]]
    facts.sort()
    return facts

def primeFactorization(n, primes):
    nod = 1
    rem = n

    for i in xrange(0, len(primes)+1):
        if primes[i]**2 > n:
            return nod*2
        exp = 1
        while rem%primes[i] == 0:
            exp += 1
            rem /= primes[i]
        nod *= exp
        if rem == 1:
            return nod
    return nod


def isPrime(x):
    if x%2 == 0:
        return False
    for i in xrange(3, int(x**.5)+1, 2):
        if x%i == 0:
            return False
    return True

def boolSieve(n):
    bound = int((n-1)/2)
    primes = [False] * bound
    test_limit = int((n**.5 - 1) / 2)
    for i in xrange(0, test_limit):
        if not primes[i]:
            for j in xrange(i+(3+2*i), bound, 3+2*i):
                primes[j] = True
    return primes

def sieve(n):
    primes = []
    bool_primes = boolSieve(n)
    for i in xrange(0, len(bool_primes)):
        if not bool_primes[i]:
            primes.append(3+2*i)
    return primes


def sumOfNums(n):
    return n*(n+1)/2

def sumOfSquares(n):
    return n*(n+1)*(2*n+1)/6

def combinations(n, k):
    return factorial(n) / (factorial(k)*factorial(n-k))


def factorial(n):
    prod = 1
    for i in xrange(1, n+1):
        prod *= i
    return prod

def fib(n):
    return int(round(((1+5**.5)**n - (1 - 5**.5)**n) / (2**n * 5**.5)))


def isPalindrome(n):
    return str(n) == str(n)[::-1]

def isLeapYear(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False
