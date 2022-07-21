class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        
        N = len(startTime)
        jobs = list(zip(startTime, endTime, profit)) #Unisce le 3 liste
        jobs.sort()
        
        @lru_cache
        def rec(i):
            
            if i == N: return 0 #Finito i task, non c'è profitto da prendere
            
            j = i+1 #Prendo il successivo task di i
            
            while j < N and jobs[i][1] > jobs[j][0]: #Scarto i successivi di i che si overlappano
                j += 1
                
            one = jobs[i][2] + rec(j) #Faccio il primo + rec(successivo non in overlap con i)
            two = rec(i+1) #Cerco seconda strada a partire da i+1
            
            return max(one,two) #Ritorno la strada con più profitto
        return rec(0)
    
"""





Versione con sorting di startTime per ottimizzare ricerca indice j:



    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        
        N = len(startTime)
        jobs = list(zip(startTime, endTime, profit)) #Unisce le 3 liste
        jobs.sort()
        startTime.sort() ###SORT di starTime per usare bisect_left
        
        @lru_cache
        def rec(i):
            
            if i == N: return 0 #Finito i task, non c'è profitto da prendere
            
            j = bisect_left(startTime,jobs[i][1]) #### Restituisce successivo task di i che non si overlappa
        
            one = jobs[i][2] + rec(j) #Faccio il primo + rec(successivo non in overlap con i)
            two = rec(i+1) #Cerco seconda strada a partire da i+1
            
            return max(one,two) #Ritorno la strada con più profitto
        return rec(0)
    
"""


        



def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:

        jobs = [(s, e, p) for s, e, p in zip(startTime, endTime, profit)]
        jobs.sort(key=lambda x:x[1]) # sort by end time

        def find_right(dp, s):
            # find the last item that <= s
            l, r = 0, len(dp)-1
            while l <= r:
                mid = (l+r)//2
                e = dp[mid][0]
                if e <= s:
                    l = mid + 1
                else:
                    r = mid - 1
            return r

        
        dp = [(0, 0)] # (endtime, total profit)
        for s, e, p in jobs:
            last = find_right(dp, s) ##find the non-overlapping next job
            if dp[last][1] + p > dp[-1][1]: 
                dp.append((e, dp[last][1] + p))

        return dp[-1][1]


