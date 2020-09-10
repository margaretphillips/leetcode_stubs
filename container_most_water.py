#given a non negative list ( a )
#where each item represents a coordinate ( i, ai )
#find two lines, where together, form the container
#that holds the most water
#ie...[1,8,6,2,5,4,8,3,7]
#1) container would be (8,8)
#2) numbers between 8 and 7 are less or equal to 8, and can be included in the container
#3) where the first x = 8 because its the value of the first number
#4) and y = 8 because its the index of the second number

#find the x and y of the first item with the greatest value
#find the x and y of the second item with the same or next lowest value as the first

def container_most_water(arr):
    #print(arr)
    x = 0
    y = 0
    #find the maximum value and the index of the item
    x1 = max(arr)
    y1 = arr.index(x1)
    #find the maximum value and the index of the second item
    x2 = max(arr)
    y2 = arr.index(x1, y1+1)
    #slice the items between the first y
    n = arr[y1+1:y2]
    #slice the value between the second y and the end of the array
    r = arr[y2+1:len(arr)]
    #if there are elements beyond y2
    # compare the maximum value of the two subarrays
    #if the max value of the second subarray is bigger adjust the container
    if len(r) > 0 and max(r) > max(n):
       x2 = max(r)
       y2 = arr.index(max(r), y2+1)




    return [(x1, y1),(x2,y2)]


arr = [1,8,6,2,5,4,8,3,7]
result = container_most_water(arr)
print(result)