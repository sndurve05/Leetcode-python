
def lengthOfLongestSubstring( s):
        
        max_length=0
        for i in range (0,len(s)-1):
            for j in range(i+1,len(s)):
                if s[i]==s[j]:
                    print(i,j)
                    sub = s[i:j]
                    
                    print(sub)
                    if len (sub)>max_length:
                        max_length = len(sub)
                        string = s[i:j]
                    break
                
        return max_length,string

print(lengthOfLongestSubstring("abcabcbbababba"))