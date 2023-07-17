def encode(encode_string):  # should add 3 to each number in string
    password = ''  # inputs string and outputs string
    for element in encode_string:
        element = int(element)
        element += 3
        if element >= 10:  # i added this if statement because the password would encode 9 into 12 but the program only wants the digits to be from 0 to 9
            element -= 10
        element = str(element)
        password += element
        #  deleted the "continue" because it was redundant
    return password


def decoder(decoded_string):  # made function to decode password
    decoded_password = ''
    for element in decoded_string:  # iterates through the string
        element = int(element)
        element -= 3  # decodes the element
        if element < 0:  # since the math makes it possible to form a negative digit,
            element += 10  # add 10 to bring it to the correct digit
        element = str(element)  # return element to string then add to the empty string variable
        decoded_password += element
    return decoded_password


def main():
    #  I removed both variables here that stored "None" since they are redundant
    while True:
        "\n"
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit\n")
        #  "\n" doesn't do anything, I moved it into the print above in order for it to actually print
        menu_option = int(input("Please enter an option: "))
        if menu_option == 1:
            encode_string = input("Please enter your password to encode: ")
            encoded_password = encode(encode_string)
            print("Your password has been encoded and stored!\n")  # added \n to print space before printing menu again in the new loop
        elif menu_option == 2:
            decoded = decoder(encoded_password)  # made a variable to store decoded password
            print(f"The encoded password is {encoded_password}, and the original is {decoded}.\n")  # your variables here for the f-string were wrong, I fixed them
        elif menu_option == 3:
            quit()


if __name__ == '__main__':
    main()
