class Solution(object):
    
def ladderLength(self, beginWord, endWord, wordList):
        deque = collections.deque([beginWord])
        ls = string.ascii_lowercase
        wordList = set(wordList)
        dist = 1
        while deque:
            size = len(deque)
            for _ in range(size): # BFS level by level
                word = deque.popleft()
                if word == endWord:
                    return dist
                for i in range(len(word)):
                    for c in ls:
                        if word[i] != c:
                            newWord = word[:i]+c+word[i+1:]
                            if newWord in wordList:
                                wordList.remove(newWord)
                                deque.append(newWord)
            dist += 1
        return 0