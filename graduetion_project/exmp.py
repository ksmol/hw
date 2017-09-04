a = [x for x in range(10)]
print(a)
b = [x for x in range(11, 20)]
print(b)
c = [a, b]
print(c)
for ind in c:
    for i in ind:
        print(i)
d = [i for ind in c for i in ind]
print(d)