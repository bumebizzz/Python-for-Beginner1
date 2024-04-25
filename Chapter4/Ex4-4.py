#โจทย์อยู่ใน README.md Assignment 4
#Assignment 4-4.1
n = int(input())
s = 0
for i in range(n):
    s += i
print(s)


#Assignment 4-4.2
n = int(input())
s = 0
for i in range(1,n+1):
    if i%2 == 0:
        s += i
    s += i
print(s)

#Assignment 4-4.3
n = int(input())
s = 0
k = 1
for i in range(n,0,-1):
    if i%2 == 0:
        s += i*k
    else:
        s -= k
    k += 2
    s += i*k
print(s)

#Ex4-4.4
#อ่านจำนวนเต็ม a, b และ c จาก input แล้วแสดงจำนวนเต็มที่มีค่า a, a+c, a+2c, ... บรรทัดละหนึ่งค่า 
#โดยจะหยุดแสดงเมื่อค่าที่คำนวณมากกว่าหรือเท่ากับ b เช่น a=2, b=7, c=2 จะแสดง 2, 4 และ 6 บรรทัดละค่า
x = input().split()
a = int(x[0])
b = int(x[1])
c = int(x[2])
for i in range(a, b, c):
    print(i)

#Ex4-4.5
#อ่านจำนวนเต็มไม่ติดลบ m จาก input แล้วแสดงจำนวนเต็มที่มีค่าตั้งแต่ -m จนถึง m บรรทัดละหนึ่งค่า
m = int(input())
for i in range(-m, m+1):
    print(i)

#Ex4-4.6
#อ่านจำนวนเต็มไม่ติดลบ m จาก input แล้วแสดงเฉพาะจำนวนเต็มคู่ที่มีค่าตั้งแต่ -m จนถึง m บรรทัดละหนึ่งค่า
m = int(input())
s = -m; t = m
if m%2 == 1: 
    s += 1
    t -= 1
for i in range(s, t+1, 2):
    print(i)

#Ex4-4.7
#ข้อมูลที่ input มีบรรทัดแรกเป็นจำนวนเต็ม n ตามด้วยอีก n บรรทัดเป็นจำนวนเต็ม d0, d1, ..., dn-1 บรรทัดละจำนวน 
#จงเขียนโปรแกรมอ่านข้อมูลจาก input (โดยใช้วงวน for) เพื่อหาผลรวมของ d0, d1, ..., dn-1
n = int(input())
s = 0
for k in range(n):
    s += int(input())
print(s)

#Ex4-4.8
#มีรายการของจำนวนเต็มในบรรทัดเดียวกันของ input เช่น 10 20 30 55 
#จงเขียนชุดคำสั่งอ่านจำนวนเต็มเหล่านี้เก็บใส่ตัวแปรชื่อ a ที่เป็นลิสต์ 
#จากนั้นสร้างลิสต์ของจำนวนจริงมีขนาดเท่ากับของ a แต่ละช่องเก็บค่าครึ่งหนึ่งของที่เก็บใน a เช่น อ่านข้อมูลได้ a = [10,20,30,55] แล้วก็สร้าง b = [5.0, 10.0, 15.0, 27.5]
x = input().split()
a = [0]*len(x)
for i in range(len(x)):
    a[i] = int(x[i])
b = [0.0]*len(x)
for i in range(len(a)):
    b[i] = a[i]/2