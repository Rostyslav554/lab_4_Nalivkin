c0 = int(input("Введіть будь-яке невід’ємне та ненульове ціле число: "))

steps = 0

if c0 > 0:
    while c0 != 1:
        print(c0)
        if c0 % 2 == 0:
            c0 = c0 // 2
        else:
            c0 = 3 * c0 + 1
        steps += 1
    print(c0)
    print("Кількість кроків:", steps)
else:
    print("Будь ласка, введіть будь-яке невід’ємне та ненульове ціле число.")
