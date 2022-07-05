# Problem description: https://leetcode.com/problems/insert-interval/

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        min_limit = 0
        result_list = [] 
        overlap_min = newInterval[0]
        overlap_max = newInterval[1]
        
        
        for index in range(len(intervals)):
            
            if newInterval[0] > intervals[index][1]:
                result_list.append(intervals[index])
                
            elif newInterval[1] < intervals[index][0]:
                result_list.append([overlap_min, overlap_max])
                return result_list + intervals[index:]
                
                
            else:
                overlap_min = min(intervals[index][0], newInterval[0])
                overlap_max = max(intervals[index][1], newInterval[1])
        
                
                
                
                
                