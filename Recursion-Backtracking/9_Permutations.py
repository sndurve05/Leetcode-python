class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        output=[]
       
        def backtrack(remaining_num,path):
          
            if len(remaining_num)<=0 or len(path)==len(nums):
                output.append(list(path))
                return

            for num in range(len(remaining_num)):
                path.append(remaining_num[num])
                new_remaining = remaining_num[:num]+remaining_num[num+1:]
                backtrack(new_remaining,path)
                path.pop()
               
            
        backtrack(nums,[])
        return output