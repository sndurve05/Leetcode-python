def isAdditiveNumber(num):
      
    def backtrack(start,second_num="",third_num=""):

        if start == len(num): #base_condition
            return True

        if start==0:   #First_time
                
            for j in range( 1 , len(num)+1):
                    
                first_num = num[:j]
                        
                if (len(first_num)>1 and first_num[0]=="0"):
                    continue

                for k in range(j+1,len(num)+1):
                    second_num = num[j:k]
                          
                    if (len(second_num)>1 and second_num[0]=="0"):
                        continue
                       
                    y = int(first_num)+int(second_num)

                    third_num = num[k:(k+(len(str(y))))]
                    end= (k+(len(str(y))))
                       
                    if len(third_num) != len(str(y)):
                        continue

                    if third_num != str(y):
                        continue
                        
                    if backtrack(end, second_num, third_num):
                        return True
                                
            return False                  
        else:
            first_num = second_num
            second_num = third_num
            
            y = int(first_num) + int(second_num)

            third_num = num[start:start+(len(str(y)))]  

            if len(third_num)>1 and third_num[0]=="0":
                return False

            if len(third_num) != len(str(y)):
                return False

            end2 = start+(len(str(y)))

            if third_num == str(y):
                return backtrack(end2, second_num, third_num)
                
            return False   

    return backtrack(0)              
      

num=input("Enter")
print(isAdditiveNumber(num))