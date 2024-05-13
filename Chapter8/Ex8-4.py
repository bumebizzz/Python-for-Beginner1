#Ex8-4.1
#p1 และ p2 เป็นดิกเก็บคะแนนของนักเรียนที่เรียนวิชา 1 และ 2 ตามลำดับในรูปแบบ {เลขประจำตัว: คะแนน} 
#จงเขียนฟังก์ชัน take_both(st_id, p1, p2) เพื่อหาว่านักเรียนที่มีเลขประจำตัว st_id เรียนทั้งสองวิชาหรือไม่
def take_both(st_id, p1, p2):
    return st_id in p1 and st_id in p2

#Ex8-4.2
#p1 และ p2 เป็นดิกเก็บคะแนนของนักเรียนที่เรียนวิชา 1 และ 2 ตามลำดับในรูปแบบ {เลขประจำตัว: คะแนน} 
#จงเขียนฟังก์ชัน both(p1, p2) เพื่อคืนลิสต์ที่เก็บเลขประจำตัวนักเรียนเรียนทั้งสองวิชา โดยเรียงลำดับเลขประจำตัวนักเรียนในลิสต์จากน้อยไปมากด้วย
def both(p1, p2):
    result = []
    for sid in p1:
        if sid in p2:
            result.append(sid)
    result.sort()
    return result

#Ex8-4.3
#สตริง DNA เป็นสตริงที่มีตัวอักษรแค่ A, T, G และ C เท่านั้น 
#จงเขียนฟังก์ชัน count_bases(dna) คืนดิกในรูปแบบ {เบส: จำนวน} เช่น count_bases("AAAATTTGG") ได้ {"A":4, "T":3, "G":2, "C":0}
def count_bases(dna):
    count = {"A":0, "T":0, "G":0, "C":0}
    for b in dna:
        count[b] += 1
    return count

#Ex8-4.4
#จงเขียนฟังก์ชัน count_chars(text) ที่นับว่าใน text มีอักขระอะไรเท่าไรบ้าง (โดยให้ตัวอักษรเล็กเหมือนใหญ่ เช่น count_chars("ABCabcZ") ได้ดิก {'A': 2, 'B': 2, 'C': 2, 'Z': 1} เป็นผลลัพธ์
def count_chars(text):
    count = {}
    for c in text:
        c = c.upper()
        if c in count:
            count[c] += 1
        else:
            count[c] = 1
    return count

#Ex8-4.5
#income1 และ income2 เป็นดิกในรูปแบบ {รหัสสาขาร้าน: รายได้} 
#ซึ่งเก็บรายรับของร้านอาหารสาขาต่าง ๆ จงเขียนฟังก์ชัน merge(income1, income2) ที่คืนดิกใหม่ในรูปแบบเดียวกัน แต่เก็บข้อมูลรวมจากทั้งสองดิกที่รับมา เช่น income1 = {"P100":100, "P200":200} และ income2 = {"P200":300, "P300":90} merge กันแล้วจะได้ดิกใหม่ {"P100":100, "P200":500, "P300":90}
def merge(income1, income2):
    result = {}
    for k in income1:
        result[k] = income1[k]
    for k in income2:
        if k in result:
            result[k] += income2[k]
        else:
            result[k] = income2[k]
    return result