# https://leetcode.ca/all/261.html

import collections

class Solution:
    def validTree(self, n: int, edges):

            if len(edges)!=n-1:return False

            dist = collections.defaultdict(list)
            for n1,n2 in edges:
                dist[n1].append(n2)
                dist[n2].append(n1)

            visited=set()
            queue=collections.deque([0])
            while queue:
                node = queue.popleft()
                visited.add(node)
                for related in dist[node]:
                    if related not in visited:
                        visited.add(related)
                        queue.append(related)
            return len(visited)==n


sol = Solution()
#test = [(nodes, edges[[]])]
#t[0] -> true
#t[1] -> false
test = [ (5, [[0, 1], [0, 2], [0, 3], [1, 4]]), (5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]])]
print(sol.validTree(test[0][0], test[0][1]))
print(sol.validTree(test[1][0], test[1][1]))