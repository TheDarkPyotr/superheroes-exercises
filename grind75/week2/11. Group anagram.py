class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for x in strs:
            count = [0] * 26
            for v in x:
                count[ord(v) - ord('a')] += 1   #uso di array delle occorrenze come chiave attraverso tupla
            res[tuple(count)].append(x)
        return res.values()