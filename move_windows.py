#given an array of integers
#move all the zeros to the end of the array
# while maintaining the relative position of the other elements

def zerostoback(arr):
    z = arr.count(0)
    n = []
    for i in range(0, len(arr)-1):
        if arr[i] != 0:
            n.append(arr[i])

    for i in range(z):
        n.append(0)

    return n

arr = [1,0,3,5,7,0,14]
result = zerostoback(arr)
print(result)