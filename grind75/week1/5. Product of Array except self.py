class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        res = [1 for i in range(n)]
        left,right = nums[0],nums[n-1]

        for i in range(1,n):
            res[i] *= left
            left *= nums[i]

        for i in range(n-2,-1,-1):
            res[i] *= right 
            right *= nums[i]
        return res