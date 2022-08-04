# Lab 3
# Programmer: Chris Vaisnor
# OS: Linux Ubuntu 20.04 LTS
# Python Version: 3.8.10

### Program Description ###
"""This is my program for Lab 3 - A Huffman Encoding Tree.
The user will be prompted to enter the name of the file with the character frequency list.
The program will read the frequency file and create a Huffman Tree.


The next prompt will ask if they would like to encode or decode a file.

If they choose to encode a file, the user will be prompted to enter the name of the file to encode.
The program will read the file and encode it using the Huffman Tree.
The program will print out the input text and the encoded text to the console.
The program will also write the input text and encoded text to a file.


If they choose to decode a file, the user will be prompted to enter the name of the file to decode.
The program will read the file and decode it using the Huffman Tree.
The program will print out the input text and the decoded text to the console.
The program will also write the input text and decoded text to a file."""

from user_utils_inputs import get_frequency_text, get_user_mode, get_clear_text, get_encoded_text
from user_utils_outputs import write_encoded_text, write_decoded_text
from tree_functions import create_huffman_tree, print_huffman_tree, encode_string, decode_string

def main():
	"""This is the main function."""

	# get the name of the frequency file, returns a dict of char frequencies
	frequency_dict = get_frequency_text()
	print()
	
	# if Quit is chosen
	if frequency_dict == None:
		print('Exiting program...')
		return

	# create a Huffman Encoding Tree from frequency dictionary
	huffman_tree = create_huffman_tree(frequency_dict)

	
	print('This is the Huffman Encoding Tree Printed in Preorder.')
	print('----------- Root, Left Child, Right Child -----------')
	print()
	print_huffman_tree(huffman_tree)

	while True:
		# get the user's choice of whether to encode/decode a file, manually enter a string, or quit
		mode = get_user_mode()
		print()

		if mode == 'E': # file mode - Encode
			clear_text = get_clear_text()
			
			# pass in tree and clear text to encode
			encoded_text = encode_string(clear_text, huffman_tree) ############## error is occuring here #############

			print('The encoded text is:')
			print(encoded_text)
			
			# prompt for write to file
			write_encoded_text(clear_text, encoded_text)
			continue

		if mode == 'D': # file mode - Decode
			encoded_text = get_encoded_text()

			# pass in tree and encoded text to decode
			decoded_text = decode_string(encoded_text, huffman_tree)

			# print out the input text and decoded text to the console and write to file
			write_decoded_text(encoded_text, decoded_text)

			continue

		if mode == 'ME': # manual encode
			manual_text = input("Enter a text to encode: ").upper() # convert input to uppercase
			print()
			encoded = encode_string(manual_text, huffman_tree)
			print('Encoded text:', encoded)
			print()
			continue

		if mode == 'MD': # manual decode
			manual_text = input("Enter text to decode: ").upper() # convert input to uppercase
			print()
			decoded = decode_string(manual_text, huffman_tree)
			print('Decoded text:', decoded)
			print()
			continue
		
		if mode == 'Q': # quit the program
			print('Exiting program...')
			break
		return


if __name__ == '__main__':
	print('Lab 3 - Huffman Encoding Tree')
	print('Programmer: Chris Vaisnor')
	print()

	main()
