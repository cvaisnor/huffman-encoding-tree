"""The script contains the functions for writing the encoded/decoded text to console/file."""


def write_encoded_text(clear_text, encoded_text):
	"""This function prompts the user for the name of the output text file and writes the contents to both the console
	and a file. """
	while True:
		file_input = input("Enter file name to write encoded text to: ")
		if file_input.endswith('.txt'):
			break
		else:
			print("Error: File name not recognized. Format should be 'filename.txt' Please try again.")
			print()  # blank line
			continue

	with open(file_input, 'w') as f_out:
		f_out.write(clear_text)
		f_out.write("\n")
		f_out.write(encoded_text)
	return


def write_decoded_text(encoded_text, decoded_text):
	"""This function prompts the user for the name of the output text file and writes the contents to both the console
	and a file. """
	while True:
		file_input = input("Enter file name to write decoded text to: ")
		if file_input.endswith('.txt'):
			break
		else:
			print("Error: File name not recognized. Format should be 'filename.txt' Please try again.")
			print()  # blank line
			continue

	print("\nThe encoded text is:")
	print(encoded_text)
	print("\nThe decoded text is:")
	print(decoded_text)

	# write the encoded text and decoded text to a file
	with open(file_input, 'w') as f_out:
		f_out.write(encoded_text)
		f_out.write("\n")
		f_out.write(decoded_text)
	return
