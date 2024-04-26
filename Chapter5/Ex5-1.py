#Ex5-1.1
#มีข้อมูลทาง input สามบรรทัด บรรทัดแรกเป็นรายการของรหัสสินค้า 
#บรรทัดที่สองเป็นรายการของราคา (มีจำนวนข้อมูลเท่ากับของบรรทัดแรก โดยสินค้าชิ้นที่ตำแหน่ง i ก็มีราคาที่ตำแหน่ง i) 
#บรรทัดสุดท้ายเป็นรหัสสินค้าที่อยากรู้ว่าราคาเท่าไร ถ้าเป็นรหัสที่ไม่มีอยู่ ให้แสดง Not found
#ลักษณะข้อมูล
# บรรทัดแรก A100 A200 A300 A400
# บรรทัดที่สอง 20.5 50.0 35.0 65.0
# บรรทัดที่สาม A300

prod_ids = input().split()
prices = input().split()
qid = input()
found = False
for i in range(len(prod_ids)):
    if qid == prod_ids[i]:
        found = True
        break
if found:
    print(prices[i])
else:
    print("Not found")

#Ex5-1.2
#ลักษณะข้อมูลเหมือนข้อที่แล้ว แต่บรรทัดที่สามจะเป็นราคา 
#แล้วอยากให้หาว่ามีรหัสสินค้าอะไรบ้างที่ราคาไม่เกินราคาที่กำหนดในบรรทัดที่สาม 
#โดยให้แสดงรหัสสินค้าเรียงตามที่เขียนในบรรทัดแรก แสดงบรรทัดละรหัส 
#ถ้าไม่มีรหัสสินค้าใดเลย ให้แสดง Not found (จากตัวอย่างที่แสดง จะแสดงรหัสสินค้า A100, A200 และ A300 บรรทัดละรหัส)
#ลักษณะข้อมูล
# บรรทัดแรก A100 A200 A300 A400
# บรรทัดที่สอง 20.5 50.0 35.0 65.0
# บรรทัดที่สาม 55.0
prod_ids = input().split()
x = input().split()
prices = [0.0]*len(x)
for i in range(len(x)):
    prices[i] = float(x[i])
qprice = float(input())
found = False
for i in range(len(prod_ids)):
    if prices[i] <= qprice:
        print(prod_ids[i])
        found = True
if not found:
    print("Not found")