# Lab 3
# Programmer: Chris Vaisnor
# OS: Linux Ubuntu 20.04 LTS
# Python Version: 3.8.10

### Program Description ###
"""This is my program for Lab 3 - A Huffman Encoding Tree.
The user prompted to enter the name of the file with the character frequency table.
The program will read the frequency file and create a Huffman Tree.

----- Main Menu -----
If they choose to encode/decode a file, the user will be prompted to enter the name of the file to encode/decode.
The program will read the file and encode/decode it using the Huffman Tree.
The program will print out the input text and the encoded/decoded text to the console.
The program will prompt the user if they would like to write the encoded/decoded text to a file.

The user can manually encode/decode text using the Huffman Tree.
The user can print the Huffman Tree in preorder traversal.
The user can quit the program at any time."""

from user_utils_inputs import get_frequency_text, get_user_mode, get_clear_text_file, get_encoded_text_file
from user_utils_outputs import write_encoded_text, write_decoded_text
from tree_functions import create_huffman_tree, print_huffman_tree, encode_string, decode_string

def main():
	"""This is the main function."""

	# get the name of the frequency file, returns a dictionary of the character frequency
	frequency_dict = get_frequency_text()
	
	if frequency_dict == 'Q': # if Quit is chosen
		print('Exiting program...')
		return

	print('(Punctionation is not included in the frequency table and will be ignored)')
	print()

	# create a Huffman Encoding Tree from frequency dictionary
	huffman_tree = create_huffman_tree(frequency_dict)

	while True:
		print('-----------------------Main Menu-----------------------')
		print()
		
		mode = get_user_mode() # get user mode preference
		print()

		if mode == 'P': # print the tree
			print('This is the Huffman Encoding Tree Printed in Preorder.')
			print('----------- Root, Left Child, Right Child -----------')
			print()
			print_huffman_tree(huffman_tree) # recursive function to print the tree
			print()
			continue

		elif mode == 'E': # file mode - Encode
			clear_text = get_clear_text_file()
			print()
			
			encoded_text = encode_string(clear_text, huffman_tree) # pass in clear text and tree
			print()
			
			write_encoded_text(clear_text, encoded_text) # prompt for write to file
			print()
			continue

		elif mode == 'D': # file mode - Decode
			encoded_text = get_encoded_text_file()

			decoded_text = decode_string(encoded_text, huffman_tree) # pass in encoded text and tree

			write_decoded_text(encoded_text, decoded_text) # prompt for write to file
			print()
			continue

		elif mode == 'ME': # Manual Mode - Encode
			while True:
				manual_text = input("Enter text to encode or '!' to return to menu: ")
				print()
				if manual_text == '!':
					break
				encode_string(manual_text, huffman_tree)
				print()
				continue

		elif mode == 'MD': # Manual Mode - Decode
			while True:
				manual_text = input("Enter text to decode (string of 0's & 1's) or '!' to return to menu: ")
				print()
				if manual_text == '!':
					break
				decode_string(manual_text, huffman_tree)
				print()
				continue
		
		elif mode == 'Q': # quit the program
			print('Exiting program...')
			break

		else: # end of Main Menu while loop
			print('Invalid input. Please try again.')
			print()
			continue


if __name__ == '__main__': # driver of the program
	print('Lab 3 - Huffman Encoding Tree')
	print('Programmer: Chris Vaisnor')
	print()

	main() # call the main function
