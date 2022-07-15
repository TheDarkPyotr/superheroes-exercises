class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        m_len = 0
        limit=len(s)
        start = 0
        end = 0
        for i in range( len(s)):
            l,r = i,i
            while l>=0 and r< limit and s[l]==s[r]:
                tmp=r-l+1
                if tmp > m_len:
                    start = l
                    end = r+1
                    m_len=tmp
                l-=1
                r+=1
            l,r = i,i+1
            while l>=0 and r< limit and s[l]==s[r]:
                tmp=r-l+1
                if tmp > m_len:
                    start = l
                    end = r+1
                    m_len=tmp
                l-=1
                r+=1
        return s[start:end]