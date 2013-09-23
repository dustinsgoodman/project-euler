'''
Each new term in the Fibonacci sequence is generated by adding 
the previous two terms. By starting with 1 and 2, the first 10 
terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values 
do not exceed four million, find the sum of the even-valued terms.

==> 4613732
'''

golden_ratio = (1+5**.5)/2
multiplier = golden_ratio**3
fib_val = 2
sum = 0
while fib_val < 4000000:
    sum += fib_val
    fib_val = round(fib_val*multiplier)
print int(sum)