import math

def eratosthenes_sieve(number):
    notPrimes = {}
    
    max = math.ceil(math.sqrt(number))

    for i in range (2, max):
        if i in notPrimes:
            continue
        else:
            if (number % i == 0):
                yield i
            
            for j in range(i*i, max, 2*i):
                notPrimes[j]=True

print(max(list(eratosthenes_sieve(600851475143))))