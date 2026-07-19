class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        min_c_target = float('+inf')
        answer , sum = 0,0 

        for i in range(len(nums)):
            left = i+1
            right = len(nums)-1

            while left<right:   
                sum = nums[i] + nums[left] + nums[right]
           
                if sum == target:
                    return target 

                if abs(target - sum ) < abs(min_c_target ):
                   
                    min_c_target = abs(target - sum )
                    answer = sum
                    
                if sum>=target:
                     right-=1

                else:
                    left+=1
        return answer
