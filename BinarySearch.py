#search technique to find any element in a collection
#only works in a sorted collection
#1) sort the array
#2) find the midpoint
#3) if the target is at the midpoint return
#4) otherwise increase or decrease the midpoint until you find the target


def binarysearch(arr, target):
    #sort the array
    arr = sorted(arr)
    #find the middle index
    mid = len(arr) // 2
    #return if the mid is the target
    if arr[mid] == target:
        return mid
    else:
        #otherwise adjust the mid until target is found
        while arr[mid] != target:
            if arr[mid] < target:
                #go up
                mid += 1
            else:
                #go down
                mid -= 1
        return mid

# return element of target
arr = [1,2,6,7,3,9,2,3,4,5]
target = 4

result = binarysearch(arr, target)
print('index of target is ' + str(result))

#1) constant assignments 2 ( arr, mid) -- ignore constant
#2) comparison ( if mid is target initial ) -- ignore comparison ( lesser operation )
#3) n comparison ( is mid the target ) -- n comparison
#4) n assignment ( update mid ) - n assignment --ignore lesser comparison
# O(n) -- linear search