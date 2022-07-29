# Problem description: https://leetcode.com/problems/move-zeroes/

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        zeroes = nums.count(0)
        for k in range(zeroes):
            nums.remove(0)
            
        array = [0]*zeroes
        return nums.extend(array)

"""

# in-place
def moveZeroes(self, nums):
    zero = 0  # records the position of "0"
    for i in xrange(len(nums)):
        if nums[i] != 0:
            nums[i], nums[zero] = nums[zero], nums[i]
            zero += 1

"""
            