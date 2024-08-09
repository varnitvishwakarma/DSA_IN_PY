def print14(n):
    a = 'A'  # Starting character

    for i in range(n):
        for j in range(i + 1):  
            print(chr(ord(a) + j), end="")  
        print()  
n = 5
print14(n)
def print14(n):
    for i in range(1, n + 1): 
        for j in range(65, 65 + i): 
            print(chr(j), end="")  
        print() 

n = 5
print14(n)
