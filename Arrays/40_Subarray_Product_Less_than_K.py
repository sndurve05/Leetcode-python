'''class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k <= 1:
            return 0
        count =0
        for i in range (len(nums)):
            left, right = i,i
            pro = 1
            while right < len (nums):
                pro = pro * nums[right]
                if pro < k:
                    count+=1
                    right+=1
                else:
                    break
        return count '''


class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k <= 1:
            return 0

        left =0       
        count = 0 
        product = 1

        for right in range (len(nums)):
            product = product * nums[right]

            while product >= k :
                product = product // nums[left]
                left+=1
               
            count += right - left +1        
            '''
            counts subarrays if [10,5,2,6]
            and right is at 5 then the count will add more 2 which are the subarrays [5] and [5,10]
            '''
            
        return count 