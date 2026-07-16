class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        output=[]
        used=[False]*len(nums)

        def backtrack(path):
            if len(path)==len(nums):
                output.append(list(path))
                return

            for i in range(len(nums)):
                if used[i]:
                    continue
                
                if i>0 and nums[i]==nums[i-1] and not used[i-1]:
                    continue

                path.append(nums[i])
                used[i]=True

                backtrack(path)

                path.pop()
                used[i]=False

        backtrack([])
        return output

        
