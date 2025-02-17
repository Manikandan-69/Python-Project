def missing_numbers(n):
    numbers=set(n)
    x=sorted(n)
    output=[]
    for i in range(1,x[-1]):
        if i not in numbers:
            output.append(i)
    return output

a=[1,3,5,7,9,8,6,4,15]
op=missing_numbers(a)
print(op)