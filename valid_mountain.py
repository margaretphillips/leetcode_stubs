#given an array of integers return true if certain conditions are met
#1) length of array is at least 3
#2) the array should have an increasing sequence followed by a decreasing sequence
#3) ie....[1,2,3,3,2,1]

def validmountain(arr):
    n = True
    n = len(arr) >= 3
    if n:
        mid = arr[max(arr)]
        a1 = arr[0:mid+1]
        a2 = arr[mid+1:len(arr)]
        for a in range(0, len(a1)-1):
            if int(a1[a]) < int(a1[a+1]):
                n = True
            else:
                return False
        for a in range(0, len(a2)-1):
            if int(a2[a]) > int(a2[a+1]):
                n = True
            else:
                return False

    return n

arr = [1,2,3,4,3,2,1]
result = validmountain(arr)
print(result)