class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if (len(nums)>1 and nums[0]>nums[1]) or len(nums)==1:
            return 0
        elif len(nums)>1 and nums[-1]>nums[-2]:
            return len(nums)-1
        
        low =1
        high = len(nums)-2
        while low<=high:
            mid = low + (high-low)//2

            if nums[mid-1]<nums[mid] and nums[mid]>nums[mid+1]:
                return mid
            elif nums[mid-1]>nums[mid] and nums[mid]<nums[mid+1]:
                low=mid+1 
            elif nums[mid]<nums[mid+1]:
                low=mid+1
            elif nums[mid-1]>nums[mid]:
                high = mid-1

           

