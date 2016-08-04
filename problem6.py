def calculateSquaredSum(limit):
    sum = 0

    for i in range(1,limit+1):
        sum = sum + i

    return sum*sum

def calculateSumOfSquares(limit):
    sumOfSquares = 0

    for i in range(1,limit+1):
        sumOfSquares = sumOfSquares + i*i

    return sumOfSquares

limit = 100

print(abs(calculateSumOfSquares(limit) - calculateSquaredSum(limit)))