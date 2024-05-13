#Ex8-3.1
#จงเขียนฟังก์ชัน get_countries(capital_city, s) รับ capital_city เป็นดิกเก็บข้อมูลในรูปแบบ {ชื่อประเทศ: ชื่อเมืองหลวง} และ s เป็นสตริง 
#ฟังก์ชันนี้คืนลิสต์ของชื่อประเทศที่ขึ้นต้นด้วยค่าที่เก็บใน s โดยลิสต์ที่คืนเรียงชื่อประเทศจากน้อยไปมากตามพจนานุกรม
def get_countries(capital_city, s):
    result = []
    for country in capital_city:
        if country.find(s) == 0:
            result.append(country)
    result.sort()
    return result

#Ex8-3.2
#จงเขียนฟังก์ชัน get_courseIDs(number_of_students, k) รับดิก number_of_students ที่เก็บข้อมูลในรูปแบบ {รหัสวิชา: จำนวนนิสิตที่ลงทะเบียน} กับ k ที่เป็นจำนวนเต็ม 
#ฟังก์ชันนี้คืนลิสต์ของรหัสวิชาต่าง ๆ ที่มีจำนวนผู้ลงทะเบียนเรียนตั้งแต่ k คนขึ้นไป โดยให้เรียงรหัสวิชาในลิสต์ที่คืนจากน้อยไปมาก
def get_courseIDs(number_of_students, k):
    result = []
    for cid in number_of_students:
        if number_of_students[cid] >= k:
            result.append(cid)
    result.sort()
    return result

#Ex8-3.3
#จงเขียนฟังก์ชัน add_all(points, blacklist, extra) รับดิก points ที่เก็บข้อมูลในรูปแบบ {รหัสสมาชิก: จำนวนแต้มสะสม}, blacklist เป็นลิสต์เก็บรหัสสมาชิก กับ extra เป็นจำนวนแต้ม 
#ฟังก์ชันนี้จะเพิ่มแต้มเป็นจำนวน extra ในดิก points ให้กับสมาชิกทุกรายที่มีรหัสไม่ปรากฏใน blacklist ฟังก์ชันนี้ไม่คืนอะไรเลย เพราะจะปรับข้อมูลใน points
def add_all(points, blacklist, extra):
    for m in points:
        if m not in blacklist:
            points[m] += extra
#ใช้วงวน for หยิบสมาชิกใน points เพื่อไปตรวจว่าต้องไม่อยู่ใน blacklist จึงจะเพิ่มแต้มให้