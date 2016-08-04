def check(dividend):
    lowestDivisor = 1
    highestDivisor = 20

    for divisor in range(lowestDivisor, highestDivisor+1):
        if (dividend % divisor != 0):
            return False
    
    return True

candidate = 20
while (True):
    if(check(candidate)):
        break
    
    candidate = candidate + 1

print(candidate)

      

    