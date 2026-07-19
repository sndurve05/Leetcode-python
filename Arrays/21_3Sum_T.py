class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        output=[]
       
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            if nums[i]>0:
                break
            num1 = nums[i]
            target = -1 * nums[i]
            left =  i+1
            right = len(nums)-1
            while left<right:
    
                if nums[left]+nums[right]>target:
                    right-=1

                elif nums[left]+nums[right]<target:
                    left+=1
                else:
                    output.append([num1, nums[left], nums[right]])
                    left+=1
                    right-=1

                    while left < right and nums[left] == nums[left-1]:
                        left += 1

                    while left < right and nums[right] == nums[right+1]:
                        right -= 1
                
        return output
