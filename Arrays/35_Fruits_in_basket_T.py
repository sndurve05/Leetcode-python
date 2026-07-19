class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        mpp = {}
        left=0
        right=0
        max_len=0
        length = 0
        while right < len(fruits):
            if fruits[right] not in mpp:
                mpp[fruits[right]]=1
          
            else:
                mpp[fruits[right]]+=1
        
            if len(mpp)<=2:
                
                length = sum(mpp.values())
                max_len = max(max_len, length)
                
            else:
                mpp[fruits[left]]-=1
                
                if mpp[fruits[left]]==0:
                    del mpp[fruits[left]]
                left+=1
                
            right+=1
     
        return max_len
