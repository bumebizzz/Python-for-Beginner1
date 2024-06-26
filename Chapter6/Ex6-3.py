#EX6-3.1
#จงเขียนฟังชัน dot ที่รับลิสต์ของจำนวนจริง 2 ลิสต์ แต่ละลิสต์แทนเวกเตอร์มีขนาดเท่ากัน 
#ฟังก์ชันนี้คำนวณและคืน dot product ของสองเวกเตอร์ที่ได้รับ
def dot(u, v):
    d = 0
    for i in range(len(u)):
        d += u[i]*v[i]
    return d

#EX6-3.2
#จงเขียนฟังชัน add ที่รับลิสต์ของจำนวนจริง 2 ลิสต์ แต่ละลิสต์แทนเวกเตอร์มีขนาดเท่ากัน 
#ฟังก์ชันนี้คำนวณและคืนผลบวกของสองเวกเตอร์ที่ได้รับ
def add(u, v):
    w = []
    for i in range(len(u)):
        w.append(u[i]+v[i])
    return w

#EX6-3.3
#จงเขียนฟังชัน to_list_of_strings ที่รับลิสต์หนึ่งตัว เพื่อสร้างและคืนลิสต์อีกตัวที่ภายในเก็บค่าที่นำข้อมูลจากลิสต์ที่รับมาแปลงเป็นสตริง 
#เช่น รับ [1,2,3] จะคืน ['1', '2', '3']
def to_list_of_strings(x):
    results = []
    for e in x:
        results.append(str(e))
    return results