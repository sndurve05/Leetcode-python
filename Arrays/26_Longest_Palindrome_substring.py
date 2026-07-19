'''def longestPalindrome( s):
        
        def palindrome(string, left=0, right=0):
           
            right = len(string)-1
            while left<right:
                if string[left] != string[right]:
                    return False
                left+=1
                right-=1

            return True
        
        max=""
        string=""
        for i in range (0,len(s)):
            print("i", i)
            for j in range(i+1,len(s)+1):
                print("j",j)
                string = s[i:j]
                
                if palindrome(string):
                    print("enetered if for string: ",string)
                    if len(string)>len(max):
                        max = string 
                        print(max)

        return max'''

#TIME COMPLEXITY O(n)
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def expandaroundcentre (left,right):
             
            while left>=0 and right<len(s) and s[left]==s[right]:
                left-=1
                right+=1

            return right-left-1

        if len(s)==0:
            return ""
        max_len = 0
        start = 0
        for i in range(len(s)):
            len1 = expandaroundcentre(i,i)
            len2 = expandaroundcentre(i,i+1)

            current_len = max(len1,len2)

            if current_len>max_len:
                max_len = current_len 

                start = i - ((current_len-1)//2)

        return s[start : start + max_len]
