def fibonacci(maxValue):
    n1 = 1
    n2 = 2

    next = 3

    idx = 1

    while (next <= maxValue):
        if idx == 1:
            yield 0
        elif idx == 2:    
            yield 2
        else:
            next = n1 + n2

            if (next % 2 == 0):
                yield next
            else:
                yield 0

            n1 = n2
            n2 = next
        
        idx = idx + 1

print(sum(fibonacci(4000000)))