'''
For the caesar cipher, I took the ascii values of a lowercase version of the letter and subtracted it by the shift.
If the subtracted value was below the ascii value of a, i subtracted the difference between Z and (a and the subtracted value) so that it loops around the alphabet
I then checked for uppercase and subtracted it by 32 to obtain the ascii value of the uppercase letter.
I checked if the letter was in the alphabet using a hardcoded list. 
If the letter was in the list, I applied the shift. If it wasn't i didn't change it.
'''
def decrypt_caesar(text: str, shift: int) -> str:
    textlist = list(text)
    newlist = []
    for i in textlist:
        if ord(i.lower()) >= ord('a') and ord(i.lower()) <= ord('z'):
            newascvalue = ord(i.lower()) - shift%26
            if newascvalue < ord('a'):
                newascvalue = ord('z') - (ord('a') - newascvalue) + 1
            if i.isupper():
                newascvalue -= 32
            newlist.append(chr(newascvalue))
        else:
            newlist.append(i)
    return "".join(newlist)
def main() -> None:
    text = input("Enter a text to decipher: ")
    print(decrypt_caesar(text, 3))
'''
For the atbash cipher, I took a similar approach to the caesar, and found the difference between the ascii values of the lowercase letter and a.
I subtracted the ascii value of z from this difference, and subtracted 32 if it was uppercase.
If it wasn't a letter, I didn't change it.
I returned a string using the join() function.
'''
def decrypt_atbash(text: str) -> str:
    textlist = list(text)
    newlist = []
    for i in textlist:
        if ord(i.lower()) >= ord('a') and ord(i.lower()) <= ord('z'):
            newascvalue = ord('z') - (ord(i.lower()) - ord('a'))
            if i.isupper():
                newascvalue -= 32
            newlist.append(chr(newascvalue))
        else:
            newlist.append(i)
    return "".join(newlist)
'''
For the a1z26 cipher, I created 3 three lists. One for the text, one for all numbers between 0 and 26 and one for the return string.
I then created a temp variable that will come into play later.
I looped through the list, and looked for numbers. If i founf a number, I looked for the next character and checked if it was a number as well.
If it was, i stored the index of the next char as a temp so that it skips in the next iteration.
Then I checked if it wasn't a dash, so i could add all punctuation and leters.
Then i returned a joined newlist
'''
def decrypt_a1z26(text: str) -> str:
    textlist = list(text)
    numlist = [str(i) for i in range(0, 27)]
    newlist = []
    temp = 10000000
    for i in range(0, len(textlist)):
        if textlist[i] in numlist:
            if i < len(textlist)-1:
                if textlist[i+1] in numlist:
                    newlist.append(chr(int(textlist[i]+textlist[i+1])+64))
                    temp = i + 1
                else:
                    if i != temp:
                        newlist.append(chr(int(textlist[i])+64))
            else:
                if i != temp:
                    newlist.append(chr(int(textlist[i])+64))
        elif textlist[i] != "-":
            newlist.append(textlist[i])
    return "".join(newlist)


def main() -> None:
    text = input("Enter a text to decipher: ")
    print("Let's try all the methods we have:")
    print(f"Caesar Cipher: {decrypt_caesar(text, 3)}\nAtbash Cipher: {decrypt_atbash(text)}\nA1Z26 Cipher: {decrypt_a1z26(text)}")

main()