class Solution(object):
    def getFood(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int

        - `'*'` is your location. There is **exactly one** `'*'` cell.
        - `'#'` is a food cell. There may be **multiple** food cells.
        - `'O'` is free space, and you can travel through these cells.
        - `'X'` is an obstacle, and you cannot travel through these cells.
        """
        
        q = []
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '*':
                    q.append((r, c))
                    break
        
        result = 0
        while q:
            result += 1
            new_q = []
            for r, c in q:
                for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    nr, nc = r+dr, c+dc
                    if not (0 <= nr < len(grid) and
                            0 <= nc < len(grid[0]) and
                            grid[nr][nc] != 'X'):
                        continue
                    if grid[nr][nc] == '#':
                        return result
                    grid[nr][nc] = 'X'
                    new_q.append((nr, nc))
            print("q is {}, new_q is {}".format(q,new_q))

            q = new_q 
        return -1

#G1, output = 3
G1 = [["X","X","X","X","X","X"],["X","*","O","O","O","X"],["X","O","O","#","O","X"],["X","X","X","X","X","X"]]

#G2, output= -1
G2 = [["X","X","X","X","X"],["X","*","X","O","X"],["X","O","X","#","X"],["X","X","X","X","X"]]

#G3, outpu = 6
G3 = [["X","X","X","X","X","X","X","X"],["X","*","O","X","O","#","O","X"],["X","O","O","X","O","O","X","X"],["X","O","O","O","O","#","O","X"],["X","X","X","X","X","X","X","X"]]

sol = Solution()
for g in [G1,G2,G3]:
    print(sol.getFood(g))