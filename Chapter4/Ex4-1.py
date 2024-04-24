#โจทย์อยู่ใน README.md Assignment 4
#Assignment 4.1
n = input ()
c = 0
while n > 0:
    n //= 2
    c += 1
print(c)

#Assignment 4.2
b = [1,2,3]
n = len(b)
k = 0
d = 0
while k < n:
    d += 2**k*int(b[n-k-1])
    k += 1
print(d)


#Assignment 4.3
c = 0
while n>0:
    n = n-1
    if n%3 == 0:
        n = n-c
        c += 1
print(c)