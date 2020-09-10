#Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
#For example, two is written as II in Roman numeral, just two one's added together.
#Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.
#exceptions:
#I can be placed before V (5) and X (10) to make 4 and 9.
#X can be placed before L (50) and C (100) to make 40 and 90.
#C can be placed before D (500) and M (1000) to make 400 and 900.
#Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.

class Solution:
    def romanToInt(self, s):
        l = []
        x = []
        y = 0
        exceptions = {
            'IV': 4,
            'IX': 9,
            'XL': 40,
            'XC': 90,
            'CD': 400,
            'CM': 900
        }
        numerals = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        for i, letter in enumerate(s):
            if s[i:i+2] in exceptions:
                l.append([s[i:i+2], (i, i+1)])
                x.append(str(i))
                x.append(str(i+1))
            else:
                l.append([s[i], (i,i)])


        for i, letter in enumerate(l):
            if letter[1][0] == letter[1][1]:
                if str(letter[1][0]) in x:
                    l.remove(l[i])


        for i, letter in enumerate(l):
            if letter[1][0] == letter[1][1]:
                y += numerals[letter[0]]
            else:
                y += exceptions[letter[0]]

        return y

s = 'IX'
s = 'XII'
s = 'LVI'
s = 'III'
s = 'VV'
s = 'IV'
s = "MCMXCIV"
s = "LVIII"
s = "MDCCCLXXXIV"
#( 1884 )

result = Solution()
final = result.romanToInt(s)
print(final)


"""def romanToInt(self, s):
    l = []
    x = []
    y = 0
    exceptions = {
        'IV': 4,
        'IX': 9,
        'XL': 40,
        'XC': 90,
        'CD': 400,
        'CM': 900
    }
    numerals = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    for i, letter in enumerate(s):
        if s[i:i + 2] in exceptions:
            l.append([s[i:i + 2], (i, i + 1)])
        else:
            l.append([s[i], (i, i)])

    for i, letter in enumerate(l):
        if letter[1][0] != letter[1][1]:
            x.append(str(letter[1][0]))
            x.append(str(letter[1][1]))

    for i, letter in enumerate(l):
        if letter[1][0] == letter[1][1]:
            if str(letter[1][0]) in x:
                l.remove(l[i])

    for i, letter in enumerate(l):
        if letter[1][0] == letter[1][1]:
            y += numerals[letter[0]]
        else:
            y += exceptions[letter[0]]

    return y"""


"""def romanToInt(self, s):
    y = 0
    exceptions = {
        'IV': 4,
        'IX': 9,
        'XL': 40,
        'XC': 90,
        'CD': 400,
        'CM': 900,
        'III': 3,
        'VVV': 15
    }
    numerals = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    for i in exceptions:
        if i == s:
            return exceptions[i]

    skip = False
    for i in range(0, len(s)):
        if (i + 1) < len(s):
            x = s[i] + s[i + 1]
        else:
            if s[i] not in numerals:
                # print(" here2 " + str(x))
                return y

        # print(s[i:])
        if x in exceptions:
            print('exceptions  ' + str(x) + '  :  ' + str(exceptions[x]))
            y += int(exceptions[x])
            skip = True
        elif s[i] in numerals:
            print('numerals  ' + str(s[i]) + ' : ' + str(numerals[s[i]]))
            if skip == False:
                y += int(numerals[s[i]])

    return y"""