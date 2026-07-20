class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        left = 0
        right = left+k
        s = float(sum(nums[left:right]))
        max_avg = float(s/k)
        

        while right < len(nums):
            s = float((s - nums[left]+nums[right]))
            avg = float(s/k)
            max_avg = max(max_avg, avg)
            left +=1
            right+=1
            
        return max_avg
