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
            