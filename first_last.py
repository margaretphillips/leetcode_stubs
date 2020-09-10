#given an array of integers
#sorted in asc order
#find start and end positions of a given target value

def firstandlast(arr, target):
    #get the index of the target
    x = arr.index(target)
    #reverse the array and find what the backward index is
    n = sorted(arr, reverse=True)
    #subtract the backward index from the len ( -1 for zero indexing )
    y = len(n) - n.index(target)-1

    return x,y



arr = [10,10,11,11,11,14,15]
target = 11

result = firstandlast(arr, target)
print(arr)
print(result)