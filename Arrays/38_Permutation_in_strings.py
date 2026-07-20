class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1)>len(s2):
            return False

        left = 0 
        right = left + len(s1)
        mpp = {}

        for char in s1:
            if char in mpp:
                mpp[char]+=1
            else:
                mpp[char]=1

        dict1 = {}
        for i in s2[left:right]:
            if i in dict1:
                dict1[i]+=1
            else:
                dict1[i]=1

        while True:
            if dict1==mpp:
                return True
            if right==len(s2):
                break
            dict1[s2[left]]-=1

            if dict1[s2[left]] == 0:
                del dict1[s2[left]]

            if s2[right] in dict1:
                dict1[s2[right]] += 1
            else:
                dict1[s2[right]] = 1
                
            left+=1
            right+=1
            
        return False