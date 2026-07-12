class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        arr=[]
        output=[]
        for i in range(1,n+1):
            arr.append(i)

        def backtrack(index,path):
            if len(path)==k:
                output.append(list(path))
                return
                
            if index>=len(arr):
                return

            path.append(arr[index])
            backtrack(index+1,path)
            path.pop()
            backtrack(index+1,path)

        backtrack(0,[])
        return output