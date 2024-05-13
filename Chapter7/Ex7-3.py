#Ex7-3.1
#จงเขียนฟังก์ชัน dedent(line) ที่คืนสตริงใหม่ที่มีค่าภายในเหมือน line แต่ลดจำนวนช่องว่างเฉพาะที่อยู่ติดกันทางซ้ายสุดลงครึ่งหนึ่ง 
#เช่น dedent("        a =    0") ได้ "  a =    0"
def dedent(line):
    c = 0
    for e in line:
        if e != " ":
            break
        c += 1
    return line[c//2:]

#Ex7-3.2
#จงเขียนฟังก์ชัน rot5_digits(s) ที่คืนสตริงใหม่ที่มีค่าภายในเหมือน s แต่เปลี่ยนเฉพาะตัวเลขข้างในจากเลข 0,1,2,3,4,5,6,7,8 และ 9 เป็น 5,6,7,8,9,0,1,2,3 และ 4 ตามลำดับ 
#เช่น rot5_digits("My number is 02-218-6981") ได้ "My number is 57-763-1436"
def rot5_digits(s):
    rot5 = ""
    for e in s:
        if "0" <= e <= "9":
            rot5 += str((int(e)+5) % 10)
        else:
            rot5 += e
    return rot5

#Ex7-3.3
#สตริง DNA เป็นสตริงที่มีตัวอักษรแค่ A, T, G และ C เท่านั้น จงเขียนฟังก์ชัน count_bases(dna) คืนลิสต์ที่เก็บจำนวนเบสที่พบใน dna 
#โดยเก็บจำนวนของ A, T, G และ C ในช่องที่ 0, 1, 2, และ 3 ตามลำดับของลิสต์ที่คืน เช่น count_bases("AAAATTTGGC") ได้ [4, 3, 2, 1]
def count_bases(dna):
    bases = "ATGC"
    freq= [0,0,0,0]
    for e in dna:
        freq[bases.index(e)] += 1
    return freq


