def missing_numbers(n):
    numbers=set(n)
    x=sorted(n)
    output=[]
    for i in range(1,x[-1]):
        if i not in numbers:
            output.append(i)
    return output

a=[1,4,15,5,6,7,8,8,8,10]
op=missing_numbers(a)
print(op)