from itertools import permutations
"""
LeetCode Medium
Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.

Since the result may be very large, so you need to return a string instead of an integer.

 

Example 1:

Input: nums = [10,2]
Output: "210"
Example 2:

Input: nums = [3,30,34,5,9]
Output: "9534330"
 

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 109"""

# plan: 
# we can beat the naive approach of creating all n! combinations by observing for small k, and reasonable n:  sum(k!) << n!
# we look through nums to find the elements with the highest first digit i.e. if we have [3,5,9,99,91] then we pick out the numbers 9, 99 and 91.
# we then create all 3! numbers and pick the largest, and repeat this process until completion. note that for any particular iteration:
# there will be at most 21 factorial cases which is quite a lot but this process willl be refined once we have the rough version working.

# functions: 
# create_all_numbers, creates all possible numbers for a list of digits. (to be amended)
# get next_largest_first_digits, given a list, find all the numbers with highest first digit, remove them from the list and move them to another a list.



def create_max_num(numbers:list) -> str:
    return str(max([int(''.join(map(str,permutation))) for permutation in permutations(numbers)]))

def get_next_largest_digit(nums: list,first_digits:list) -> list:
    highest_first_digit = max([int(str(num)[0]) for num in nums])
    return [num for num in nums if int(str(num)[0]) == highest_first_digit]
   
def main(nums:list) -> int:
    all_first_digits = [str(num)[0] for num in nums]
    l_num = ''
    while nums:
       numbers = get_next_largest_digit(nums,all_first_digits)
       nums = [num for num in nums if int(num) not in numbers] 
       l_num += create_max_num(numbers)
     
       

    return l_num

print(main([3,30,34,5,9]))
       


