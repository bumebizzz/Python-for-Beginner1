#EX6-1.1
#จงเขียนคำสั่งแสดงคำร้องของเพลง Happy Birthday to You ข้าง ๆ นี้ โดยการเรียกใช้ฟังก์ชัน sing ให้เป็นประโยชน์
#ผลลัพธ์
# Happy Birthday to you
#Happy Birthday to you
#Happy Birthday 
#Happy Birthday 
#Happy Birthday to you

def sing(msg, times):
    for k in range(times):
        print( msg )

sing("Happy Birthday to You", 2)
sing("Happy Birthday", 2)
sing("Happy Birthday to You", 1)

#EX6-1.2
#จงเขียนคำสั่งในฟังก์ชัน HBD(name) ให้แสดงคำร้องอวยพรวันเกิดระบุชื่อคนด้วย ดังตัวอย่างข้าง ๆ นี้ 
#(สีแดงคือชื่อคน) ภายใน HDB ต้องเรียกใช้ฟังก์ชัน sing ให้เป็นประโยชน์ 
#โดยในโปรแกรมข้างล่างนี้มีฟังก์ชัน sing และมีคำสั่งรับชื่อ แล้วเรียก HBD ให้แสดงคำร้องอวยพรวันเกิดให้แล้ว
#Happy Birthday to you
#Happy Birthday to you
#Happy Birthday Dear JJ # JJ คือชื่อคน
#Happy Birthday to you 

def sing(msg, times):
    for k in range(times):
        print( msg )

def HBD(name):
    sing("Happy Birthday to You", 2)
    sing("Happy Birthday Dear " + name, 1)
    sing("Happy Birthday to You", 1)

name = input()
HBD(name)