
"""
Original text: https://aaronice.gitbook.io/lintcode/sweep-line/meeting-rooms-ii
Python Solution (no test cases): https://zhenyu0519.github.io/2020/07/13/lc253/

We use min heap. First we sort the intervals then iterate the intervals, 
for each interval, if the start time is greater or equal than the heap[0] we will 
pop from heap and push the interval’s end time into heap. Otherwise, we will just push the interval’s 
end time into heap. Finally, the result will be the size of heap.

"""
from heapq import heapify, heappush, heappop

def minMeetingRooms(intervals) -> int:
    size = len(intervals)
    if size <= 1:
        return size
    
    heap = []
    sorted_intervals = sorted(intervals)
    min_heap = heapify(heap)
    heappush(heap, sorted_intervals[0][1])

    for interval in sorted_intervals[1:]:
        if interval[0] >= heap[0]:
            heappop(heap)
            heappush(heap, interval[1])
        else:
            heappush(heap, interval[1])

    return len(heap)

print(minMeetingRooms([[0, 30],[5, 10],[15, 20]]))
