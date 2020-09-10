#given an array of integers
#every number in the array appears twice except for 1
#find that number

def singlenumber(arr):
    for i in arr:
        if arr.count(i) == 1:
            return i

arr = [11,13,14,11,15,14,13,12,12]
result = singlenumber(arr)
print(result)
