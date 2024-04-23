#มีตัวแปร d1, m1, y1 กับ d2, m2, y2 ให้แล้ว เก็บวันเดือนปีเกิดของ Tom กับ Jerry ตามลำดับ 
#จงแสดงว่า Tom หรือ Jerry ใครเกิดก่อน (ให้ถือว่าไม่มีกรณีเกิดวันเดือนปีเดียวกัน)

y1 = int(input())
m1 = int(input())
d1 = int(input())

y2 = int(input())
m2 = int(input())
d2 = int(input())

if [y1,m1,d1] < [y2,m2,d2]:
  print("Tom")
else:
  print("Jerry")