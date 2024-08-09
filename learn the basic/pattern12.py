def print12(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j,end=" ")
        for j in range(1,2*(2*n-2*j)+1):
            print(" ",end="")
        for j in range(i,0,-1):
            print(j,end=" ")
        print()
print12(5)