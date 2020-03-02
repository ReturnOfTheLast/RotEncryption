from string import ascii_letters, digits, punctuation
import argparse

# Define rot function
def rot(*symbols):
    def _rot(n):
        encoded = ''.join(sy[n:] + sy[:n] for sy in symbols)
        lookup = str.maketrans(''.join(symbols), encoded)
        return lambda s: s.translate(lookup)
    return _rot

# Define alphanumeric rot
rot_ascii = rot(ascii_letters + digits + punctuation + ' ')

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", dest="input", metavar="<inputfile>", required=True)
    parser.add_argument("-o", dest="output", metavar="<outputfile>", required=True)
    parser.add_argument("-k", dest="key", metavar="<1-94>,<1-94>,...", required=True)
    parser.add_argument("-d", dest="decode", action="store_true", help="Enable decode mode")

    args = parser.parse_args()

    inputfile = open(args.input, "r")
    outputfile = open(args.output, "w+")
    key = args.key.split(',')

    for i in range(0, len(key)):
        if not args.decode:
            key[i] = int(key[i])
        else:
            key[i] = -int(key[i])

    clearText = ""
    clearText = inputfile.read()
    inputfile.close()

    cipherText = ""
    i = 0

    for char in clearText:
        cipherText += rot_ascii(key[i%len(key)])(char)
        i += 1
    
    outputfile.write(cipherText)
    outputfile.close()


