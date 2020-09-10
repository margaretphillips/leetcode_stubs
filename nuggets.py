#this equation seems to work for any array filled with a set of consecutive numbers ( each integer only appears once )
nums = [1,2,3,4,5,6,7,8,9,10]
n = len(nums)
print('Sum of array ', n*(n+1)//2)