class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        output=[]
        def backtrack(path,index):

            if index==len(nums):
                output.append(list(path))
                return

            path.append(nums[index])
            backtrack(path,index+1)
            path.pop()
            backtrack(path,index+1)

        backtrack([],0)
        return output

