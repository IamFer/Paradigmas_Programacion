n = 100000
fact  = 1.0
e = 1.0
x = 1.0
xx = 1.0

for i in range(1, n):
    xx *= x
    fact *= float(i)
    s = xx/fact
    e += s;

    print(xx)
    print(fact)
    print(s)
    print(e)
