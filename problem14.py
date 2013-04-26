'''
The following iterative sequence is defined for the set of positive integers:

n = n/2 (n is even)
n = 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.

==> 837799
'''

counts = {1:1}
def sequencer(n):
    global counts
    if not counts.get(n,0):
        if n%2 == 0:
            counts[n] = 1 + sequencer(n/2)
        else:
            counts[n] = 1 + sequencer((3*n + 1)/2)
    return counts[n]

max_count = start_val = curr_count = 0
for i in xrange(999999, 500000, -2):
    curr_count = sequencer(i)
    if curr_count > max_count:
        max_count = curr_count
        start_val = i

print start_val
