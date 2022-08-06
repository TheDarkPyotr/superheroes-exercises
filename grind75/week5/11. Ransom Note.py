class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        ransomDict = Counter(ransomNote)
        
        for c in magazine:
            if c in ransomDict:
                ransomDict[c] -= 1
                if ransomDict[c] == 0:
                    del ransomDict[c]
        return len(ransomDict) == 0