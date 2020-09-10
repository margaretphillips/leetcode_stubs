#Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#An input string is valid if:
#Open brackets must be closed by the same type of brackets.
#Open brackets must be closed in the correct order.

class Solution:
    def isValid(self, s):
        l = [('(', ')'), ('{', '}'), ('[', ']')]
        a = False

        for i, x in enumerate(s):
            #print(x)
            for y in l:
                #print('y ' + str(y))
                if x in y:
                    #print('found 1 ' + str(x) + ' in ' + str(y) + ' at ' + str(s.index(x)))
                    #print('found 1 ' + str(s[i]) + ' in ' + str(y) + ' at ' + str(s.index(s[i])))
                    if s[i] == y[0]:
                        #print('found 2 ' + str(s[i]) + ' in ' + str(y[0]) + ' at ' + str(s.index(s[i])))
                        if (i+1) < len(s):
                            #print('found 3 ' + str(s[i + 1]) + ' in ' + str(y[1]) + ' at ' + str(s.index(s[i + 1])))
                            if s[i] == y[0] and s[i + 1] in y[1]:
                                final = s.index(s[i + 1]) - s.index(s[i])
                                #print('found 4 ' + str(final))
                                if final == 1:
                                    #print('found')
                                    a = True
                        else:
                          #print('nope')
                          a = False
        return a
s = "()"
#Output: true
s = "()[]{}"
#Output: true
s = "(]"
#Output: false
s = "([)]"
#Output: false
s = "{[]}"
#Output: true
s = "(){}}{"
#Output: false
s = ")(){}"
#Output: false

result = Solution()
final = result.isValid(s)
print(final)