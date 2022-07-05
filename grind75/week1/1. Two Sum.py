# Problem description: https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
   
        d = {}
        
        for i, n in enumerate(nums):
            print(n)
            m = target - n
            if m in d:
                return [d[m], i]
            else:
                d[n] = i
        
        
      
        
        