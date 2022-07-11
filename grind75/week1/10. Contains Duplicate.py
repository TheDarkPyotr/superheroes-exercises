# Problem description: https://leetcode.com/problems/contains-duplicate/

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        #Alternative and simple solution:
        #return len(set(nums)) != len(nums)
    
        counter = dict()
        for num in nums:
            if num in counter:
                return True
            else:
                counter[num] = 1
        return False       
        
       
        