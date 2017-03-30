class BinaryTreeNode:

	left = ""
	right = ""
	data = ""
	terminating = False

	#The constructor... Theis class is an object to contain the variables for the left and right node as well as the data and wether it is terminating.
	def __init__(self, left, right, data, terminating):
		self.left = left
		self.right = right
		self.data = data
		self.terminating = terminating
