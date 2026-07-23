class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        low = 0
        high = len(nums)-1
        first = len (nums)
        while low<=high:
            mid = low + (high-low)//2
            if nums [mid]<target :
                low = mid+1
            elif nums [mid]>=target:   #LOWER BOUND
                first = mid
                high = mid-1

        if first == len(nums) or nums[first] != target:
            first = -1

        low = 0
        high = len(nums)-1
        last = len(nums)
        while low<=high:
            mid = low + (high-low)//2

            if nums[mid]<=target:          #HIGHER BOUND
                last = mid
                low = mid+1
            elif nums[mid]>target:
                high = mid-1

        if last == len(nums) or nums[last]!=target:
            last = -1
      
        return [first,last]
