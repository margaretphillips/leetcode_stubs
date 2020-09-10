#given an array of integers return true or false if there are any duplicates

def containsduplicate(arr):
    dict = {}
    for a in arr:
        if a not in dict:
            dict[a] = 1
        else:
            return True

    return False

arr = [1,2,3,4,14,5,6,27,7,8]
result = containsduplicate(arr)
print(result)