#Ex4-3.1
#a, b และ e จาก input (ในบรรทัดเดียวกัน คั่นด้วยช่องว่าง) แล้วแสดงคำว่า close enough ถ้า |a−b|≤e⋅max(|a|,|b|)
#เป็นจริง ไม่เช่นนั้น แสดงว่า not equal
x = input().split()
a = float(x[0])
b = float(x[1])
e = float(x[2])
if abs(a-b) <= e*max(abs(a),abs(b)):
    print("close enough")
else:
    print("not equal")

#Ex4-3.2
#รับจำนวนจริง x จาก input แล้วใช้วิธี bisection หาและแสดงค่าของ 3√x(รากที่ 3 ของ x) 
#กำหนดให้ a และ b มีค่าเกือบเท่ากัน เมื่อ |a−b|≤10−6(10 ยกกำลังลบ 6) max(|a|,|b|)
x = float(input())
L = 0; U = x
r = (L + U)/2
r3 = r**3
while abs(r3-x) > 1e-6*max(r3, x):
    if r3 > x:
        U = r
    else:
        L = r
    r = (L + U)/2
    r3 = r**3
print(r)