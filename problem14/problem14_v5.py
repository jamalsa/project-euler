# Project Euler : Problem 14 version 5
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


Result
--------
- result : correct
- time   : 0m5.833s

'''

def problem14v5():
    chain_length = {}
    max_length = 1
    max_number = 1

    for i in range(1, 1000000):
        n = i
        length = 1
        while n > 1:
            if chain_length.has_key(n):
                length += chain_length[n]
                break
            elif n%2 == 0 :
                n = n/2
            else :
                n = 3 * n + 1
            length += 1

        chain_length[i] = length
        
        if length > max_length:
            max_length = length
            max_number = i

    return (max_length, max_number)



if __name__ == "__main__":
    print problem14v5()


