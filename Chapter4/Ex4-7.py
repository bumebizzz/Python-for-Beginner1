#เขียนโปรแกรมตามผังงานข้าง ๆ นี้ (ลองทำความเข้าใจด้วยว่าทำอะไร ?)
#โจทย์อยู่ใน README.md Assignment 4-7.1
n = int(input())
s = 0
k = 0
while k < n:
    x = int(input())
    if x < 0: break
    s += x*k
    k += 1
print(s)

#โจทย์อยู่ใน README.md Assignment 4-7.2
n = int(input())
s = 0
for k in range(n):
    x = int(input())
    if x < 0: break
    s += x*k
print(s)

#Ex4-7.3
#อ่านสตริงจาก input แล้วแยกสตริงออกเป็นสองส่วน เพื่อนำไปแสดง 
#โดยตัวแยกอาจเป็น @ หรือ : หรือ - หรือ + ก็ได้ เช่น abc@def แยกได้เป็น abc กับ def (สตริงที่รับมามีตัวแยกที่กำหนดไว้ตัวใดตัวหนึ่งแค่ตัวเดียวแน่ ๆ)
t = input()
for k in range(len(t)):
    if t[k] in "@:-+": break
s1 = t[:k]
s2 = t[k+1:]
print(s1, s2)

#Ex4-7.4
#แบบฝึกหัดข้อที่แล้ว ประกันว่ามีตัวแยกแน่ ๆ ในสตริงที่อ่านเข้ามาจาก input ในข้อนี้สตริงที่อ่านมาอาจไม่มีตัวแยกก็ได้ 
#ถ้าไม่มีก็แสดงสตริงเดิมที่รับมา ถ้ามีตัวแยก ก็แสดงเหมือนข้อที่แล้ว
t = input()
found = False
for k in range(len(t)):
    if t[k] in "@:-+": 
        found = True
        break
if found:
    s1 = t[:k]
    s2 = t[k+1:]
    print(s1, s2)
else:
    print(t)
