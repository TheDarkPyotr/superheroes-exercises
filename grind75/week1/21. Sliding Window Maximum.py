#Problem description: https://leetcode.com/problems/sliding-window-maximum

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
    
   
        maximum = nums[0]
        result = []
        sliding = collections.deque()
        counter = 0

            
        for index in range(0,len(nums)):
            
            if index <= k-1:
                sliding.append(nums[index])
            else:   
                sliding.popleft()
                sliding.append(nums[index])
            
             
            maximum = max(maximum, nums[index])
            
            if maximum != nums[index]:
                counter += 1
            else:
                counter = 0
            
            if counter == k:
                maximum = max(sliding)
                counter = 0
                return index
            
            if index >= k-1:
                result.append(maximum)
                
        return result
