"""This is the script that contains the functions for gathering user input."""


def get_frequency_text() -> dict:
	"""This function prompts the user for the name of the character frequency file and returns the character frequency
	in a dictionary. """
	while True:
		file_input = input("Enter file name containing character frequencies or Q to (Q)uit: ")
		if file_input.endswith('.txt'):
			break
		
		if file_input.upper() == 'Q':
			return 'Q'

		else:
			print("Error: File name not recognized. Format should be 'filename.txt' Please try again.")
			print()  # blank line
			continue

	# read the input file and returns a dictionary of character frequencies
	frequency_dict = {}
	with open(file_input, 'r') as f_in:
		for line in f_in:
			line = line.strip()  # remove whitespace before and after the line
			line = line.replace(' ', '')  # remove spaces from the line
			line = line.split('-')  # split the character from the frequency at the '-'
			# At this point, each line is in format ['character', 'frequency']
			# add the character and frequency to the dictionary
			frequency_dict[line[0]] = int(line[1])
	return frequency_dict


def get_clear_text_file() -> str:
	"""This function prompts the user for the name of the clear text file and returns the contents."""
	while True:
		file_input = input("Enter file name containing regular text to encode: ")
		if file_input.endswith('.txt'):
			break
		else:
			print("Error: File name not recognized. Format should be 'filename.txt' Please try again.")
			print()  # blank line
			continue

	with open(file_input, 'r') as f_in:
		clear_text = f_in.read()

	return clear_text


def get_encoded_text_file() -> str:
	"""This function prompts the user for the name of the encoded text file and returns the contents."""
	while True:
		file_input = input("Enter file name of text to decode: ")
		if file_input.endswith('.txt'):
			break
		else:
			print("Error: File name not recognized. Format should be 'filename.txt' Please try again.")
			print()  # blank line
			continue

	with open(file_input, 'r') as f_in:
		encoded_text = f_in.read()

	return encoded_text


def get_user_mode() -> str:
	"""This function prompts the user for the mode of the program and returns the mode."""
	
	print('What mode would you like to run the program in? Enter corresponding letter(s):')
	print()
	
	while True:
		print('(E) Encode a file, (D) Decode a file, (ME) Manual Encode, (MD) Manual Decode.')
		mode = input("(P) Print Huffman Binary Tree in Preorder Traversal, (Q) to Quit: ")
		mode = mode.upper()

		if mode == 'E' or mode == 'D' or mode == 'ME' or mode == 'MD' or 'P' or mode == 'Q':
			return mode
		
		else:
			print("Error: Mode not recognized. Please try again.")
			print()  # blank line
			continue
