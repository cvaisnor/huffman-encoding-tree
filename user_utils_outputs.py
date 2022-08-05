"""The script contains the functions for writing the encoded/decoded text to console/file."""


def write_encoded_text(clear_text: str, encoded_text: str):
	"""This function prompts the user for the name of the output text file and writes the contents to a file. """
	
	prompt = input('Would you like to write the clear and encoded text to a file? (Y/N): ').upper()
	if prompt == 'Y':
		while True:
			file_input = input("Enter file name to write contents to: ")
			if file_input.endswith('.txt'):
				break
			else:
				print("Error: File name not recognized. Format should be 'filename.txt' Please try again.")
				print()  # blank line
				continue

		with open(file_input, 'w') as f_out:
			f_out.write('The clear text is: ')
			f_out.write('\n')
			f_out.write(clear_text)
			f_out.write("\n")
			f_out.write("\n")
			
			f_out.write('The encoded text is: ')
			f_out.write('\n')
			f_out.write(encoded_text)
			print("\nThe clear text and encoded text have been written to the file: " + file_input)
			print('Returning to main menu...')
	else:
		print('Returning to main menu...')
	
	return


def write_decoded_text(encoded_text: str, decoded_text: str):
	"""This function prompts the user for the name of the output text file and writes the contents to a file. """
	
	prompt = input('Would you like to write the encoded and decoded text to a file? (Y/N): ').upper()
	if prompt == 'Y':
		while True:
			file_input = input("Enter file name to write decoded text to: ")
			if file_input.endswith('.txt'):
				break
			else:
				print("Error: File name not recognized. Format should be 'filename.txt' Please try again.")
				print()  # blank line
				continue

		# write the encoded text and decoded text to a file
		with open(file_input, 'w') as f_out:
			f_out.write('The encoded text is: ')
			f_out.write('\n')
			f_out.write(encoded_text)
			f_out.write("\n")
			f_out.write("\n")

			f_out.write('The decoded text is: ')
			f_out.write("\n")
			f_out.write(decoded_text)
			print("\nThe encoded text and decoded text have been written to the file: " + file_input)
			print('Returning to main menu...')
	else:
		print('Returning to main menu...')

	return
