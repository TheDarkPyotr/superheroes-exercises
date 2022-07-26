class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
    
        n = len(grid) #righe
        m = len(grid[0]) #colonne
        island = 0
        
        def bfs(i,j):
            
            grid[i][j] = "0"
            
            if i+1 >= 0 and j >= 0 and i+1<n and j < m and grid[i+1][j] != "0": #giù
                bfs(i+1,j)
                
            if  i-1 >= 0 and j >= 0 and i-1<n and j < m and grid[i-1][j] != "0": #su
                bfs(i-1,j)
                
            if  i >= 0 and j-1 >= 0 and i<n and j-1 < m and grid[i][j-1] != "0": #sx
                bfs(i,j-1)
                
            if  i >= 0 and j+1 >= 0 and i<n and j+1 < m and grid[i][j+1] != "0": #dx
                bfs(i,j+1)
                
        for i in range(n):
            for j in range(m):
                if grid[i][j] != "0":
                    bfs(i,j)
                    island += 1
        return island