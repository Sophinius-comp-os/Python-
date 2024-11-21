#Break Statement
num =20
while num <= 25:
    print(num)

    if num == 23:
        break
    num += 1


#Continue statement

devices= ["Laptop", "phone", "Desktop"]
for x in devices:
    if x == "Laptop":
        continue
    print(x)
