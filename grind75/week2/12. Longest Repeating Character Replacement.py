class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # sempre sliding window
        start = 0
        r = 0
        dic_ = {}
        res = 0
        while r < len(s):
            dic_[s[r]] = 1 + dic_.get(s[r], 0)

            while (r - start + 1) - max(dic_.values()) > k:
                dic_[s[start]] -= 1
                start += 1
            res = max(res, r - start + 1)
            r += 1
        return res