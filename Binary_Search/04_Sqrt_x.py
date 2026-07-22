class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        low = 0
        high = x

        while low<=high:
            mid = low + (high - low)//2
            sq = mid**2 
            if sq > x:
                high =mid-1
            elif sq < x:
                low = mid +1
            else:
                return mid
        return high #in line 13 we make high = mid-1 and the condition is that we need to consider the immediate lower of where it is rejecting.