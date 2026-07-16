def solveNQueens(n):
    output=[]
    string =""

    while len(string)<n:
        string=string+"."
        
    original_string=string    

    def backtrack(row, col, Queens, start_col, string, path, place_queen):
        if len(path)==n and row==n :
            output.append(path)
            path=[]
            return

        if col >= n :
            if start_col != 0:
                col = start_col-1   
            else:
                col=start_col+1
            start_col = col
            place_queen = True

        if row==0 :   
            if n%2 !=0:                  #n is odd and first row
                i = 0
            elif n%2 ==0:                #n is even and first row
                i =1     
            for col in range(i, n):
                print(col,path)
                start_col = col
                place_queen =True
                string=string.replace(string[col],"Q")
                path.append(string)
                backtrack(row+1, col+2, Queens-1, start_col, original_string, path, place_queen =True)

        if place_queen :
            string.replace(string[col],"Q")
            path.append(string)
            backtrack(row+1, col+2, Queens-1, start_col, original_string, path, place_queen =True)

    backtrack(0, 0, n, 0, "", [], False )
    return output

print(solveNQueens(4))