import BinaryTree
import os

def getGameToPlay():
    #Load the files in the games directory
    games = os.listdir("Games")
    #Loop backwards to avoid errors when deleting an item from the lsit
    for i in range(len(games) - 1, 0, -1):
        #Only delete if it is not a ".classification" file
        if games[i][-15:] != ".classification":
            del games[i]

    print("Which game would you like to play?")

    #Print out each game in order in the games array
    for i in range(0, len(games), 1):
        print(i+1, games[i][:-15])

    #Get the game they want and return it and handle errors
    try:
        choice = int(input("Game number: ")) - 1
        if choice >= len(games) or choice < 0:
            print("\n\nNot a valid option...\n")
            return getGameToPlay()
        else:
            return "Games/" + games[choice]
    except ValueError:
        print("\n\nInvalid input... Try again!\n")
        return getGameToPlay()
    

#This works by using a binary tree to laod a file into a tree structure that can be moved through by the user
n = BinaryTree.createBinaryTree(getGameToPlay())

#Print newlines before the start of the game
print("\n\n\n\n")

#As longas we are not in a terminating node we will keep on going through the tree answering questiosn
while n.terminating == False:
	#Get the input in lower case of the user asking the question in the data variable of the node and replacing the escaped newline characters as newline characters
	answer = input (n.data.replace("\\n", "\n") + " ").lower()
	
	#Then check if the answer is yes	
	if answer in ["y", "yes"]:
		#The left side of the tree is the yes side
		n = n.left
	elif answer in ["n", "no"]:
		#If no go down the right side
		n = n.right
	else:
		#Otherwise it's not a valid answer... Tell the naughty people -___-
		print ("Not a valid answer! Only yes and no are allowed!")

#Exit the loop once we are at a terminating node therefore have worked out the animal so tell them!
print ("Your animal is a", n.data)
