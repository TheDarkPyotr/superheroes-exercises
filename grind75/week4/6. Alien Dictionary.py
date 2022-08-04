from typing import List
from collections import defaultdict, deque

"""
Build a graph with each character as a vertex and dependency as an edge connecting characters. 

Then sort vertices topologically. When performing topological sort, we'll need an array to store 
how many incoming edges each node has and always pick the node that has lowest number of incoming 
edge first, usually 0. 

If every node has at least one incoming edge (sinking), then it's a connected graph, 
meaning the graph is cyclic. In our case, the order would not be valid if the the graph is cyclic.

words = [
  "wrt",
  "wrf",
  "er",
  "ett",
  "rftt"
]

w1, w2 in zip(words, words[1:])
i = 0
    (wrt, wrf)
    (wrf, er)
    (wrt, ett)
    (wrt, rftt)
    ch1, c2 in zip(w1,w2):
        (w,w), (w,r) , (w,f), (r,w), (r,r), (r,f), (t,w) (t,r), (t,f)


"""
def alienOrder(words: List[str]) -> str:
    in_degree = {ch: 0 for word in words for ch in word}

    # 1. Build graph
    graph = defaultdict(set)
    for w1, w2 in zip(words, words[1:]):    #Per ogni combinazione di parole ??
        for ch1, ch2 in zip(w1, w2):        #e per ogni combinazione di caratteri
            if ch1 != ch2:                  #se i caratteri sono diveris
                if ch2 not in graph[ch1]:   #e non ancora collegati nel grafo
                    graph[ch1].add(ch2)
                    in_degree[ch2] += 1     #+1 arco in ingresso su nodo ch2
                break
        else:  # Check that second word isn't a prefix of first word.
            if len(w2) < len(w1):
                return ""

    print(graph)
    # 2. Identify vertices that have no incoming edge
    no_incoming_edges = deque([ch for ch in in_degree if in_degree[ch] == 0])
    print(no_incoming_edges)
    # 3. Repeatedly pick vertex of in-degree 0 and append it to the output
    aliendict = ""
    while no_incoming_edges:

        vertex = no_incoming_edges.popleft()
        aliendict += vertex
        print("Node {}, Alien dictionary {}".format(vertex, aliendict))
        for ch in graph[vertex]:
            in_degree[ch] -= 1
            if in_degree[ch] == 0:
                no_incoming_edges.append(ch)

    if len(aliendict) < len(in_degree):
        return ""

    return aliendict

words = [
  "wrt",
  "wrf",
  "er",
  "ett",
  "rftt"
]
print(words)
print(alienOrder(words))

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        adj = {char: set() for word in words for char in word}

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            minLen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]: #edge case:
                return ""
            for j in range(minLen):
                if w1[j] != w2[j]:
                    print(w1[j], w2[j])
                    adj[w1[j]].add(w2[j])
                    break

        visited = {}  # {char: bool} False visited, True current path
        res = []

        def dfs(char):
            if char in visited:
                return visited[char]

            visited[char] = True

            for neighChar in adj[char]:
                if dfs(neighChar):
                    return True

            visited[char] = False
            res.append(char)

        for char in adj:
            if dfs(char):
                return ""

        res.reverse()
        return "".join(res)