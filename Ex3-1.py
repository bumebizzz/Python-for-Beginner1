#โจทย์อยู่ใน README.md Assignment 3
#Assignment 3.1
a = int(input())
b = int(input())
if a < b:
  min = a
  max = b
else:
  min = b
  max = a
print(min, max)

#Assignment 3.2
if abs(a-b) > 2:
    a,b = b,a
else:
    a = b**2 + a
print(a,b)

#Assignment 3.3
#if a%2 == 0: a เป็นจำนวนคู่
if a%2 == 0:
    a *= 2
else:
    if a > 10:
        a //= 2
    else:
        a = 0
print(a)

#Assignment 3.4
#if a%2 == 0: a เป็นจำนวนคู่
if a%2 == 0:
    if a > 10:
        a //= 2
    else:
        a = 0
else:
    a *= 2
print(a)

#Assignment 3.5
if a%2 == 0:
    b = 2*a
    if a > 10:
        a //= 2
    else:
        b += a
    a += b
else:
    a *= 2
print(a,b)