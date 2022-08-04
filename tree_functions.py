"""These are the functions that act on the Huffman Encoding Tree."""
from object_classes import HuffmanNode, PriorityQueue


# function to print the nodes of a Huffman Encoding Tree in preorder traversal
def print_huffman_tree(tree : HuffmanNode):
	"""This function prints the nodes of a Huffman Encoding Tree in preorder traversal. (Root, Left, Right) """

	print('Root:', tree.character, ',', tree.frequency)

 # base case, leaf node
	if tree.left_child is None and tree.right_child is None:
		print('This is a leaf node.')
		print()
		return 
	
	# if the left child exists, print the left child
	if tree.left_child is not None:
		print('Root -> Left Child: ')
		print_huffman_tree(tree.left_child)

	# if the right child exists, print the right child
	if tree.right_child is not None:
		print('Root -> Right Child:')
		print_huffman_tree(tree.right_child)


def create_huffman_tree(frequency_dict: dict):
	"""This function creats a Full Huffman Encoding Binary Tree based on character frequencies from a dictionary using a priority queue.
	The top of the queue is the lowest frequency character. The tree is built by adding the two lowest frequency characters to the tree,
	concatinating the characters, and then adding the two new nodes to the queue with the respective left and right child nodes.
	The tree is built until there is only one node left in the queue."""

	# create a priority queue
	pq = PriorityQueue()

	# add the nodes to the queue
	for character in frequency_dict:
		pq.enqueue(HuffmanNode(frequency_dict[character], character, None, None), frequency_dict[character])

	# while there are more than one node in the queue
	while len(pq.queue) > 1:
		
		# remove the top two nodes from the queues
		node1 = pq.dequeue() # lowest frequency node
		node2 = pq.dequeue() # second lowest frequency node

		# if the nodes have the same frequency, concatenate the characters alphabetically
		if node1.frequency == node2.frequency:
			if node1.character < node2.character:
				concatenated_character = node1.character + node2.character
			elif node2.character < node1.character:
				concatenated_character = node2.character + node1.character
		else:
			concatenated_character = node1.character + node2.character

		# create a new node with the combined characters and frequency
		node = HuffmanNode(node1.frequency + node2.frequency, concatenated_character, node1, node2)

		# add the new node to the queue
		pq.enqueue(node, node.frequency)

	# return the root node of the tree
	return pq.queue[0]


# encode a string using a Huffman Encoding Tree,
def encode_string(input_string, tree : HuffmanNode):
	"""This function encodes a string using a Huffman Encoding Tree. The root is passed in as a parameter.
	The encoding is done by traversing the tree and adding 0 for the left child and 1 for the right child.
	The encoding is returned as a string."""

	print('The clear text is: ')
	print(input_string)
	print()

	# make sure input is upper case
	input_string = input_string.upper()

	# create an empty string
	encoded_string = ''
		
	# traverse the tree per character
	for character in input_string:

		# if new line, go to the next line
		if character == '\n':
			encoded_string += '\n'
			continue
		
		# if character is not in ASCII range A-Z
		if ord(character) not in range(65, 91):
			continue
		
		# start at the root node for each character
		current_node = tree

		# Each left child assignment is 0, each right child assignment is 1
		while len(current_node.character) >= 2: # if the length of the character is greater than 1, it is not a leaf node

			if character in current_node.left_child.character: # if the character is in the left child
				encoded_string += '0'
				if current_node.left_child is None:
					break
				current_node = current_node.left_child
				continue

			elif character in current_node.right_child.character: # if the character is in the right child
				encoded_string += '1'
				if current_node.right_child is None:
					break
				current_node = current_node.right_child
				continue
	
	print('The encoded text is:')
	print(encoded_string)
	
	return encoded_string

# function to decode a string using a Huffman Encoding Tree
def decode_string(input_string, tree : HuffmanNode):
	"""This function decodes a string using a Huffman Encoding Tree. The root is passed in as a parameter.
	The decoding is done by traversing the tree and adding 0 for the left child and 1 for the right child.
	The decoding is returned as a string."""

	print('The encoded text is: ')
	print(input_string)

	# create an empty string
	decoded_string = ''

	# traverse the tree per character
	for character in input_string:

		# if new line, go to the next line
		if character == '\n':
			decoded_string += '\n'
			continue

		if character != '0' or character != '1':
			print('Invalid character, skipping.')
			continue

		# start at the root node
		current_node = tree

		# Each left child assignment is 0, each right child assignment is 1
		while len(current_node.character) >= 2: # if the length of the character is greater than 1, it is not a leaf node

			if character == '0': # if the character is 0
				if current_node.left_child is None:
					break
				current_node = current_node.left_child
				continue

			elif character == '1': # if the character is 1
				if current_node.right_child is None:
					break
				current_node = current_node.right_child
				continue

		# add the character to the decoded string
		decoded_string += current_node.character

	print('The decoded text is:')
	print(decoded_string)

	return decoded_string