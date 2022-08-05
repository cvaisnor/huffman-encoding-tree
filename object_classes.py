"""This script contains the object classes. A priority queue is used to add nodes 
to the tree such that the lowest frequency node is at the top of the queue."""


class HuffmanNode:
	"""This is the class for the Huffman Encoding Node/Tree."""

	def __init__(self, frequency, character, left_child, right_child):
		"""This is the constructor for a Huffman Node.
		Each node has: frequency, character, left child, right child."""

		self.frequency = frequency
		self.character = character
		self.left_child = left_child
		self.right_child = right_child	

	def print_node(self):
		"""This function prints the individual node to the console."""

		print('This node contains:')
		print('Frequency:', self.frequency)
		print('Character:', self.character)
		print('Left Child:', self.left_child.character)
		print('Right Child:', self.right_child.character)


class PriorityQueue:
	"""This is a class for a priority queue. The top node is the node with the lowest frequency."""
	
	def __init__(self):
		"""This is the constructor for a priority queue."""
		self.queue = []

	def enqueue(self, node: HuffmanNode):
		"""This function adds a node to the priority queue."""
		self.queue.append(node)
		self.queue.sort(key=lambda x: x.frequency)

	def dequeue(self):
		"""This function removes the top node from the priority queue."""
		return self.queue.pop(0)

	def print_queue(self):
		"""This function prints the priority queue to the console."""

		print('Priority Queue:')
		for node in self.queue:
			node.print_node()
		print()
