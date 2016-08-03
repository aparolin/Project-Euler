multiples = {}

def calculateMultiples(number, limit):
    for i in range(number, limit, number):
        multiples[i] = i

limit = 1000

calculateMultiples(3, limit)
calculateMultiples(5, limit)

print(sum(multiples.values()))