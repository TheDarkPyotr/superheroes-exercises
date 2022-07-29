   
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        if not any(map(bool, nums)):
            return '0'
        
        nums = list(map(str, nums)) # LIst[string]
        print(nums)

        if len(nums) < 2:
            return "".join(nums)
        
        def compare(x, y):
            return (int(nums[x]+nums[y])) > (int(nums[y]+nums[x]))
        print(nums)
        
        for x in range(len(nums) - 1):
            y = x + 1
            print(y)
            while x < len(nums) and y < (len(nums)):
                if not compare(x,y):
                    nums[y], nums[x] = nums[x], nums[y]
                y+=1

        return "".join(nums)   


class Wrapper:
    def __init__(self, val):
        self.val = str(val)
        
    def __lt__(self, other):
        return int(self.val+other.val) < int(other.val+self.val)

    
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = [Wrapper(n) for n in nums]
  
        nums.sort(reverse=True)
        

    
        nums = [n.val for n in nums]
    
        
        return str(int(''.join(nums)))