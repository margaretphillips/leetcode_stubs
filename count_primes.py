#given a target, count the prime numbers that are less than the target
#prime numbers can only be divided by 1 and itself

def primenumbers(n):
    c = 0

    for i in range(2, n):
        x = i % 2
        y = i % i
        if x + y == 0:
            c += 1

    return c

n = 12
result = primenumbers(n)
print(result)