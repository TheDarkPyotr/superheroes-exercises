"""

### Problem locked on Leetcode: https://leetcode.com/problems/meeting-rooms
Description

Given an array of meeting time intervals consisting of start and end times 
[[s1,e1],[s2,e2],…] (si < ei), determine if a 
person could attend all meetings.
Sample I/O
Example 1

        Input: [[0,30],[5,10],[15,20]]
        Output: false

Example 2

        Input: [[7,10],[2,4]]
        Output: true


Solution at --------> https://zhenyu0519.github.io/2020/07/12/lc252/#note
"""

# Sort the list by start time and iterate the sorted list. 
# If the current start time is less than previous end time, 
# then there is conflict and you can not attend all meeting.
def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        new_intervals = sorted(intervals, key=lambda x: x[0])
        for i in range(1,len(new_intervals)):
            if new_intervals[i-1][1] > new_intervals[i][0]:return False
        return True