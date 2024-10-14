"""
LeetCode Easy
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 """

""" Plan: instead of doing every combinbation of digits in nums we will find every way to sum a number, which for even n will be 
a tuple of (0,n), (1,n-1), (2,n-2) ... (n/2,n/2). After which the .index method in python makes light work of the remaining work.


Functions:
find_every_every_two_sum: takes a list and returns a tuple of every possible way to sum two digits to make a particular number.
main function: loops through whatever above function and check."""

def find_every_two_sum(number:int) -> list[tuple]:
    """This function finds every two sum."""
    i = 0
    two_sums=[]
    while i <= (number//2):
        two_sums.append((i,number -i))
        i+=1
    return two_sums


def main(nums:list, number: int) -> list[int,int]:
    every_two_sum = find_every_two_sum(number)
    for num1,num2 in every_two_sum:
        if num1 and num2 in nums:
            return [nums.index(num1),nums.index(num2)]
        
print(main([1,3,4],7))