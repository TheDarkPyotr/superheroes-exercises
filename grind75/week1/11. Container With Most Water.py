#Problem description: https://leetcode.com/problems/container-with-most-water/
class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        left = 0
        right = len(height) - 1
        res = 0 

        """
                
        for outer_i, element in enumerate(height):
            inner_i = outer_i + 1
            for inner_i in range(len(height)):
                
                temp = (inner_i - outer_i)*min(height[inner_i], height[outer_i])
                if  temp > res:
                    res = temp
        return res
      
    
    
        while left < right:
            
            if height[left] < height[right]:
                temp =  (right-left)*height[left]
                left += 1
            else:
                temp =  (right-left)*height[right]
                right -= 1
                
            if temp > res:
                res = temp
        return res
      """
   
    def maxArea(self, H: List[int]) -> int:
        ans, i, j = 0, 0, len(H)-1
        while (i < j):
            if H[i] <= H[j]:
                res = H[i] * (j - i)
                i += 1
            else:
                res = H[j] * (j - i)
                j -= 1
            if res > ans: ans = res
        return ans

                
                
           
        