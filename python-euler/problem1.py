'''
If we list all the natural numbers below 10 that are multiples of 3 or 5, 
we get 3, 5, 6 and 9. The sum of these multiples is 23. Find the sum of 
all the multiples of 3 or 5 below 1000.

==> 233168
'''

'''
Solution using equation S = d * int(x/d) * (1 + int(x/d)) / 2 
where d is the number we're finding multiples of and x is the 
limiting factor to the numbers we are finding subtracted by 1.
'''
def sumNaturalN(n, limit):
    limit -= 1
    return n * int(limit/n) * (1 + int(limit/n)) / 2

'''
Add multiples of 3 and 5 and substract multiples of 15 because 
both mutliples of 3 and multiples of 5 will find all the sets 
of 15. Hence, there are 2 sets of 15 so we need to remove one 
from the answer.
'''
sum = sumNaturalN(3,1000) + sumNaturalN(5,1000) - sumNaturalN(15, 1000)
print sum
