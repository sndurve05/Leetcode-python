class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        output=[]
        def backtrack(i,path):
            
            if len(path)==k and sum(path)==n:
                output.append(list(path))
                return
            if i>9:
                return
            path.append(i)
            backtrack(i+1,path)
            path.pop()
            backtrack(i+1,path)

        backtrack(1,[])
        return output
