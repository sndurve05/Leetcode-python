class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        output=[]
        candidates.sort()
        def backtrack(path,index):
    
            if sum(path)==target:
                output.append(list(path))
                return

            if sum(path)>target:
                return

            for i in range(index,len(candidates)):
                if candidates[i]>target:
                    break
                    
                path.append(candidates[i])
                backtrack(path,i)
                path.pop()
                
               
        backtrack([],0)
        return output

        