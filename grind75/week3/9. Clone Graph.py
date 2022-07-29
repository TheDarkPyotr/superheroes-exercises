class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        nodelist = {}
        if node is None:
            return 
        newNode = Node(node.val,[])
        nodelist[node] = newNode #  = {node: newNode}
        self.dfs(node, nodelist)
        
        return newNode
           
    def dfs(self, node, nodelist):
        
        for n in node.neighbors:
            if n not in nodelist:
                
                copy = Node(n.val, [])
                nodelist[n] = copy
                nodelist[node].neighbors.append(copy)
                self.dfs(n, nodelist)
            else:
                nodelist[node].neighbors.append(nodelist[n])
                print(nodelist)