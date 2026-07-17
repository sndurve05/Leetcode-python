class Solution(object):
    def maxSubArray(self, nums):      # USED Hashing
        """
        :type nums: List[int]
        :rtype: int
        """
        sum=0
        max_sum = float('-inf')        # if it is a negative array,, setting max to 0 would give outout as 0 ( correct output will be the maximum one among those negative numbers)
        min_sum = 0
        prefix_sum = {0:-1} #KEY: SUM; VALUE:INDEX
        for i in range (len(nums)):
            num = nums[i]
            sum += num
            prefix_sum[sum] = i
            candidate_sum = sum - min_sum
            max_sum = max(max_sum , candidate_sum)
            min_sum = min(min_sum , sum)

        return max_sum