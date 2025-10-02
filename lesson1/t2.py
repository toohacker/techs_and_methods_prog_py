s = 0
while True:
    try:
        n = int(input("Введите число: "))
        s += n
    except ValueError:
        print("Enter a num! please ")
        continue
    if n == 0:
        print(s)
        break
