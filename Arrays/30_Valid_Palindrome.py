class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        s = " ".join(s)
    
        for i in s:
        
            if (not i.isalnum()):
                s = s.replace(i,"")
        
        if s==s[::-1]:
            return True
        else:
            return False  