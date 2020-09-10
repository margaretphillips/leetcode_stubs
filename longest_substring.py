#given a string ie...abcabcbb
# find the longest substring that doesn't have repeating characters

def longest_substring(str):
    l = 0
    top = 0
    for i in range(1, len(s)+1):
        #get a substring
        n = s[l:i]
        #get a count of each item in the substring
        m = [n.count(x) for x in s[l:i]]
        #if the count of any item is more than 1
        # restart the first element of the substring to the next element
        if len(m) > 0:
            if max(m) > 1:
                l += 1
            if len(m) > top:
                top = len(m)-1

    return top

s = 'abcabcbb'
#s = 'abcdeacknsqc'
result = longest_substring(s)
print(result)

