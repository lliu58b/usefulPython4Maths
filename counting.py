import math

def permutation(n, r):
    result = 0
    temp = n
    while temp > (n - r):
        if temp == n:
            result = n
        else:
            result = result * temp
        temp -= 1
    return result 

def combination(n, r):
    if r == 0:
        return 1
    result = int(permutation(n, r)/math.factorial(r))
    return result

print(combination(200, 3))
print(combination(200, 4))
print(combination(200, 5))