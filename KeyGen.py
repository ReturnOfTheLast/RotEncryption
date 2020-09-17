from random import randint as __ri

def genKey(length):
    key = ""
    for i in range(0, length):
        key += str(__ri(1, 94))
        if i < length - 1:
            key += ","
    return key

if __name__ == "__main__":
    length = int(input("Length of key: "))
    print(genKey(length))
