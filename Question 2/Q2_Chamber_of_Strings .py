# Function to separate and process string
def process_string(string):

    # Create number string from input string
    number_str = ''.join(filter(str.isdigit, string))

    # Create character string from input string
    letter_str = ''.join(filter(str.isalpha, string))

    # Create even number string from number string
    even_numbers = [int(n) for n in number_str if int(n) % 2 == 0]

    # Convert even number string to ASCII Code Decimal Values
    even_numbers_ascii = [ord(str(n)) for n in even_numbers]

    # Uppercase the character string
    uppercase_letters = [ch for ch in letter_str if ch.isupper()]

    # Convert the uppercase string to ASCII Code Decimal Values
    uppercase_ascii = [ord(ch) for ch in uppercase_letters]

    print(f"Number string: {number_str}")
    print(f"Letter string: {letter_str}")
    print(f"Even Numbers: {even_numbers}")
    print(f"Even Numbers ASCII: {even_numbers_ascii}")
    print(f"Uppercase Letters: {uppercase_letters}")
    print(f"Uppercase ASCII: {uppercase_ascii}")

    return even_numbers, even_numbers_ascii, uppercase_letters, uppercase_ascii


# Function to decipher the cryptogram
def caesar_decrypt(string, shift):
    decrypted_message = []

    if string is None:   # Check for empty string
        print("No cryptogram provided.")
        return ""

    for char in string:
        if char.isalpha():  # Only decrypt alphabetic characters
            # Adjust the base value for uppercase and lowercase letters
            base = ord('A') if char.isupper() else ord('a')

            # Shift the character within its alphabet range
            decrypted_char = chr((ord(char) - base - shift) % 26 + base)
            decrypted_message.append(decrypted_char)
        else:
            decrypted_message.append(char)  # Don't decrypt non-alphabetic characters

    return ''.join(decrypted_message)


# Process String Example
s = '56aAww1984sktr235270aYmn145ss785fsq31D0'
process_string(s)

# Decipher String Example
cryptogram = '''
            VZ FRYSVFU VZCNGVRAG NAQ N YVGGYR VAFRPHER V ZNXR ZVFGNXRF V NZ BHG BS PBAGEBY
            NAQNG GVZRF UNEQ GB UNAQYR OHG VS LBH PNAG UNAQYR ZR NG ZL JBEFG GURA LBH FHER NF
            URYYQBAG QRFREIR ZR NG ZL ORFG ZNEVYLA ZBAEBR
            '''

# Test decryption with different shift values
for shift in range(1, 26):
    print(f"Shift {shift}: {caesar_decrypt(cryptogram, shift)}")
