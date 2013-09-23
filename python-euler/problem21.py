'''
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a  b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.

==> 31626
'''

def d(n):
    return 1 + sum([i for i in xrange(2,int(n/2+1)) if n%i==0])

sum_of_factors = [(i,d(i)) for i in xrange(1,10000)]
answer = 0
for i in sum_of_factors:
    if i[1] < 10000 and sum_of_factors[i[1]-1][1] == i[0] and i[0] != i[1]:
        answer += i[0]

print answer





