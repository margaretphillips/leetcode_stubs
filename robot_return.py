#robot is standing at position (0,0)
#given a series of moves what is its final position
#1) U = UP
#2) D = DOWN
#3) R = RIGHT
#4) L = LEFT


def robotreturn(str):
    x = 0
    y = 0

    for s in str:
        if s == 'U':
            y += 1
        elif s == 'D':
            y -= 1
        elif s == 'R':
            x += 1
        elif s == 'L':
            x -= 1

    return x, y

str = 'UDRDRLDRRLR'
result = robotreturn(str)
print(result)
