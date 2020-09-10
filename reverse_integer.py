#given a 32-bit signed integer, reverse digits of an integer.

class Solution:
    def reverse(self, x):
        if x >= 2 ** 31 - 1 or x <= -2 ** 31: return 0

        sign = x < 0
        x = str(abs(x))
        l = []
        rev = 0

        for i, num in enumerate(x):
            l.append(x[-(i+1)])
        if sign:
            rev = int(','.join(l).replace(',', '')) * -1
        else:
            rev = int(','.join(l).replace(',', ''))

        #make sure the reverse is also 32 bit
        if int(rev) >= 2 ** 31 - 1 or int(rev) <= -2 ** 31:
            return 0
        else:
            return int(rev)


x = 2147483648
#x =1534236469
#my out 9646324351
#expected 0
#x = 123
#Output: 321
x = -123
#Output: -321
#x = 120
#Output: 21

result = Solution()
final = result.reverse(x)
print(final)
