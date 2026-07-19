class Solution(object):
    def minimumRecolors(self, blocks, k):
        """
        :type blocks: str
        :type k: int
        :rtype: int
        """
        left=0
        right = left + k
        count, min_count = 0,float('inf')
        while right<len(blocks)+1:
            for x in blocks[left:right]:
                if x=="W":
                    count+=1
            min_count=min(min_count,count)
            count=0
            left+=1
            right+=1

        return min_count