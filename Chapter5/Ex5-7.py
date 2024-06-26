#Ex5-7.1
#เขียนคำสั่งอ่านชื่อย่อธนาคารจากอินพุตซึ่งเป็นรายการของชื่อคั่นด้วยช่องว่าง เช่น SCB BBL KBANK 
#นำมาเก็บแบบลิสต์ในตัวแปรชื่อ banks โดยเก็บเรียงจากซ้ายไปขวาในลิสต์ ตามลำดับพจนานุกรม
banks = input().split()
banks.sort()

#Ex5-7.2
#เขียนคำสั่งอ่านเลขท้ายสามตัวของสลากกินแบ่งที่ถูกรางวัลจากอินพุต เช่น 323 434 028 นำมาเก็บแบบลิสต์ในตัวแปรชื่อ last3 
#โดยเก็บจากซ้ายไปขวาในลิสต์ เรียงจากมากไปน้อย
last3 = input().split()
last3.sort()
last3 = last3[::-1]

#Ex5-7.3
#เขียนคำสั่งอ่านชื่อย่อธนาคารและราคาหุ้นจากอินพุตในรูปแบบดังตัวอย่าง SCB=132.0, BBL=176.5, KBANK=172.0 
#เพื่อแสดงชื่อธนาคารกับราคาหุ้น (คั่นด้วยช่องว่าง) บรรทัดละธนาคาร เรียงตามชื่อธนาคาร ตามพจนานุกรม
banks = []
t = input().split(", ")
for e in t:
    banks.append(e.split("="))
banks.sort()
for name,q in banks:
    print(name,q)

#Ex5-7.4
#เขียนคำสั่งอ่านชื่อย่อธนาคารและราคาหุ้นจากอินพุตในรูปแบบดังตัวอย่าง SCB=132.0, BBL=176.5, KBANK=172.0 
#เพื่อมาประมวลผลและแสดงชื่อธนาคาร บรรทัดละชื่อ จากชื่อที่มีราคาหุ้นมากสุดมาน้อยสุด
quotes = []
t = input().split(", ")
for e in t:
    name,q = e.split("=")
    quotes.append([float(q),name])
quotes.sort()
for q,name in quotes[::-1]:
    print(name)