class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        visited = set()
        m = len(board)
        n = len(board[0])
        
        def dfs(i,j,step):
        
            visited.add((i,j))
            if step <= len(word)-1 and word[step] == board[i][j]:
                
                
                if step == len(word)-1:
                    return True
                directions = [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]
                
                for t in directions:
                    if t[0] >= 0 and t[0] < m and t[1] >= 0 and t[1] < n and t not in visited:
                        if dfs(t[0],t[1],step+1) is True:
                            return True
                        else:
                            visited.remove((t[0],t[1]))
            else:
                return False
            
        for i in range(m):
            for j in range(n):
                if word[0] == board[i][j]:
                    visited.add((i,j))
                    if dfs(i,j,0) is True:
                        return True
                    visited = set()
        return False