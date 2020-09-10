#Determine whether an integer is a palindrome.
# An integer is a palindrome when it reads the same backward as forward.
#Could you solve it without converting the integer to a string?


class Solution:
    def isPalindrome(self, n):
        if n < 0: return False

        divisor = 1
        while (n / divisor >= 10):
            divisor *= 10

        while n != 0:
            leading = n // divisor
            trailing = n % 10

            if leading != trailing: return False

            n = (n % divisor) // 10
            divisor = divisor // 100

        return True

n = 121
#Output: true
#n = -121
#Output: false
#Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
#n = 10
#Output: false
#Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

result = Solution()
final = result.isPalindrome(n)
print(final)


"""def palindrome(self, n):
    # Find the appropriate divisor
    # to extract the leading digit
    divisor = 1
    while (n / divisor >= 10):
        divisor *= 10

    while (n != 0):

        leading = n // divisor
        trailing = n % 10

        # If first and last digit
        # not same return false
        if (leading != trailing):
            return False

        # Removing the leading and
        # trailing digit from number
        n = (n % divisor) // 10

        # Reducing divisor by a factor
        # of 2 as 2 digits are dropped
        divisor = divisor / 100

    return True"""
