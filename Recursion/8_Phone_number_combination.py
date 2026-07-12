class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        dict_map={2:"abc",3:"def",4:"ghi",5:"jkl",6:"mno",7:"pqrs",8:"tuv",9:"wxyz"}
        output=[]
        def backtrack(i,substring):
            if i==len(digits):
                output.append(substring)
                return
            
            num_key=int(digits[i])
            string=dict_map[num_key]

            for char in range(len(string)):
                substring = substring + string[char]
                backtrack(i+1,substring)
                substring=substring[:-1]
                
        backtrack(0,"")
        return output