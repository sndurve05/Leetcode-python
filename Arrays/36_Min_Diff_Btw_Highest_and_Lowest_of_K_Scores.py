class Solution(object):
    def minimumDifference(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        left = 0
        right = left+k-1
        min_score = float('inf')
        while right < len(nums):
            min_score = min(min_score, nums[right] - nums[left])
            left+=1
            right+=1

        return min_score