def factorial(n):
    res = 1
    for i in range(2,n+1):
        res *= i
    return count_0(res)

def count_0(n):
    c = 0
    t = str(n)
    for i in range(1, len(t)):
        if t[-i] == "0":
            c+=1
        else: break
    return c

if __name__ == "__main__":
    test = 3000
    print(factorial(test))