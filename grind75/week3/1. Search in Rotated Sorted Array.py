class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        n = len(nums)
        left = 0
        right = n-1
        
        if n == 0:
            return -1
        
        while left <= right:
            
            ##Prendo la metà
            mid = left + (right-left) // 2
            
            #Se raggiunto il target, finito
            if nums[mid] == target:
                return mid
            ## Se centro >= sx allora [sx:centro] crescente, flessione starà da [centro+1:n] 
            if nums[mid] >= nums[left]:
                
                #Poiché da [sx:centro] crescente, controllo se target è nel range
                if nums[left] <= target < nums[mid]:
                    right = mid - 1 #circoscrivo array a [sx, mid-1]
                else:
                    left = mid + 1 #circoscrivo array a [mid+1, dx]
                    
            #Se centro < sx allora [centro:dx] crescente, flessione è in [sx:centro]        
            elif nums[mid] < nums[left]: 
                
                #Poiché [centro:dx] crescente, controllo se target è nel range
                if nums[mid] < target <= nums[right]:
                    left = mid+1 #allora circoscrivo array a [mid+1,dx]
                else:
                    right = mid - 1 #circoscrivo array a [sx,mid-1]
        
        return -1