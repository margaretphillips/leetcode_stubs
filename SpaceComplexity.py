#space complexity
#only care about the space taken by the algorithm not the input

nums = [1,2,3,4]
n = len(nums)
sum = 0

for i in range(0, n):
    sum += nums[i]

print('Sum of array ', sum)

#1) count the number of variables  -  n, sum = 2 variables
#2) loop counter gets assigned n times - for i  ( i ) but doesn't take up space in memory
#3) ignore constants ( n, sum )
#4) sum gets assigned n times but it is still a single variable
#5) space complexity = O(1)

n = 100
arr = []

for i in range(0, len(n)):
    arr.append(i)

#1) count the variables - 2 variables ( n, arr )
#2) loop counter gets assigned n times - for i  ( i ) but doesn't take up space in memory
#3) ignore constants ( n )
#4) arr get's assigned n times but is not a constant, because it grows in memory for each loop
#5) space complexity is O(n)