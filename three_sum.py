"""
LeetCode Medium
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that 
i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
 

Constraints:

3 <= nums.length <= 3000
-105 <= nums[i] <= 105"""

"""Plan: 
we can find every three sums that happens in the range |105| which is 211^3 operations. This is better than 3000^3 
operations which would happen if we tried every combination of three numbers in nums.

functions: find_every_three_sum, main"""


def find_every_three_sum() -> list:
    three_sums = [[0,0,0]]
    for i in range(-105,106):
        for j in range(-105,106):
            for k in range(-105,106):
                if i+j+k == 0 and i != j and j != k and i != k:
                    three_sums.append(set([i,j,k]))
    return three_sums
def main(nums:list):
    three_sum = []
    every_three_sum = find_every_three_sum()
    for num1,num2,num3 in every_three_sum:
        if num1 in nums and num2 in nums and num3 in nums:
            three_sum.append([num1,num2,num3])
    return three_sum



