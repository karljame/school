yes_no = ["yes", "no"]
directions = ["left" , "right", "forward", "backwards"]

user_name = input("whats your name?")
print("hello," + user_name)
response = ""
while response not in yes_no:
    response = input("woude like do play a game?/yes/no/")
    if response == "yes":
        print("ha-sa your adventure starts at the chell")
    elif response == "no":
        print("goodbye")
    else:
        print("wrong its yes or no/ ")
    
response = ""
while response not in directions:
    print("to your left, theres a wall that you can push ")
    print("to your right, theres a wall where theres a rat hole in it")
    print("staright forword, theres chell bars that are rusti you can wait it out to disappeared")
    print("behinde you , you find a  ")
directions = input("which one do you pick left/right/forword/behinde you"):
    if response == "left":
        print("you push the wall and it breaks you find out that its made of some strange material callde LEGO")
    elif response == "right":
        print("you go through the rat hole and you find yourself in a strange place a giant picks you up and squeezed till you die")
    elif response == "forword":
        print("you wait for houers until you feel a earthquak and a someone picks the chell bars up and eats them")
    elif response == "behinde you":
        print("")

    
