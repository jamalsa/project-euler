# Project Euler : Problem 14 version 3
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
- time   : 1m9.553s

'''

def problem14v3():
    tmp_list = [sequence(number) for number in range(1, 1000000)]
    tmp_list.sort()
    return tmp_list[-1]

def sequence(number):
    n = number
    length = 1
    while n > 1:
        if n%2 == 0 :
            n = n/2
        else :
            n = 3 * n + 1
        length += 1

    return (length, number)


if __name__ == "__main__":
    print problem14v3()



