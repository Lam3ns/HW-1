a = int(input("A "))
b = int(input("B "))
while a <= b:
    print(a, end='')


a = int(input("A "))
b = int(input("A "))
while a <= b:
    if a % 2 == 1:
        print(a, end=" ")



a = int(input("A "))
b = int(input("B: "))

if a <= b:
    print(a, b)
    for n in range(a, b + 1):
        if n % 2 == 0:
            print(n)
else:
    print("Помилка")


a = int(input("A "))
b = int(input("B "))
while b >= a:
    print(b, end=" ")
    b -= -1


a = 5
b = 7
t = a
a = b
b = t
print(a, b)
a, b = b, a
print(a, b)

a = int(input("A "))
b = int(input("B "))
if a > b:
    a, b = b, a
while a <= b:
    if a % 2:
        print(a, end=" ")
    a += 1



a = int(input("B "))
b = int(input("A "))

if a <= b:
    print("")
    for n in range(a, b + 1):
        if n % 2 == 0:





1 work (2)
a = int(input("A "))
b = int(input("B "))

s = 0
while a <= b:
    s += a
   a += 1
print("Сума {0}".format(s))
print(f"Сума = {s}")



a = int(input("A "))
b = 1

for i in range(1, a + 1):
    b *= 1

print(f"fact {a} ")



a = int(input("A "))

for i in range(a):
   print('*', end='')


a = int(input("A "))
b = input("B ")

for i in range(a):
    print(b, end='')

print()




a = 1
while a < 10:
    b = 1
    while b < 10:
      print(a * b, end=" ")
      b += 1
    print()
    a += 1


for aqq in bq:
    a = 5
    b = 7
    r = a + b
    print(r)








