import BinaryTreeNode

#Create nodes takes an array of lines and the line number to start from and creates a node and adds its childs nodes
def createNodes(lines, lineNum):
	node = None
	#The data for the lines are splited by commas in the way comment line, yes line num, no line num, data
	data = lines[int(lineNum)].split(",")
	#If the len of the data is not valid it's an invalid file
	if len(data) != 4:
		print ("Not valid file")
		return None
	else:
		#Then create the node by parsing in the nodes unless its a terminating noe then set the child nodes to none as well as this the node is given its data and has a boolean value for if it is terminating
		node = BinaryTreeNode.BinaryTreeNode(createNodes(lines, data[1]) if data[1] != "-" else None, createNodes(lines, data[2]) if data[2] != "-" else None, data[3], True if data[1] == "-" else False)
	return node

#Creates a binary tree from a file path
def createBinaryTree(file):
	#Open the file in read mode
	fileReader = open(file, "r")
	#Read and split into an array at the newline values
	f = fileReader.read().split("\n")

	#The tree is created by calling the createNodes function
	tree = createNodes(f, 0)
			
	#Return tree
	return tree
