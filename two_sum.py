#given an array of integers and a target integer
#return the indices of the numbers in the array that add up to that target number

class Solution:
    def twoSum(self, nums, target):
        for i,num in enumerate(nums):
            if (target-num) in nums:
                if nums.index(target-num)!=i:
                    return [i,nums.index(target-num)]

nums = [3,13]
target = 6
#Output: [0,1]
#nums = [3,2,4]
#target = 6
#Output: [1,2]
#nums = [2,7,11,15]
#target = 9
#Output: Because nums[0] + nums[1] == 9, we return [0, 1]
#nums = [12,2,33,5,6,17,8]
#target = 19

result = Solution()
final = result.twoSum(nums, target)
print(final)

#nums = [3,3]
#target = 6
#Output: [0,1]
#nums = [3,2,4]
#target = 6
#Output: [1,2]
#nums = [2,7,11,15]
#target = 9
#Output: Because nums[0] + nums[1] == 9, we return [0, 1]
#nums = [12,2,33,5,6,17,8]
#target = 19

"""def twoSum(nums, target):
    # remove any numbers >= target
    n = [x for x in nums if x < target]
    # set a pointer at beginning and end
    x = 0
    # find the combination
    while n[x] + n[x + 1] != target:
        x += 1

    return f'[{x}, {x + 1}]'"""









