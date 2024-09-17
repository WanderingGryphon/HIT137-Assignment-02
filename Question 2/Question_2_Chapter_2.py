def isolation_of_translate(s):
    string_of_numbers = ''.join(filter(str.isdigit, s))
    string_of_letters = ''.join(filter(str.isalpha, s))
    
    even_numbers_ascii_code = [ord(c) for c in string_of_numbers if int(c) % 2 == 0]
    uppercase_ascii = [ord(c) for c in string_of_letters if c.isupper()]
    
    print("Number String should be :", string_of_numbers)
    print("Letter String should be :", string_of_letters)
    print("Even Numbers ASCII code should be :", even_numbers_ascii_code)
    print("Uppercase Letters ASCII code should be :", uppercase_ascii)
    
# the overall sample is given following
s = '56aAWW1984sktr235270aymn145ss785fsq31D0'
isolation_of_translate(s)

def decrypt_the_cryptogram(cryptogram):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    # Here,I am trying provide each possible shift
    for shiftroaster in range(26):
        decrypted = ''
        for allchar in cryptogram:
            if allchar in alphabet:
                # Find the corresponding letter after shifting
                original_index = alphabet.find(allchar)
                shifted_index = (original_index - shiftroaster) % 26
                decrypted += alphabet[shifted_index]
            else:
                decrypted += allchar
        
        print(f"Shift {shiftroaster}: {decrypted}")

# Cryptogram Example
cryptogram = "VZ FRYSVFU VZCNGVRAG NAQ N YVGGYR VAF RPHER V ZNXR ZNXR ZVF GNXRF V NZ BHG BS PBAGEBY NAQNG GVZRF UNEQ GB UNAQYR OHG VS LBH PNAG UNAQYR ZR NG ZL JBEFG GURA LBH FHER NF URYYQBAG QRFREIR ZR NG ZL ORFG ZNEVYLA ZBAEBR"
decrypt_the_cryptogram(cryptogram)
