#EX7-1.1
#จงเขียนฟังก์ชัน is_palindrome(s) ตรวจว่า s เป็น palindrome หรือไม่ 
#(palindrome คือสตริงที่มีลำดับอักขระจากซ้ายไปขวา เหมือนกับลำดับอักขระจากขวาไปซ้าย เช่น ABBA หรือ 12-343-21)
def is_palindrome(s):
    return s == s[::-1]

#EX7-1.2
#จงเขียนฟังก์ชัน ngrams(s, n) ที่คืนลิสต์ของตัวอักขระ n ตัวติดกันทุกแบบใน s 
#เริ่มจากซ้ายไปขวา เช่น ngrams("ABCDEF", 3) ได้ ["ABC", "BCD", "CDE", "DEF"]
def ngrams(s, n):
    ng = []
    for i in range(len(s)-n+1):
        ng.append(s[i:i+n])
    return ng

#EX7-1.3
#จงเขียนฟังก์ชัน strip_all(s, c) ที่คืนสตริงที่เหมือน s แต่ลบอักขระที่เก็บในสตริง c ออกหมด 
#เช่น strip_all("I-dont-know-how-to-code-this", "-") จะคืนสตริง "Idontknowhowtocodethis"
def strip_all(s, c):
    t = ""
    for ch in s:
        if ch != c:
            t += ch
    return t

#EX7-1.4
#จงเขียนฟังก์ชัน zero_pad(n, d) มี n และ d เป็นจำนวนเต็ม ฟังก์ชันนี้คืนสตริงที่เก็บเลขเหมือนที่ปรากฎใน n แต่จะเติมเลข 0 ทางซ้ายให้สตริงที่ได้มีความยาว d (ถ้า n มีอย่างน้อย d หลักอยู่แล้ว ก็ไม่ต้องเติม) 
#เช่น zero_pad(123, 5) จะได้ "00123" ในขณะที่ zero_pad(123, 2) จะได้ "123"
def zero_pad(n, d):
    return ("0"*d + str(n))[-max(d,len(str(n))):]

#EX7-1.5
#จงเขียนฟังก์ชัน thousands_separator(n) รับจำนวนเต็ม n เพื่อคืนสตริงที่มีเลขเหมือน n แต่จะเติม comma คั่นตามหลักการเขียนจำนวนที่ใช้กันทั่วไป 
#เช่น thousands_separator(1234567) จะได้ "1,234,567"
def thousands_separator(n):
    x = str(n)[::-1]
    s = ""
    for i in range(0, len(x), 3):
        s += x[i:i+3] + ","
    return s[:-1][::-1]


