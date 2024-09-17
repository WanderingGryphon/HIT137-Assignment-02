# Function to calculate the key from the given code
def get_key():
    total = 0
    for i in range(5):
        for j in range(3):
            if i + j == 5:
                total += i + j
            else:
                total -= i - j

    counter = 0
    while counter < 5:
        if total < 13:
            total += 1
        elif total > 13:
            total -= 1
        else:
            counter += 2
    return total

# Decryption function to decrypt the code using the key
def decrypt(encrypted, key):
    decrypted = ''
    for char in encrypted:
        if char.isalpha():
            shifted = ord(char) - key
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26
            decrypted += chr(shifted)
        else:
            decrypted += char
    return decrypted


# Main function to control the flow
def main():
    while True: # Continues until 0 is entered
        try:
            # Get input from user and convert to integer
            user_input = int(input("\nEnter 1 for the encryption key"
                              "\nEnter 2 to decrypt the provided code with key"
                              "\nEnter 3 to fix the decrypted code and show its output"
                              "\nEnter 0 to exit. Enter your number: \n"))

            # Check if input is one of the valid options
            if user_input == 1:
                print('The key is: ', get_key()) # Calculate and display the key
            elif user_input == 2:
                encrypted_code = '''
tybony_inevnoyr = 100
zl_qvpg = { 'xrl1' : 'inyhr1' , 'xrl2' : 'inyhr2' , 'xrl3': 'inyhr3'}

qrs cebprff_ahzoref():
    tybony tybony_inevnoyr
    ybpny_inevnoyr = 5
    ahzoref = [ 1,2,3,4,5]

    juvyr ybpny_inevnoyr > 0:
        vs ybpny_inevnoyr % 2 == 0:
            ahzoref.erzbir(ybpny_inevnoyr)
        ybpny_inevnoyr -= 1

    erghea ahzoref

zl_frg = { 1,2,3,4,5,5,4,3,2,1}
erfhyg = cebprff_ahzoref(ahzoref=zl_frg)

qrs zbqvsl_qvpg():
    ybpny_inevnoyr = 10
    zl_qvpg ['xrl4'] = ybpny_inevnoyr

zbqvsl_qvpg(5)

qrs hcqngr_tybony():
    tybony tybony_inevnoyr
    tybony_inevnoyr += 10

sbe v va enatr(5):
    cevag(v)
    v += 1

vs zl_frg vf abg Abar naq zl_qvpg[ 'xrl4'] == 10:
    cevag("pbaqvgvba zrg!")

vs 5 abg va zl_qvpg:
    cevag("5 abg sbhaq va gur qypgvbanel!")

cevag(tybony_inevnoyr)
cevag(zl_qvpg)
cevag(zl_frg)
        '''

                print('\n-----Decrypted Code Start-----\n')
                print(decrypt(encrypted_code, get_key()))
                print('\n-----Decrypted Code End-----\n')

            elif user_input == 3:
                fixed_code = '''
global_variable = 100
my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}

def process_numbers(numbers):  # Fix: Added 'numbers' parameter to match the function call
    # Fix: Removed global declaration as global_variable is not modifed in this function
    local_variable = 5
           
    while local_variable > 0:
        # Fix: Check if 'local_variable' is in 'numbers' to avoid ValueError
        if local_variable % 2 == 0 and local_variable in numbers:
            numbers.remove(local_variable)
        local_variable -= 1

    return numbers

my_set = {1, 2, 3, 4, 5}  # Fix: Removed duplicate elements, as sets automatically handle duplicates
result = process_numbers(my_set)  # Fix: Removed the redundant 'numbers='

def modify_dict():  
    local_variable = 10
    my_dict['key4'] = local_variable  

modify_dict()  # Fix: Removed the argument as the function does not accept any arguments

def update_global():
    global global_variable
    global_variable += 10

for i in range(5):
    print(i)
    # Fix: Removed i += 1 as the 'for' loop will do it automatically

if my_set is not None and my_dict['key4'] == 10:
    print("condition met!")

if 5 not in my_dict:
    print("5 not found in the dictionary!")

print(global_variable)
print(my_dict)
print(my_set)
        '''

                print('\n-----Corrected Decrypted Code Start-----\n')
                print(fixed_code)
                print('\n-----Corrected Decrypted Code End-----\n')
                print('\n-----Corrected Decrypted Code Output-----\n')

                global_variable = 100
                my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}

                def process_numbers(numbers):  # Fix: Added 'numbers' parameter to match the function call
                    # Fix: Removed global declaration as global_variable is not modifed in this function
                    local_variable = 5

                    while local_variable > 0:
                        # Fix: Check if 'local_variable' is in 'numbers' to avoid ValueError
                        if local_variable % 2 == 0 and local_variable in numbers:
                            numbers.remove(local_variable)
                        local_variable -= 1

                    return numbers

                my_set = {1, 2, 3, 4, 5}  # Fix: Removed duplicate elements, as sets automatically handle duplicates
                result = process_numbers(my_set)  # Fix: Removed the redundant 'numbers='

                def modify_dict():
                    local_variable = 10
                    my_dict['key4'] = local_variable

                modify_dict()  # Fix: Removed the argument as the function does not accept any arguments

                def update_global():
                    global global_variable
                    global_variable += 10

                for i in range(5):
                    print(i)
                    # Fix: Removed i += 1 as the 'for' loop will do it automatically

                if my_set is not None and my_dict['key4'] == 10:
                    print("condition met!")

                if 5 not in my_dict:
                    print("5 not found in the dictionary!")

                print(global_variable)
                print(my_dict)
                print(my_set)

            elif user_input == 0:
                print("Exiting the program.")
                break  # Exit the loop and terminate the program

            else:
                print("Invalid input. Please enter 1, 2, 3, or 0.")

        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Run the main function
main()