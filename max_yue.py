def fun(a,b):
    if a<b:
        a,b = b,a
    c = a%b
    while c != 0:
        a = b
        b = c
        c = a % b
    return b

print(fun(16,15))