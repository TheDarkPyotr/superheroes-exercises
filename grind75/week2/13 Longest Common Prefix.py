def longestCommonPrefix(words): 
        prefix = words[0]
        
        for word in words[1:]:
            
            while word[:len(prefix)] != prefix: 
                print("prefix is %s",prefix)
                prefix = prefix[:-1]
                print("postfix is %s",prefix)
                    
                if not prefix: 
                    return ""
        return prefix
    

#print(longestCommonPrefix(["flo0123456789","flower","flight"]))
print(longestCommonPrefix(["florida","flower","flight", "flow"]))