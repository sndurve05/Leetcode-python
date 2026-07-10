class Solution(object):
    def validStrings(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        output=[]
        
        def backtrack(zero,one,current_str):
            if len(current_str)==n or one+zero==n:
                output.append(current_str)
                return

            if len(current_str) == 0:
                backtrack(zero + 1, one, current_str + "0")
                backtrack(zero, one + 1, current_str + "1")
                return
            
            elif current_str[-1]== "0":
                backtrack(zero,one+1,current_str+"1")
                
            else:
                backtrack(zero+1,one,current_str+"0")
                backtrack(zero,one+1,current_str+"1")

        backtrack(0,0,"")
        return output