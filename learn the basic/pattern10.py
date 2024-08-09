def print10(n):
    for i in range(1,2*n):
            
            if i>n:
                star=2*n-i
            else:
                star=i
    
            for j in range(star):
                    print("*",end=" ")
        
                
            print()

print10(3)