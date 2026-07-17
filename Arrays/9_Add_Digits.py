def f(num):
                                    #RECURSION
    if int(num)<10:
        return num
    total=0
    for i in str(num):
      
        total+=int(i)
       
    num=total
    return f(num)
   
    
