"""Given an integer n, return the number of trailing zeroes in n!."""


import math
def count_zeroes(num:int)->int:
    count =0
    # NAIVE APPROACH
    num = str(math.factorial(num))
    for char in num[::-1]:
        if char != '0':
            return count
        count += 1
    return count

def count_zeroes2(num:int)->int:

    multiples = {5:0,2:0,10:0}

    for i in range(2,num+1):
        if i %2 == 0 and i%5 != 0:
            multiples[2] += 1
        if i%5 == 0 and i%2 != 0:
            k=i
            while k%5 == 0:
                multiples[5] += 1
                k /= 5
        
           
        if i%10 == 0:
            k=i
            while k%10 ==0:
                multiples[10] += 1
                k /= 10
   
            
    return min(multiples[2],multiples[5]) + multiples[10]
  