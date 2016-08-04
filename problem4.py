import math

def isPalyndrome(word):
    length = len(word)
    middle = math.ceil(length/2)

    for i in range(0, middle):
        firstChar = word[i]
        lastChar = word[-i-1]

        if (firstChar != lastChar):
            return False
    
    return True

largestPalyndrome = 0

for i in range(100,1000):
    for j in range(100,1000):
        candidate = i*j

        if isPalyndrome(str(candidate)):
            if candidate > largestPalyndrome:
                largestPalyndrome = candidate

print(largestPalyndrome)