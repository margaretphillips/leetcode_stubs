#time complexity

nums = [1,2,3,4]
n = len(nums)
print('Sum of array ', n*(n+1)//2)

#count operations
#1) assignment ( nums = [1,2,3,4]) - ignore constant
#2) assignment ( n = len(nums)) - ignore constant
#3) multiplication ( n* ) - ignore constant - arithmetic - ( * )
#4) addition ( (n+1) )  - ignore constant - arithmetic - ( + ) - ignore constant ( 1 )
#5) division ( //2 ) - ignore constant - arithmetic - ( // ) - ignore constant ( 2 )
#6) the only thing that is left is n so complexity is 1

#number of operations do not depend on the length of the array
#time complexity = O(1)
#represents an algorithm with a constant number of operations regardless of the size of the input

nums = [1,2,3,4]
n = len(nums)
sum = 0

for i in range(0, n):
    sum += nums[i]

print('Sum of array ', sum)

#count operations
#1) assignment ( nums = [1,2,3,4]) - ignore constant
#2) assignment ( n = len(nums)) - ignore constant
#3) assignment ( sum = 0) - ignore constant
#4) n additions ( sum += )
#5) n assignments ( = )
# n assignments, n additions, n comparisons ( range(0, n ))
#this is 5N + 3 operations
#O(n) because the time and space complexity will increase depending on the input

#linear O(n) - as input grows runtime scales
#constant o(1) - as input grows runtime is constant
#quadratic O(n^)  -- using ^ to represent squared -- as our input grows the runtime squares
