a = [i for i in range(2, 11)]
def prime1(n):
    for i in range(2, n):
        if n%i == 0:
            return False
    return True
aprime = []
for i in a:
    if prime1(i):
        aprime.append(i)
print(a)
print(aprime)

b = [i for i in range(2, 11)]
bprime = list(filter(lambda x: all(x%i != 0 for i in range(2, x)), b))
print(b)
print(bprime)

n =2
x = 5 if n>2 else None
print(x)