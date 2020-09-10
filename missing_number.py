#given an array of integers find the missing number in the array

def missingnumber(arr):
    num = 0
    n = sorted(arr)

    for i in range(0, len(arr)-1):
        n = arr[i]+1 == arr[i+1]
        if n == False:
            return arr[i]+1


arr = [1,2,3,5,6,7,8,9]
result = missingnumber(arr)
print(result)