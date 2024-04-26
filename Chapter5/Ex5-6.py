#Ex5-6.1
#โปรแกรมข้างล่างนี้อ่านชื่อย่อจังหวัด ไทยกับอังกฤษ คั่นด้วยช่องว่าง เช่น BKK กทม CMI ชม KBI กบ นำมาสร้างเป็นลิสต์ eng = ["BKK", "CMI", "KBI"] กับลิสต์ th = ["กทม", "ชม", "กบ"] 
#จงเขียนคำสั่งต่อที่อ่านชื่อย่อจังหวัดจากอินพุต ถ้าเป็นชื่อย่อไทย ก็แสดงชื่อย่ออังกฤษ ถ้าเป็นชื่อย่ออังกฤษก็แสดงชื่อย่อไทย ถ้าไม่ใช่ทั้งสอง ก็แสดง Not found
x = input().split()
eng = x[::2]
th = x[1::2]
q = input()
if q in eng:
    i = eng.index(q)
    print(th[i])
elif q in th:
    i = th.index(q)
    print(eng[i])
else:
    print("Not found")


#Ex5-6.2
#โปรแกรมข้างล่างนี้อ่านชื่อย่อจังหวัด ไทยกับอังกฤษ คั่นด้วยช่องว่าง เช่น BKK กทม CMI ชม KBI กบ นำมาสร้างเป็นลิสต์ abbr = [["BKK","กทม"], ["CMI","ชม"], ["KBI","กบ"]] 
#จงเขียนคำสั่งต่อที่อ่านชื่อย่อจังหวัดจากอินพุต ถ้าเป็นชื่อย่อไทย ก็แสดงชื่อย่ออังกฤษ ถ้าเป็นชื่อย่ออังกฤษก็แสดงชื่อย่อไทย ถ้าไม่ใช่ทั้งสอง ก็แสดง Not found
x = input().split()
abbr = []
for i in range(0,len(x),2):
    abbr.append([x[i],x[i+1]])
q = input()
found = False
for e,t in abbr:
    if q == t:
        print(e)
        found = True
    elif q == e:
        print(t)
        found = True
if not found:
    print("Not found")