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
        if i.lower() in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']:
            newascvalue = ord('z') - (ord(i.lower()) - ord('a'))
            if i.isupper():
                newascvalue -= 32
            newlist.append(chr(newascvalue))
        else:
            newlist.append(i)
    return "".join(newlist)


def main() -> None:
    text = input("Enter a text to decipher: ")
    print("Let's try all the methods we have:")
    print(f"Caesar Cipher: {decrypt_caesar(text,3)}\nAtbash Cipher: {decrypt_atbash(text)}")

main()