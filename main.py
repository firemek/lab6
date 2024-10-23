def decode(encoded):
    decoded_password = ""
    for char in encoded:
        new_c = str((int(char)-3)%10)
        decoded_password += new_c
    return decoded_password

def encode(password):
    temp = []
    output = ""
    for i in range(0, len(password)):  # for every character in the password
        temp.append(int(password[i])) # adds it to temp list
    for a in range(0, len(temp)):  # for every item in the temp list
        temp[a] = temp[a] + 3  # adds 3 to every number
        output += str(temp[a])  # adds every item in the list into output string

    return output


if __name__ == '__main__':
    x = 0  # variable to start

    while x == 0:
        print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit")  # prints out menu
        user_selection = int(input("\nPlease enter an option: "))  # prompts user for menu selection
        user_password = input("Please enter your password to encode: ") # prompts user for the password to encode

        if user_selection == 1:  # runs user_password into encode function
            user_password = encode(user_password)
            print("Your password has been encoded and stored!")

        elif user_selection == 2:  # runs user_password into decode function
            # TODO: function to decode
            pass
        elif user_selection == 3: # terminates the program
            x = 1
