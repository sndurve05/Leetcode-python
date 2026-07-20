class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        if target > sum(nums):
            return 0
        
        left,right,sum1 = 0,0,0
        min_len = float ('inf') 

        while right < len(nums):
            if nums[right]>=target:
                return 1
            
            sum1 += nums[right]
            right+=1

            while sum1 >= target:
                min_len = min(min_len, right - left)
                sum1 -= nums[left]
                left += 1
        
        return min_len
