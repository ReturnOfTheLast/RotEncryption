from string import ascii_letters, digits, punctuation
from KeyGen import genKey as __gk
import argparse as __ap

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
    parser = __ap.ArgumentParser()
    parser.add_argument("input", metavar="<input>")
    parser.add_argument("-k", dest="key", metavar="<1-94>,...", help="Use specific key")
    parser.add_argument("-d", dest="decode", action="store_true", help="Enable decode mode")
    args = parser.parse_args()
    
    if args.key:
        keyText = args.key
    else:
        keyText = __gk(len(args.input))

    keyList = keyText.split(',')

    for i in range(0, len(keyList)):
        if not args.decode:
            keyList[i] = int(keyList[i])
        else:
            keyList[i] = -int(keyList[i])

    clearText = ""
    clearText = args.input
    cipherText = ""
    
    i = 0
    for c in clearText:
        cipherText += rot_ascii(keyList[i%len(keyList)])(c)
        i += 1
    print("Text: " + cipherText)
    print("Key: " + keyText)