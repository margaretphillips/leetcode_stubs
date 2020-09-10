#for a given unsorted array
# #find the two consecutive numbers with the greatest sum

#1) initialize max at 0
#2) get the sum of the first items up to k
#3) loop through the array where the upper point would be length - k
#4) for each item subtract the previous result from the sum of the current item and the item at position k

def slidingwindow(arr, n,  k):
    max = 0
    item = sum([arr[i] for i in range(k)])
    for i in range(0, n-k):
        item = item - arr[i] + arr[i+k]
        if item > max:
            max = item

    return max

#arr = [1,2,6,7,3,9,2,3,4,5]
arr = [80,-50, 80, -100]
n = len(arr)
k = 2

result = slidingwindow(arr, n, k)
print(result)
