"""
Quiz Problem 6

Write a recursive Python function, given a non-negative integer N, to
calculate and return the sum of its digits.

Hint: Mod (%) by 10 gives you the rightmost digit (126 % 10 is 6), 
while doing integer division by 10 removes the rightmost digit 
(126 / 10 is 12).

This function has to be recursive; you may not use loops!

This function takes in one integer and returns one integer.
"""

def sumDigits(N):
    if type(N) != int or N < 0:
        raise ValueError
    if N == 0:
        return 0
    return N % 10 + sumDigits(N / 10)
