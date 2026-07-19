class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        list1=[]
        for n in nums:
            list1.append(n*n)
        
        list1.sort()

        return list1