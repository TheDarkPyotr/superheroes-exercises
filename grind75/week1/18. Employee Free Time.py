"""
Original text: https://aaronice.gitbook.io/lintcode/sweep-line/employee-free-time
Python Solution with test cases: https://github.com/xiaoningning/LeetCode-Python/blob/master/759%20Employee%20Free%20Time.py

Teorical solution: merge all intervals (solving overlap) and the results are the "free time hole" after
merging
"""
from typing import List
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e
    
    def __str__(self, s=0, e=0):
        return "[" + str(self.start) + "] [" + str(self.end) + "]"
        
class Solution:
  def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
    ans = []
    intervals = []
    
    for s in schedule:
      intervals.extend(s)

    #Ordina per tempo di inizio
    intervals.sort(key=lambda x: x[0])

    previousEndTime = intervals[0][1]

    for interval in intervals:
      if interval[0] > previousEndTime:
        ans.append(Interval(previousEndTime, interval[0])) #Free time holes
      previousEndTime = max(previousEndTime, interval[1])

    return ans

case1 = [[[1,2],[5,6]],[[1,3]],[[4,10],[4,2]]]
solution1 = [[3,4]]
sol = Solution()
listing = sol.employeeFreeTime(case1)
if listing == None:
    print("NONE")
else:
    for x in listing:
        print(x)
   