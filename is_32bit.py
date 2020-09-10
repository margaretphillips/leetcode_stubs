#how to find out if an int is 32 bit
x = 2147483648

#if abs(x) >= 2147483648: return 0
#if x >= 2 ** 31 - 1 or x <= -2 ** 31: return 0
#if abs(x) > 0xffffffff: return 0

"""def is32(n):
    try:
     bitstring=bin(n)
    except (TypeError, ValueError):
      return False
    
    if len(bin(n)[2:]) <=32:
        return True
    else:
        return False"""
