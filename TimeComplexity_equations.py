#time complexity

#1) ignore smaller terms
# 5N^ * 3N + 1
#1) ignore smaller terms ( 1 )
#2) ignore constants ( 5, 3, 1)
#3) when N^ * N - N is a smaller terms than N^ so ignore
#4) this is O(n^)

#what is considered a constant
#1) arithmetic operations
#2) assignments
#3) direct array element access by index


def findcomplexity(n):
    sum1 = 0 #ignore constants
    sum2 = 0 #ignore constants
    for i in range(0, n):
        for j in range(0, n): #this is O(n^)
            sum1 +=1

    for k in range(0, n):
        sum2 += 1 #this is O(n) - doesn't matter how many n

    return sum1, sum2

#O(n^) + O(n) - throw out the smaller term
#answer this is O(n^)
print(findcomplexity(10))