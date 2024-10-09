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


# functions: 
# create_max_num creates the maximum number.
# get next_largest_first_digits, given a list, find all the numbers with highest first digit, remove them from the list and move them to another a list.



def create_max_num(numbers:list) -> str:
    numbers = [str(num) for num in numbers]
    one_digit_num = [str(num) for num in sorted([int(num) for num in numbers if len(num) == 1],reverse=True)]
    two_digit_num = [str(num) for num in sorted([int(num) for num in numbers if len(num) == 2],reverse=True)]
    three_digit_num = [str(num) for num in sorted([int(num) for num in numbers if len(num) == 3],reverse=True)]
    print(one_digit_num+two_digit_num+three_digit_num)
    return "".join(one_digit_num+two_digit_num+three_digit_num)


def get_next_largest_digit(nums: list) -> list:
    highest_first_digit = max([int(str(num)[0]) for num in nums])
    return [num for num in nums if int(str(num)[0]) == highest_first_digit]
   
def main(nums:list) -> int:
    l_num = ''
    while nums:
       numbers = get_next_largest_digit(nums)
       nums = [num for num in nums if int(num) not in numbers] 
       l_num += create_max_num(numbers)
     
    return l_num

print(main([3,30,34,5,9]))
       


