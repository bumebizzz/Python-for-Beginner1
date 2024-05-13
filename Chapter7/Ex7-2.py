#EX7-2.1
#จงเขียนฟังก์ชัน number_of_newlines(s) หาว่ามีรหัสขึ้นบรรทัดใหม่ในสตริง s กี่ตัว
def number_of_newlines(s):
    c = 0
    for e in s:
        if e == "\n": c += 1
    return c

#EX7-2.2
#จงเขียนฟังก์ชัน left_strip(s) คืนสตริงใหม่ที่เหมือน s แต่ไม่มีช่องว่างทางซ้าย เช่น left_strip(" ab ") ได้ "ab "
def left_strip(s):
    return ((s+".").strip())[:-1]

#Ex7-2.3
#จงเขียนฟังก์ชัน right_strip(s) คืนสตริงใหม่ที่เหมือน s แต่ไม่มีช่องว่างทางขวา เช่น right_strip(" ab ") ได้ " ab"
def right_strip(s):
    return (("."+s).strip())[1:]

#Ex7-2.4
#จงเขียนฟังก์ชัน first_index_of(s,t) หาว่ามี t ปรากฎเริ่มต้นใน s ที่อินเด็กซ์ใด ถ้ามีหลายที่ให้คืนอินเด็กซ์น้อยสุด ถ้าไม่มีให้คืน -1 เช่น first_index_of("abracadabra", "bra") 
#ได้ 1 ในขณะที่ first_index_of("abracadabra", "BRA") ได้ -1
def first_index_of(s,t):
    return s.find(t)

#Ex7-2.5
#จงเขียนฟังก์ชัน first_index_of(s,t) หาว่ามี t ปรากฎเริ่มต้นใน s ที่อินเด็กซ์ใด 
#ถ้ามีหลายที่ให้คืนอินเด็กซ์น้อยสุด ถ้าไม่มีให้คืน -1 โดยการหาในถือว่าตัวอังกฤษเล็กเหมือนใหญ่ เช่น first_index_of("abracadabra", "bra") ได้ 1 และ first_index_of("abracadabra", "BRA") ก็ได้ 1
def first_index_of(s,t):
    return s.lower().find(t.lower())