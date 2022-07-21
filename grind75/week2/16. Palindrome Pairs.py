class Solution:
    def palindromePairs(self, words):
        """
        # APPROACH : GREEDY ##
        ## LOGIC ##

        1st Inside For Loop: [abaaa, ba, aa] => prefix : 'ab', check if reverse of 'ab' 
        is the given list, check if remainingprefix :'aaa' is palindrome, make sure it is 
        not the same word, (reverse word).

        2nd  Inside For Loop: [ abaaa, ba, aa ] => suffix : 'aa', check if reverse of 'aa' 
        is the given list, check if remainingsuffix :'aba' is palindrome, make sure it is not 
        the same word, (reverse word).
        
		## TIME COMPLEXITY : O(K^2 x N) ## k -> prefix
		## SPACE COMPLEXITY : O((K + N)^2) ##

        # Ex : 
        # words : ["abcd","dcba","lls","s","sssll"]
        # reversedWords: {'dcba': 0, 'abcd': 1, 'sll': 2, 's': 3, 'llsss': 4}
        # ans : [[0,1],[1,0],[3,2],[2,4]]
        """

        def isPalindrome(s):
            start = 0
            end = len(s) - 1

            while( start < end ):
                if( s[ start ] != s[ end ] ):
                    return False
                start += 1
                end -= 1
            return True

        results = set()
        reversedWords = { word[::-1]: index for index, word in enumerate(words) }

        for i, word in enumerate(words):
            for j in range(0,len(word)+1):
                prefix = word[:j]
                print("Prefix {} at j {}".format(prefix, i,j) )
                pfremain = word[j:]
                print("Prefix remain {} at j {}".format(pfremain, i) )

                if prefix in reversedWords and isPalindrome(pfremain) and reversedWords[prefix] != i:
                    results.add((i,reversedWords[prefix]))
                    print("####################### ADDED PREFIX {} at j {} with solution {},".format(prefix, i, (i,reversedWords[prefix])) )


            for j in range(len(word), -1, -1):
                suffix = word[j:]
                print("Suffix {} at j {}".format(suffix, i,j) )
                sfremain = word[:j]
                print("Suffix remain {} at j {}".format(sfremain, i,j) )
                if suffix in reversedWords and isPalindrome(sfremain) and reversedWords[suffix] != i:
                    results.add((reversedWords[suffix],i))
                    print("####################### ADDED SUFFIX {} at j {} with solution {}".format(suffix, i, (reversedWords[suffix],i)))

        return results

sol = Solution()
print(sol.palindromePairs(["abcd","dcba","lls","s","sssll"]))
#print(sol.palindromePairs(["bat","tab","cat"]))
#print(sol.palindromePairs(["a",""]))