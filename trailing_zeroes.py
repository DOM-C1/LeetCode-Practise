"""Given an integer n, return the number of trailing zeroes in n!."""

"""Note that the zeroes come from either 2*k,5*k"""
import math
def is_multiple_of_2_or_5(num:int)->bool:
    return (num%5==0 or num%2==0) and num%10 != 0
def is_multiple_of_10(num:int)->bool:
    return num%10==0
def main(num:int)-> int:
    count =0
    for number in range(math.factorial(num)):
        if is_multiple_of_2_or_5(number):
            