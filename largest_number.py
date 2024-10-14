
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



def create_max_num(numbers1:list) -> str:
    index = 1
    max_num = ''

    while numbers1:
        num1 = get_next_largest_digit(numbers1,1)
        num2 = get_next_largest_digit(numbers1,2)
        
    
        if num1 and num2:
            print(num2)
            if int(num2[0][2]) > int(num2[0][1]): 
                numbers1 = [num for num in numbers1 if str(num) not in num2]
                max_num+="".join(num2)
            else:
                numbers1 = [num for num in numbers1 if str(num) not in num1]
                max_num+="".join(num1)
        elif num1:
            print(num1)
            numbers1 = [num for num in numbers1 if str(num) not in num1]
            max_num+="".join(num1)
        elif num2:
            numbers1 = [num for num in numbers1 if str(num) not in num2]
            max_num+="".join(num2)
    
        # if index == 1:
        #     next_largest_digit = get_next_largest_digit(numbers1,index)
        #     max_num+="".join(next_largest_digit)
        #     numbers1 = [num for num in numbers1 if str(num) not in next_largest_digit]
        #     index +=1
        # else:
        #     next_largest_digit = get_next_largest_digit(numbers1,index)
    
        #     max_num+="".join(next_largest_digit)
        #     numbers1 = [num for num in numbers1 if str(num) not in next_largest_digit] 
          
        #     index=1
    return max_num


   


def get_next_largest_digit(nums: list,index:int) -> list:
    highest_first_digit = [int(str(num)[index]) for num in nums if index == (len(str(num)) -1)]
    if highest_first_digit:
        highest_first_digit = max(highest_first_digit)
        nums= sorted([num for num in nums if int(str(num)[index]) == highest_first_digit],reverse=True)
        return [str(num) for num in nums]
    return []
   
def main(nums:list) -> int:
    l_num = ''
    while nums:
       numbers = get_next_largest_digit(nums,0 )
       nums = [num for num in nums if str(num) not in numbers] 
       l_num += create_max_num(numbers)
     
    return l_num

print(main([3,30,34,5,9]))
       


