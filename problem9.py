def check(a,b,c):
    if (a*a + b*b == c*c):
        return True
    else:
        return False

for a in range(1,999):
    for b in range(1,999-a):
        c = 1000-a-b
        if (check(a,b,c)):
            print("a: " + str(a) + " b: " + str(b) + " c: " + str(c))
            print(a*b*c)
            break