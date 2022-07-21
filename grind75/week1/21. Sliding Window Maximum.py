#Problem description: https://leetcode.com/problems/sliding-window-maximum

from gc import collect

from matplotlib import collections


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
    
   
        maximum = nums[0]
        result = []
        sliding = collections.deque()
        counter = 0

            
        for index in range(0,len(nums)):
            
            if index <= k-1:
                #Accodo i primi |k| elementi
                sliding.append(nums[index])
            else:
                #Scorro finestra rimuovendo leftmost   
                sliding.popleft()
                sliding.append(nums[index])
                #e aggiungendo nuovo elemento preso dall'array
             
            #Prendo il massimo incontrato finora 
            maximum = max(maximum, nums[index])
            
            #Se massimo è diverso dall'elemento corrente
            if maximum != nums[index]:
                counter += 1 
            else:
                counter = 0
            #Se ho 
            if counter == k:
                maximum = max(sliding)
                counter = 0
                return index
            
            if index >= k-1:
                result.append(maximum)
                
        return result

def maxSlidingWindow2(self, nums: List[int], k: int) -> List[int]:

    output = []
    q = collections.deque() #we memorize the indexes
    l = r = 0

    while r < len(nums):
        while q and nums[q[-1]] < nums[r]: #q non è vuota e il valore in cima alla coda è minore del corrente 
                q.pop()
        q.append(r) #append the index itself

        #remove the left value from window
        if l > q[0]:
            q.popleft()
        
        #siccome l=r=0, controlliamo che:
        if (r+1) >= k:
            output.append(nums[q[0]])
            l += 1
        
        r += 1
    return output

    
