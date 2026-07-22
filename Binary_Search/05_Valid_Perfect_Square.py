class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        low = 0
        high = num
        while low<=high:
            mid = low+ (high-low)//2

            sq = mid *mid

            if num == sq:
                return True

            elif num >sq:
                low = mid+1

            else :
                high = mid-1

        return False