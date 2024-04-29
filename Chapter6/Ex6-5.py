#EX6-5.1
#ฟังก์ชัน mean_sd ข้างล่างนี้หาค่าเฉลี่ยและส่วนเบี่ยงเบนมาตรฐาน (ที่ทำงานได้ถูกต้องแล้ว ไม่ต้องแก้ไข) 
#จงเขียนคำสั่งเพิ่มเติมเพื่อหาค่าเฉลี่ยและส่วนเบี่ยงเบนมาตรฐานของข้อมูลในลิสต์ x แสดงบรรทัดละค่า (แสดงค่าเฉลี่ยก่อน)
# ไม่ปรับเปลี่ยนคำสั่งใด ๆ ในฟังก์ชันข้างล่างนี้
def mean_sd(x):
    mean = sum(x)/len(x)
    s2 = 0
    for e in x:
        s2 += (e-mean)**2
    sd = (s2/len(x))**0.5
    return mean,sd

x = [1,2,2,3,2,3,2,3,2,3,2,3,2,2,3,2]
m,s = mean_sd(x)
print(m)
print(s)

#EX6-5.2
#ฟังก์ชัน mean_sd ข้างล่างนี้หาค่าเฉลี่ยและส่วนเบี่ยงเบนมาตรฐาน (ที่ทำงานได้ถูกต้องแล้ว ไม่ต้องแก้ไข) 
#จงเขียนคำสั่งเพิ่มเติมเพื่อหาค่าเฉลี่ยและส่วนเบี่ยงเบนมาตรฐานของข้อมูลในลิสต์ x แสดงบรรทัดละค่า (แสดงค่าเฉลี่ยก่อน)
def mean_sd(x):
    mean = sum(x)/len(x)
    s2 = 0
    for e in x:
        s2 += (e-mean)**2
    print(mean)
    print((s2/len(x))**0.5)

x = [1,2,2,3,2,3,2,3,2,3,2,3,2,2,3,2]
mean_sd(x)