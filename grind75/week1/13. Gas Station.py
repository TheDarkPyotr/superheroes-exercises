# Problem description: https://leetcode.com/problems/gas-station/

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        if sum(gas) < sum(cost):
            return -1
        
        
        tot = 0
        res = 0
        
        for i in range(len(gas)):
            somma = gas[i] - cost[i]
            tot += somma
            if tot < 0:
                tot = 0
                res = i+1
            
        return res
        
      
        
        