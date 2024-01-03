# กำหนดให้ text = " Welcome " โดย print ออกมาให้อยู่กึ่งกลาง โดยมีความกว้าง 40 และมีตัวอักษรคือ # จากนั้นให้ผู้ใช้งานกรอกข้อมูลเข้ามาแล้วแสดงข้อมูลปกติ
text = " Welcome "

## print
print(text.center(40,"#"))

## รับข้อมูลจากผู้ใช้งาน
user = input("Enter your name : ")

## print
print("Hello",user)