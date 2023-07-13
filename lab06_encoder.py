
def encode(encode_string):  # should add 3 to each number in string
	password = ''  # inputs string and outputs string
	for element in encode_string:
		element = int(element)
		element += 3
		element = str(element)
		password += element
		continue
	return password

def decoder(decoded_string):
	pass

def main():
	decoded = None
	encode_string = None  # stores original input
	while True:
		"\n"
		print("Menu")
		print("-------------")
		print("1. Encode")
		print("2. Decode")
		print("3. Quit")
		"\n"
		menu_option = int(input("Please enter an option: "))
		if menu_option == 1:
			encode_string = input("Please enter your password to encode: ")
			encode(encode_string)
			print("Your password has been encoded and stored!")
		elif menu_option == 2:
			print(f"The encoded password is {decoded}, and the original is {encode_string}.")
		elif menu_option == 3:
			quit()

if __name__ == '__main__':
	main()

