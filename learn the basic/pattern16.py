def print16(n):
    for i in range(0,n):
        for j in range(65,65+i+1):
            print(chr(65+i),end=" ")
        print()

print16(4)
