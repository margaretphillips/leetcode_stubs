#given an array of string group the anagrams
#an anagram is formed by grouping the letters of a different word
#ie ...ate and tea have the same letters

def groupanagrams(arr):
    n = arr
    #sub = []
    #sep =','
    #dict = {}

    for a in arr:
        print('----------')
        print(a)
        for x in n:
            if x != a:
                for i in range(0,len(x)):
                    print(x[i])
                    print('-----')

    #for a in arr:
    #    n.append(sep.join(sorted(a)).replace(',', '').replace(' ', ''))

    #for x in n:
    #    if x not in dict:
    #        dict[x] = []
    #    else:
    #        dict[x].append(x)

    #print(dict)

    #return n


arr = ['eat', 'tea', 'tan', 'nat', 'ate']
result = groupanagrams(arr)
print(result)