def print5(n):
    for i in range(0, n):  
        for j in range(0, n - i):  
            print("*", end="")  
        print()  
print5(n)
