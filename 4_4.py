def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        pierwszy,drugi=0,1
        for i in range(n):
            drugi+=pierwszy
            pierwszy=drugi-pierwszy
        return drugi

print(fibonacci(11))