#EX6-4.1
#จงเขียนฟังชัน fill(x,e) ที่รับ x เป็นลิสต์ และ e เป็นอะไรก็ได้ fill จะทำให้ทุกช่องใน x เก็บ e (fill ไม่คืนผลใด ๆ) 
#(หมายเหตุ: หลีกเลี่ยงการใช้คำสั่ง return โดด ๆ เพราะตัวตรวจในปัจจุบันยังมีปัญหากับคำสั่งนี้)
# อย่าเปลี่ยนแปลงหัวฟังก์ชันข้างล่างนี้
def fill(x, e):
    for i in range(len(x)):
        x[i] = e


#EX6-4.2
#จงเขียนฟังชัน clip(x) ที่รับ x เป็นลิสต์ของจำนวนเต็ม ฟังก์ชันนี้จะเปลี่ยนทุกข้อมูลใน x ที่ติดลบให้เป็น 0 และเปลี่ยนทุกตัวลิสต์ที่เกิน 255 ให้เป็น 255 (ฟังก์ชันนี้อาจเปลี่ยนค่าในลิสต์ x ที่รับมา ฟังก์ชันไม่คืนผลใด ๆ) 
#(หมายเหตุ: หลีกเลี่ยงการใช้คำสั่ง return โดด ๆ เพราะตัวตรวจในปัจจุบันยังมีปัญหากับคำสั่งนี้)
def clip(x):
    for i in range(len(x)):
        if x[i] < 0:
            x[i] = 0
        elif x[i] > 255:
            x[i] = 255

#EX6-4.3
#จงเขียนฟังชัน replace(x,old,new,count) ที่รับ x เป็นลิสต์, old กับ new เป็นข้อมูลอะไรก็ได้ และ count เป็นจำนวนเต็ม ฟังก์ชันนี้จะเปลี่ยนข้อมูลใน x ที่มีค่า old ให้เป็น new เป็นจำนวนอย่างมาก count ตัว (นับจากซ้ายไปขวา) เช่น x = [1,2,3,3,3,2,3], replace(x,3,9,2) จะทำให้ x เปลี่ยนเป็น [1,2,9,9,3,2,3] 
#(หมายเหตุ: หลีกเลี่ยงการใช้คำสั่ง return โดด ๆ เพราะตัวตรวจในปัจจุบันยังมีปัญหากับคำสั่งนี้)
def replace(x, old, new, count):
    c = 0; i = 0
    while i < len(x) and c < count:
        if x[i] == old:
            x[i] = new
            c += 1
        i += 1