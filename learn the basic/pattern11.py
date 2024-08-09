def print11(n):
       for i in range(0,n):
           if i%2==0:
                start=1
           else:
                start=0

           for j in range(1,i+2):
               print(start,end="")
               start=1-start
           print()
print11(4)
