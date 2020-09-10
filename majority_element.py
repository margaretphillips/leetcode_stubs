#given an array of integers
#find the majority element

def majorityelement(arr):
    dict = {}
    max = 0
    index = 0
    for a in arr:
        if a not in dict:
            dict[a] = 1
        else:
            dict[a] += 1

    for d in dict:
        if dict[d] > max:
            max = dict[d]
            index = d

    return index


arr = [1,2,3,4,4,4,5,6,7,7,7,7,8]
result = majorityelement(arr)
print(result)