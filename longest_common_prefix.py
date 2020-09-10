#Write a function to find the longest common prefix string amongst an array of strings.
#If there is no common prefix, return an empty string "".


class Solution:
    def longestCommonPrefix(self, strs):
        x = ''
        dict = {}
        l = []

        for s in strs:
            if s not in dict:
                dict[s] = 1
            else:
                dict[s] += 1

            for i in range(0, len(s)):
                if s[:i] != '' and len(s[:i]) > 1:
                    if s[:i] not in dict:
                        dict[s[:i]] = 1
                    else:
                        dict[s[:i]] += 1
                    if s[i:] != '' and len(s[i:]) > 1:
                        if s[i:] not in dict:
                            dict[s[i:]] = 1
                        else:
                            dict[s[i:]] += 1

        for d in dict:
            if dict[d] > 1:
                l.append(d)

        return dict

strs=["flower", "flow", "flight"]
#Output: "fl"
#strs=["dog","racecar","car"]
#Output: ""
#Explanation: There is no common prefix among the input strings.
#strs =["a"]
#expected 'a'
#strs = ["aa","ab"]
#expected 'a'

result = Solution()
final = result.longestCommonPrefix(strs)
print(final)


"""def longestCommonPrefix(self, strs):
    x = ''
    dict = {}
    l = []

    for s in strs:
        if s not in dict:
            dict[s] = 1
        else:
            dict[s] += 1

        for i in range(0, len(s)):
            if s[:i] != '' and len(s[:i]) > 1:
                if s[:i] not in dict:
                    dict[s[:i]] = 1
                else:
                    dict[s[:i]] += 1
                if s[i:] != '' and len(s[i:]) > 1:
                    if s[i:] not in dict:
                        dict[s[i:]] = 1
                    else:
                        dict[s[i:]] += 1

    for d in dict:
        if dict[d] > 1:
            l.append(d)

    return sorted(l, key=lambda x: len(x), reverse=True)[0]"""