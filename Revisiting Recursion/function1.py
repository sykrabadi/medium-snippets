def retrunVal(val1, val2):
    result = val1 + val2
    return result

def notReturnVal(val1, val2):
    result = val1 + val2
    return

a = 2
b = 3

c = retrunVal(a, b)
d = notReturnVal(a, b)

print(c)
print(d)

c = c + 2
d = d + 2
print(c)
print(d)