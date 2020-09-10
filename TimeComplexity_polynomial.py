#time complexity

#polynomial complexity

def quadratic(n):
    sum = 0
    for i in range(0,n):
        for j in range(0, n):
            sum += 1
    return sum

print(quadratic(10))

#1) n operations in outer loop
#2) n operations in inner loop for each n in outerloop
#n * n = n^ = O(n^)

def cubic(n):
    sum = 0
    for i in range(0,n):
        for j in range(0, n):
            for k in range(0, n):
                sum += 1
    return sum

print(cubic(10))

#1) n operations in outer loop
#2) n operations in inner loop for each n in outer loop
#3) n operations in inner loop for each n in outer inner loop
#n * n * n = n = O(n^^) -- ^^ meaning n to the 3rd power
