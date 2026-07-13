class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x=str(x)
        def backtrack(index=0):
            if index>(len(x)//2):
                return (True)
            
            if x[index]==x[len(x)-index-1]:
                return backtrack(index+1)

            else:
                return False
        
        return backtrack()
        