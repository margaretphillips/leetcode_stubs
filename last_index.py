#find the first and last index of a number


def lastIndex(nums,target):
    try:
        return len(nums) - nums[::-1].index(target) - 1
    except Exception as e:
        print(e)
        return 0

def lastIndex2(nums,target):
    try:
        x = 0
        for i, num in enumerate(nums):
        #if we find the target make note of the index
            if num == target:
                x = i
            #if we reach the end of the list, x is the last index
            if i == len(nums)-1:
                return nums.index(target), x
    except Exception as e:
        print(e)
        return 0

#nums = [1, 3, 5, 3, 2, 5, 7, 3]
#target = 3
#nums = [3,2,4,2,5,3,4,2]
#target = 3
#nums = [2,7,11,7,15]
#target = 7
nums = [12,33,5,6,2,17,8]
target = 2

result = lastIndex(nums, target)
print(result)
result = lastIndex2(nums, target)
print(result)