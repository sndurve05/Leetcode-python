class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        pro1 = nums[-1]*nums[-2]*nums[-3]
        pro2 = nums[0]*nums[1]*nums[-1]

        return max(pro1,pro2)