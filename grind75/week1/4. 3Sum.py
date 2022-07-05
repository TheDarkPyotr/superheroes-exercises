# Problem description:   https://leetcode.com/problems/3sum/

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
                
        res_list = []
        
        nums.sort()
        
        for index, n in enumerate(nums):
            if n == nums[index-1] and index > 0:
                continue
            else:
                left = index+1
                right = len(nums)-1
                
                while left < right:
                    current = n + nums[left] + nums[right]
                    if current == 0:
                        res_list.append([n,nums[left], nums[right]])
                        
                    if current > 0:
                        right -= 1
                    else:
                        left += 1
        return res_list
                    
            
                              