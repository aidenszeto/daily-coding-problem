'''
This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
'''

nums = [2,3,1,5,2,7,20,9,4,3]
k = 7

def two_sum(nums, k):
    complements = {}
    for num in nums:
        if ((k - num) in complements):
            print(f"Two sum: {num}, {k - num}")
            exit()
        complements[num] = k - num
    print("No two sum found")