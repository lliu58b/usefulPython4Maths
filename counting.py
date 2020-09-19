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
    result = int(permutation(n, r)/math.factorial(r))
    return result

print(combination(7, 1) * combination(6, 2))
print(combination(13, 3))