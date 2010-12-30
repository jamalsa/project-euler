# Project Euler : Problem 14 version 1
# (http://projecteuler.net/index.php?section=problems&id=14)
'''
Problem
--------

The following iterative sequence is defined for the set of positive integers:

    n -> n/2 (n is even)
    n -> 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

    13 -> 40 ->  20 ->  10 ->  5 ->  16 ->  8 ->  4 ->  2 -> 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 
10 terms. Although it has not been proved yet (Collatz Problem), it is thought 
that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.


Solution 
---------

1. Create function to generate list of sequence from given number
2. Create function to Call sequence generator for any number below 1000000, find
length of each sequence, sort it, and return number which produces the longest
chain.


Result
--------
- result : correct
- time   : 1m24.875s

'''

def problem14():
    chain_length = {}

    for i in range(1,1000000):
        chain_length[i] = len(generate_sequence(i))

    sorted_chain = sorted(chain_length.iteritems(), key = itemgetter(1),
                         reverse = True)

    return sorted_chain[0]


def generate_sequence(n):
    result = [n]
    while n > 1:
        if n%2 == 0 :
            n = n/2
        else :
            n = 3 * n + 1
        
        result.append(n)

    return result

if __name__ == "__main__":
    print problem14()

