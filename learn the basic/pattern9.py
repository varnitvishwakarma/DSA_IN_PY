def print9A(n):
        for i in range(0,n):
            for j in range(0,n-i-1):
                print(" ",end="")
            for j in range(0,2*i+1):
                print("*",end="")
            for j in range(0,n-i-1):
                print(" ",end="")
            print()
def print9b(n):
        for i in range(0,n):
            for j in range(0,i):
                print(" ",end="")
            for j in range(0,2*n-(2*i+1)):
                print("*",end="")
            for j in range(0,i):
                print(" ",end="")
            print()

print9A(3)
print9b(3)