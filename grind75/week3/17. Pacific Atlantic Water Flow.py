class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        
        n = len(heights)
        m = len(heights[0])
  
        
        
        pacific = set()
        atlantic = set()
        
        
        def dfs_pa(r,c):
        
            pacific.add((r,c))
    
            directions = [(r-1,c), (r+1,c), (r, c-1), (r, c+1)]
            
            for d in directions:
                if d not in pacific and d[0] >= 0 and d[0] < n and d[1] >= 0 and d[1] < m and heights[d[0]][d[1]] >= heights[r][c]:
                    dfs_pa(d[0],d[1])
                    
                
        def dfs_at(r,c):
        
            atlantic.add((r,c))
    
            directions = [(r-1,c), (r+1,c), (r, c-1), (r, c+1)]
            
            for d in directions:
                if d not in atlantic and d[0] >= 0 and d[0] < n and d[1] >= 0 and d[1] < m and heights[d[0]][d[1]] >= heights[r][c]:
                    dfs_at(d[0],d[1])
            
        
        for i in range(n):
            dfs_pa(i,0) # blocco colonna
        
        
        for j in range(m):
            dfs_pa(0,j) # blocco riga
            
        
        
        for i in range(n):
            dfs_at(i,m-1) # blocco colonna
        
        
        for j in range(m):
            dfs_at(n-1,j) # blocco riga
            
        res = pacific.intersection(atlantic)
        res_list = []
        for t in res:
            res_list.append(list(t))
        return list(res_list)
        