class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hashmap = {}
        for value in nums:
            if hashmap.has_key(value):
                hashmap[value]+=1
            else:
                hashmap[value]=1
        max_key = max(hashmap, key=hashmap.get)
        return max_key