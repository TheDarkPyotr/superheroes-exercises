class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key= lambda x:x[0])
        supp = intervals[0]
        count = 0
        for i in range(1,len(intervals)):
            if intervals[i][0] < supp[1]:
                if supp[1] > intervals[i][1]:
                    supp=intervals[i]
                count+=1
                continue
            supp=intervals[i]
        return count