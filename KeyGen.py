import random

length = int(input("Length of key: "))

for i in range(0, length):
    print(random.randint(1, 94), end="")
    if not i == length -1:
        print(", ", end="")
print("")
