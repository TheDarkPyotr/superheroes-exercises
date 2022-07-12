#Problem description: https://leetcode.com/problems/squares-of-a-sorted-array/submissions/
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        
        n = len(nums)
        mid = n // 2 
        if n == 1:
            return [nums[mid]**2]
        elif n == 2:
            if abs(nums[0]) > abs(nums[1]):
                return [nums[1]**2, nums[0]**2]
            else: 
                return [nums[0]**2, nums[1]**2]
        
        
        left = mid-1
        right = mid+1
        result = []
        mid_flag = False
        #result.append(nums[mid]**2)
        
        while left >= 0 and right < n:
            
            if abs(nums[mid]) <= abs(nums[left]) and abs(nums[mid]) <= abs(nums[right]) and mid_flag is False:
                result.append(nums[mid]**2)
                mid_flag = True

            
            if abs(nums[left]) < abs(nums[right]):
                result.append(nums[left]**2)
                left -= 1
            else:
                result.append(nums[right]**2)
                right += 1
                
        while left >= 0:
            if abs(nums[mid]) <= abs(nums[left]) and mid_flag is False:
                result.append(nums[mid]**2)
                mid_flag = True

            result.append(nums[left]**2)
            left -= 1
            
        while right < n:
            if abs(nums[mid]) <= abs(nums[right]) and mid_flag is False:
                result.append(nums[mid]**2)
                mid_flag = True

            result.append(nums[right]**2)
            right += 1
            
            
            
        
        return result
        
            
            
            
            
        