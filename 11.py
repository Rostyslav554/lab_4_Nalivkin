blocks = int(input("Введіть кількість блоків: "))

height = 0
blocks_in_layer = 1

while blocks >= blocks_in_layer:
    blocks -= blocks_in_layer
    height += 1
    blocks_in_layer += 1
print("The height of the pyramid:", height)
