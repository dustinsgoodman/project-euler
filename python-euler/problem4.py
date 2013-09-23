'''
A palindromic number reads the same both ways. The 
largest palindrome made from the product of two 2-digit 
numbers is 9009 = 91 99.

Find the largest palindrome made from the product of two 
3-digit numbers.

==> 906609
'''
from toolkit import isPalindrome

max_palindrome = 0
min = 100
max = 999
res = 0
for i in xrange(max, min-1, -1):
    for j in xrange(i-1, min-1, -1):
       res = i*j
       if isPalindrome(res) and res > max_palindrome:
            max_palindrome = res
print max_palindrome
