class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left = 0
        right = len(s)-1
       

        def ispalindrome(left,right):
            a = s[left:right+1]
            if a ==a[::-1]:
                return True
            return False

        while left<right:
            if s[left]==s[right]:
                left+=1
                right-=1
            else:
                if ispalindrome(left+1,right):
                    return True
                elif ispalindrome(left,right-1):
                    return True
                else:
                    return False

        return True 
            