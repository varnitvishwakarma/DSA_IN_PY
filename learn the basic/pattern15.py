def print15(n):
    for i in range(0,n):
        for j in range(65,65+(n-i)):
            print(chr(j),end="")
        print()
        

print15(3)