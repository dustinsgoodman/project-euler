'''
A Pythagorean triplet is a set of three natural numbers, a  b  c, for which,

a**2 + b**2 = c**2
For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

==> 31875000
'''

def prob9(sum):
    for a in xrange(1, sum):
        for b in xrange(a+1, 1000):
            c = (a**2 + b**2)**.5
            if c%1 == 0 and a+b+c == 1000:
                return int(a*b*c)

print prob9(1000)
                
            
