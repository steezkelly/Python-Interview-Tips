#Two Line Recursion: String Reversal

# while True: Keeps the program running until if conditional
while True:
    stringToReverse = input('Enter string to reverse: ')

    def reverse(stringToReverse):
        if len(stringToReverse)==1: return stringToReverse
        return reverse(stringToReverse[1:]) + stringToReverse[0]

    print(reverse(stringToReverse))

#Exits the program loop
    if stringToReverse == 'q':
        break
