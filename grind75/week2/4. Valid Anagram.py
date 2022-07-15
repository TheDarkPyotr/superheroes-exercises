class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic = collections.defaultdict(int)
        for x in s:
            dic[x]+=1
        for x in t:
            dic[x]-=1
        for key in dic:
            if dic[key]!=0:
                return False
        return True