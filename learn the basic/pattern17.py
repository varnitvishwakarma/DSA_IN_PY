def print17(n):
        for i in range(0, n):
            ch = chr(65)  
            breakpoint = i  
            for j in range(0, n - i - 1):
                print(" ", end=" ")

            for j in range(0, i + 1):
                print(ch, end=" ")
                ch = chr(ord(ch) + 1)  

            ch = chr(ord(ch) - 2)  
        
            for j in range(0, i):
                print(ch, end=" ")
                ch = chr(ord(ch) - 1)  
      
            print()
  

print17(5)