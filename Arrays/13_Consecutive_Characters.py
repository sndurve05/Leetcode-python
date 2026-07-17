class Solution(object):
    def maxPower(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_length=0
        for i in range(0,len(s)-1):
            for j in range(i+1,len(s)+1):
                if j==len(s) or s[i]!=s[j]:
                    sub=s[i:j]
                    if len(sub)>max_length:
                        max_length = len(sub)
                    break
        if max_length==0:
            return len(s)       
        return max_length
    
#