from string import ascii_letters, digits, punctuation
import time

anim=True

# Define rot function
def rot(*symbols):
    def _rot(n):
        encoded = ''.join(sy[n:] + sy[:n] for sy in symbols)
        lookup = str.maketrans(''.join(symbols), encoded)
        return lambda s: s.translate(lookup)
    return _rot

# Define alphanumeric rot
rot_ascii = rot(ascii_letters + digits + punctuation + ' ')

# Infinite loop for continued use
while True:
    
    # Loop for making sure the right mode is selected
    while True:
        
        # Mode selection
        mode = str(input("Do you want to (E)ncode or (D)ecode: "))
        if mode.lower() == 'e' or mode.lower() == 'd':
            if mode.lower() == 'e':
                modeStr = 'Encode'
    
            if mode.lower() == 'd':
                modeStr = 'Decode'
    
            print("\nYou have chosen to " + modeStr)
            break # Break the loop when we have selected a valid mode
    
        else:
            print("Invalid option")
            continue # Continue the loop if invalid option is selected.
    
    message = input("Enter string to " + modeStr + ": ") # Get the clear text message
    messageList = list(message) # Make a list out of it
    rotNums = []
    print("\nEnter Rot Numbers to " + modeStr.lower() + " the message with separated by commas")
    rotNums = [int(x) for x in input("Rot Numbers (1-94): ").split(',')] # Get the rot numbers, and set it up in an list

    print("")

    lengthCount = 0
    codedMessage = ""
    
    for i in messageList:
        if mode.lower() == 'e':
            codedChar = rot_ascii(int(rotNums[lengthCount%len(rotNums)]))(i) # encode the message using the rot number for this place in the message
        elif mode.lower() == 'd':
            codedChar = rot_ascii(-int(rotNums[lengthCount%len(rotNums)]))(i) # same as above but decode instead

                 
        codedMessage = codedMessage + codedChar # Add encoded character to the coded message
    
        # Some visual feedback of the process
        if anim == True:
            if int(rotNums[lengthCount%len(rotNums)]) < 10:
                print("[" + modeStr + "ROT(0" + str(rotNums[lengthCount%len(rotNums)]) + ")]-[ " + i + " > " + codedChar + " ]: " + codedMessage + message[len(codedMessage):], end = "\r")
            else:
                print("[" + modeStr + "ROT(" + str(rotNums[lengthCount%len(rotNums)]) + ")]-[ " + i + " > " + codedChar + " ]: " + codedMessage + message[len(codedMessage):], end = "\r")

        lengthCount = lengthCount + 1

        if anim == True:
            time.sleep(0.1)

    print("[   " + modeStr + "d   ]-[   |   ]: " + codedMessage) # print coded message
    print("")

    if input("Do you want to do another one? [y/N]: ").lower() == "y":
        print("")
        print("===== *RESTARTING CODER* =====") # Restart because of the infinite loop
        print("")
        continue
    else:
        break