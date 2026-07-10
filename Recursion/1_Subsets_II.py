class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        output=[]

        def backtrack(index,path):

            if len(nums)==0 or index==len(nums):
                output.append(list(path))
                return
            
            path.append(nums[index])
            backtrack(index+1,path)
            path.pop()
            
            next_index=index+1
            while next_index < len(nums) and nums[index]==nums[next_index]:
                next_index+=1

            backtrack(next_index,path)
        backtrack(0,[])        
        return output

