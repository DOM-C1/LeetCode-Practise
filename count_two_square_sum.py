"""
Leetcode Medium
Given an integer n, return the least number of perfect square numbers that sum to n.

A perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself.
 For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not"""

def get_all_squares_less_than_n(n:int)->list:
    return [num**2 for num in range(int(n**(1/2))+1)]

print(get_all_squares_less_than_n(16))
            