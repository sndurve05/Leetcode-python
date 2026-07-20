class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """       
        max_length = 0 
        left, right = 0,0
        mpp = {}
        
        while right < len (s):
            
            while s[right] in mpp:
                del mpp[s[left]]
                left+=1

            mpp[s[right]]=right 
            max_length = max ( max_length, right - left + 1)
            right+=1
            
        return max_length