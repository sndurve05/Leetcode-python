class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        output=[]

        def backtrack(path,index,remaining_sum):

            if remaining_sum==0:
                output.append(list(path))
                return

            for i in range(index,len(candidates)):
                if candidates[i]>target or sum(path)>target:
                    return

                if i>index and candidates[i]==candidates[i-1]:
                    continue

                path.append(candidates[i])
            
                backtrack(path, i+1, remaining_sum - candidates[i])
                path.pop()

        backtrack([],0,target)
        return output