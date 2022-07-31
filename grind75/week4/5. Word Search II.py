import collections

class TrieNode():
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.isWord = False
    
class Trie():
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root            #Assegno root
        for w in word:
            node = node.children[w] #Aggiorno node con figlio con chiave w
        node.isWord = True          #Ultimo nodo/carattere flaggo come word
    
    def search(self, word): #Ricerca per parole intere e non prefissi
        node = self.root
        for w in word:
            node = node.children.get(w)
            if not node:
                return False
        return node.isWord
    
class Solution(object):
    def findWords(self, board, words):
        res = []
        trie = Trie()
        node = trie.root

        for w in words:
            trie.insert(w)
            
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(board, node, i, j, "", res)
        return res
    
    def dfs(self, board, node, i, j, path, res):
        print("({},{}) PATH: {}".format(i,j, path))
        if node.isWord:
            print("({}, {}) {}.APPEND({})".format(i,j,res, path)) 
            res.append(path)
            node.isWord = False #Per evitare di reinserire duplicati

        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return 
        current_char = board[i][j]
        node = node.children.get(current_char)
        if not node:
            return 
        board[i][j] = "#"
        self.dfs(board, node, i+1, j, path+current_char, res)
        self.dfs(board, node, i-1, j, path+current_char, res)
        self.dfs(board, node, i, j-1, path+current_char, res)
        self.dfs(board, node, i, j+1, path+current_char, res)
        board[i][j] = current_char

board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
words = ["oath","pea","eat","rain"]
board1 = [["a","b"],["c","d"]]
words1 = ["abcb"]
sol = Solution()
print(sol.findWords(board,words))