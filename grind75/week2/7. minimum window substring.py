class Solution:
    def minWindow(self, s: str, t: str) -> str:
        start = 0
        r = 0
        limit = len(s)
        dic_t = Counter(t)
        dic_s = collections.defaultdict(int)
        lenght = len(dic_t)
        valido = True
        res = (float('inf'), 0, 0)
        while r < limit:
            if s[r] in dic_t:
                dic_s[s[r]] += 1

            valido = True
            if len(dic_s) == lenght:
                for k in dic_s:
                    if dic_s[k] < dic_t[k]:
                        valido = False
            else:
                valido = False

            while start <= r and valido is True:
                if r - start + 1 < res[0]:
                    res = (r - start + 1, start, r)
                if s[start] in dic_t:
                    dic_s[s[start]] -= 1
                start += 1
                for k in dic_s:
                    if dic_s[k] < dic_t[k]:
                        valido = False

            r += 1
        return "" if res[0] == float("inf") else s[res[1]:res[2] + 1]