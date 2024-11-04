secret_number = 777

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")
while True:
    number = int(input("Введіть ціле число: "))
    if number == secret_number:
        print("Молодець, магле! Тепер ти вільний")
        break
    else:
        print("Ха-ха! Ви застрягли у моїй петлі!")