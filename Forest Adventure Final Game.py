#AS91884: USE BASIC ITERATIVE PROCESSES TO DEVELOP A DIGITAL OUTCOME
#PYTHON TEXT-BASED GAME
#"FOREST ADVENTURE"
#BY DANIEL SCOTT


#INITIALISATIONS
import sys #Importing the "System" module allows the Python shell to end the game if the user encounters a "Game Over" or "Game Won" screen, using the "sys.exit()" command, which exits the thread
import time #Importing the "Time" module allows the Python shell to pause the game at certain points in the code, particularly when the player falls unconscious, using the time.sleep(n) command, which inserts a temporary pause


#VARIABLE CREATION
#This is to create variable values for those variables that the code may encounter without the user having gone through a path to create them, which results in an error. 
achievements_list = [] #The user starts the game with zero achievements, and earns them along the way
all_endings = 0 #Checks how many times the user has finished the game with all possible endings in the current playing session, thus only giving them the relevant achievement on the first occurrence
bridge_playthrough = 0 #Checks how many times in one playing session the player has encountered the bridge code, thus only giving them the relevant achievement on the first occurence
cavewin = 0 #Checks how many times in one playing session the player has encountered the cave win ending, thus only giving them the relevant achievement on the first occurence
gamewon = 0 #Checks how many times in one playing session the player has won the game, thus only giving them the relevant achievement on the first occurence
invincible_playthrough = 0 #Checks how many times in one playing session the player has had an invincible path against the slime monster, thus only giving them the relevant achievement on the first occurence
karma = 0 #Sets the user's score to 0 at the start of the game
lost_playthrough = 0 #Checks how many times in one playing session the player has recovered from being lost, thus only giving them the relevant achievement on the first occurence
monster_playthrough = 0 #Checks how many times in one playing session the player has encountered the slime monster, thus only giving them the relevant achievement on the first occurence
orb_of_cagim = 0 #Checks how many times in the current playing session the player has acquired the Orb of Cagim, so that they only receive the relevant achievement on the first occurrence
perfect_citizen = 0 #Checks how many times in one playing session the player has completed the game with a maximum karma score, thus only giving them the relevant achievement on the first occurrence
riddle_occurrence = 0 #Checks how many times in one iteration of the game the player has encountered the riddle, thus printing different messages on later occurences in the same game
riddles_playthrough = 0 #Checks how many times in one playing session the player has solved the riddle, thus only giving them the relevant achievement on the first occurence
riverwin = 0 #Checks how many times in one playing session the player has encountered the river win ending, thus only giving them the relevant achievement on the first occurence
tomatoes_found = 0 #Checks how many times in one playing session the player has found a tomato, thus only giving them the relevant achievement on the first occurence
torch_owned = False #Checks if the user has acquired a torch/flashlight in the current playthrough of the game
werewolf_playthrough = 0 #Checks how many times in one playing session the player has encountered a werewolf, thus only giving them the relevant achievement on the first occurence

#Ending variables
werewolfdeath1 = 0 #Checks how many times in the current playing session the player has experiences the werewolf death version 1 ending, thus only increasing the endings variable on the first occurrence
werewolfdeath2 = 0 #Checks how many times in the current playing session the player has experiences the werewolf death version 2 ending, thus only increasing the endings variable on the first occurrence
lostdeath = 0 #Checks how many times in the current playing session the player has experiences the lost death ending, thus only increasing the endings variable on the first occurrence
riddledeath = 0 #Checks how many times in the current playing session the player has experiences the riddle death ending, thus only increasing the endings variable on the first occurrence
monsterdeath2_1 = 0 #Checks how many times in the current playing session the player has experiences the monster death round 2 version 1 ending, thus only increasing the endings variable on the first occurrence
monsterdeath2_2 = 0 #Checks how many times in the current playing session the player has experiences the monster death round 2 version 2 ending, thus only increasing the endings variable on the first occurrence
monsterdeath3_1 = 0 #Checks how many times in the current playing session the player has experiences the monster death round 3 version 1 ending, thus only increasing the endings variable on the first occurrence
monsterdeath3_2 = 0 #Checks how many times in the current playing session the player has experiences the monster death round 3 version 2 ending, thus only increasing the endings variable on the first occurrence
cavedeathnotorch = 0 #Checks how many times in the current playing session the player has experiences the "cave with no torch" death ending, thus only increasing the endings variable on the first occurrence
cavedeath = 0 #Checks how many times in the current playing session the player has experiences the lost cave death ending, thus only increasing the endings variable on the first occurrence
endings = 0 #Counts the number of different endings which the player has experienced in the current playing session


#FUNCTION DEFINITION
#Define functions so that in the game they are able to be run

#title()
#The "title()" function is used to print the title whenever the game starts. This happens when the user first starts the game, during the Setup stage, and if they choose to restart the game
def title():
    print("""  __                    _               _                 _
 / _|                  | |             | |               | |
| |_ ___  _ __ ___  ___| |_    __ _  __| |_   _____ _ __ | |_ _   _ _ __ ___
|  _/ _ \| '__/ _ \/ __| __|  / _` |/ _` \ \ / / _ \ '_ \| __| | | | '__/ _ \ 
| || (_) | | |  __/\__ \ |_  | (_| | (_| |\ V /  __/ | | | |_| |_| | | |  __/
|_| \___/|_|  \___||___/\__|  \__,_|\__,_| \_/ \___|_| |_|\__|\__,_|_|  \___|""") #Print the title screen - the game's name
    print()
    print()
    global riddle_occurrence #Import the variable riddle_occurrence into the function so it is seen as global, and thus able to be reset to zero
    riddle_occurrence = 0
    global karma #Import the variable karma into the function so it is seen as global, and thus able to be reset to zero at the start of the new game
    karma = 0
    global torch_owned #Import the variable torch_owned into the function so it is seen as global, and thus able to reset to False at the start of the new game
    torch_owned = False

#tutorial()
#The "tutorial_code()" function is used to carry out the tutorial whenever the code commands it to be so. Having the tutorial inside a function makes it easier to run and means that if the code is changed to allow the tutorial to be run from any point in the uture it can be easily accessed
def tutorial_code():
    print("Welcome to the tutorial! Let's keep things incredibly brief, shall we?")
    print("In this game, you will be placed into a fantasy situation, in a forest (hence the game's name).")
    print("You will be offered choices, similarly to in 1990s \"Choose-Your-Own-Adventure\" books.")
    print("You will be told a few possible paths which you can take. Your choices affect the game's outcome.")
    print("Let's have a quick example.")
    print()
    enter = input("Press Enter to have an example ") #Prevents the game from progressing to the next level until the user has pressed the 'enter' key, thus answering the input prompt and continuing the game. Having an "enter" variable not used for anything else means they are able to type before pressing enter without changing anything in the game
    print()
    print("You're on your way to your grandmother's house. Along the way, you encounter a cliff obstructing your path.")
    print("What should you do? You could simply walk aronud the cliff, or you could leap off in an attempt to get to your grandmother's house faster.")
    example_choice = "undefined" #Sets the variable as a value that is not one of those accepted, meaning the while loop is able to run as, while it recognises the variable, it meets the conditions for repeating the loop
    while example_choice != "jump" and example_choice != "around": #The while loop will repetitively ask the user to enter a valid response if their reply to the input prompt is neither "jump" nor "around". The user cannot progress until a valid response is submitted
        example_choice = str(input("Enter \"jump\" to leap off the cliff. Enter \"around\" to walk around the cliff ")) #Ask their user what choice they wish to make in this situation and inform them of possible/valid inputs
        example_choice = example_choice.strip() #Removes all spaces from the front and end of the user's response 
        example_choice = example_choice.lower() #Removes all upper case letters. The above 2 lines are in order to ensure that the user needs to simply spell the word correctly, as the .strip() and .lower() make the variable non-case-sensitive
        if example_choice != "jump" and example_choice != "around": #Remind the user of the valid responses to the question if they do not answer with one of the two options ("yes" or "no"), using an if loop that activates if their response is invalid
            print("Please type either \"jump\" or \"around\".")
    print()
    if example_choice == "jump": #If the user chose to jump rather than around, print the consequences of jumping. 
        print("You leap off the cliff. It is very tall. Some say you are still falling to this day. You fail to reach your grandmother's house.")
    if example_choice == "around": #If the user chose to go around rather than jumping, print the consequences of going around 
        print("You walk around the cliff. You reach your grandmother's house in a matter of minutes and have a relatively fun time.")
    print()
    print("Congratulations! You've finished the tutorial.")
    print("The mechanics in this game are quite simple to understand, so you should now have the hang of it!")
    print("You should be ready to start.")
    enter = input("Press Enter to start the game ") #Prevents the game from progressing to the next level until the user has pressed the 'enter' key, thus answering the input prompt and continuing the game. Having an "enter" variable not used for anything else means they are able to type before pressing enter without changing anything in the game
    print(new_stage) #The new_stage here is to signify the end of the "Tutorial" stage
    print()

#game_over()
#The "game_over()" function runs the code for when the user runs into a game-ending catastrophe, and gives the user the option to restart the game or to quit
def game_over():
    global all_endings #Imports the variable all_endings into the function, making it a global, so it is able to be recognised when altering its value
    if endings == 12: #Only run this section of the code if the player has acquired all possible endings.
        all_endings += 1 #Increase the variable which tracks the number of times the player has completed the game after obtaining all endings
        if all_endings == 1: 
            achievements_list.append("ADDICT:             Find All Possible Endings") #If it is the player's first time acquiring all of the endings, award them the relevant achievement
    print("Game Over.")
    print(new_stage) #The new_stage here is to signify the end of the "Consequences" stage for the cause of game-end
    print()
    time.sleep(2) #Have a temporary 2 second pause before showing the user their options
    restart_loss = 0 #Sets the variable as a value that is not one of those accepted, meaning the while loop is able to run as, while it recognises the variable, it meets the conditions for repeating the loop
    while restart_loss != "1" and restart_loss != "2": #The while loop will repetitively ask the user to enter a valid response for progression if their reply to the input prompt isn't either "1" or "2". The user cannot progress until a valid response is submitted
        print()
        print("To restart the game, enter \"1\".")
        print("Enter \"2\" to quit.")
        restart_loss = str(input("Enter \"3\" to view your achievements. ")) #Ask their user what choice they wish to make and inform them of possible/valid inputs
        restart_loss = restart_loss.strip() #Removes additional spaces from the start and end of the user's response
        if restart_loss == "3": #If the user selects 3, show them the achievements section. However, continue to ask if they wish to leave the game or restart
            achievements()
        if restart_loss != "1" and restart_loss != "2" and restart_loss != "3": #If statement that activates if the user does not input a valid response, reminding the user of the two valid inputs ("1" and "2")
            print()
            print("Please select \"1\", \"2\" or \"3\".")
    if restart_loss == "1": #If the user selected "1" to restart in the game_over() screen, this piece of code will run. Otherwise, the code for if they selected "2" will run
        print()
        print(new_stage) #This new_stage is to signify the end of the game's playthrough
        print()
        title() #The title is shown here to split the two games and show clearly where the new game begins
        game() #The new game is run, as the user has asked to restart the game
    if restart_loss == "2": #If the user selected "2" to quit in the game_over() screen, this piece of code will run. Otherwise, the code for if they selected "1" will run
        print()
        sys.exit() #Exit out of the game's code by exiting the system module, closing the thread and ending the program

#game_won()
#The game_won() function contains the code that informs the user that they have won, and gives them the option to restart the game or quit
def game_won():
    global all_endings #Imports the variable all_endings into the function, making it a global, so it is able to be recognised when altering its value
    if endings == 12: #Only run this section of the code if the player has acquired all possible endings.
        all_endings += 1 #Increase the variable which tracks the number of times the player has completed the game after obtaining all endings
        if all_endings == 1: 
            achievements_list.append("ADDICT:             Find All Possible Endings") #If it is the player's first time acquiring all of the endings, award them the relevant achievement
    print("You have won the game.")
    print(new_stage) #The new_stage here is to signify the end of the "Consequences" stage for the cause of game-end
    time.sleep(2) #Have a temporary 2 second pause before the user sees their options
    restart_won = "undefined" #Sets the variable as a value that is not one of those accepted, meaning the while loop is able to run as, while it recognises the variable, it meets the conditions for repeating the loop
    while restart_won != "1" and restart_won != "2": #The while loop will repetitively ask the user to enter a valid response for progression if their reply to the input prompt isn't either "1" or "2". The user cannot progress until a valid response is submitted
        print()
        print("To restart the game and try for a different ending, enter \"1\".")
        print("Enter \"2\" to quit.")
        restart_won = str(input("Enter \"3\" to view your achievements. ")) #Ask their user what choice they wish to make and inform them of possible/valid inputs
        restart_won = restart_won.strip() #Removes additional spaces from the start and end of the user's response
        if restart_won == "3": #If the user selects 3, show them the achievements section. However, continue to ask if they wish to leave the game or restart
            achievements() #Go to the achievements function
        if restart_won != "1" and restart_won != "2" and restart_won != "3": #If statement that activates if the user does not input a valid response, reminding the user of the two valid inputs ("1" and "2")
            print()
            print("Please select \"1\", \"2\" or \"3\".")
    if restart_won == "1": #If the user selected "1" to restart in the game_over() screen, this piece of code will run. Otherwise, the code for if they selected "2" will run
        print()
        print(new_stage) #This new_stage is to signify the end of the game's playthrough
        print()
        title() #The title is shown here to split the two games and show clearly where the new game begins
        game() #The new game is run, as the user has asked to restart the game    
    if restart_won == "2": #If the user selected "2" to quit in the game_over() screen, this piece of code will run. Otherwise, the code for if they selected "1" will run
        print()
        sys.exit() #Exit out of the game's code by exiting the system module, closing the thread and ending the program

#achievements()
#The achievements() function contains the code which informs the user of the progress they have made and how much more they can potentially make, and is accessible from the game won/lost screens
def achievements():
    print(new_stage) #This new_stage is to signify the end of the game won/lost screen
    print()
    print("Y O U R    A C H I E V E M E N T S")
    print(new_stage) #This new_stage is to signify the start of the achievements section
    print()
    global achievements_list #Imports the variable achievements_list into the function, making it a global, so it is able to be recognised when checking the length
    achievements_count = len(achievements_list) #Find the number of items in the achievements list, and put it in a variable called achievements_count
    print("You have achieved {}/12 achievements.".format(achievements_count)) #Inform the user how many of the 10 achievements they have got, by using the number of items in the list
    print("You have found {}/12 possible endings.".format(endings)) #Inform the user how many of the 12 possible endings they have got, by putting the value for endings in teh {} space
    print(new_stage) #This new_stage is to signify the start of the achievement list
    print()
    if achievements_count != 0: #Only print the list of achievements if the user actually has any. Otherwise, there will just be an empty section, and that would look bad. Therefore, only print this section if the user has achievements
        for i in range(achievements_count):
            print(achievements_list[i]) #The above for loop repeats for each achievement the player has gained in their current playing session, and prints the items from the list of variables, in the order in which they were obtained
        print(new_stage) #This new_stage is to signify the end of the achievements section
        print()
    achievements_menu = 0 #Sets the variable as a value that is not one of those accepted, meaning the while loop is able to run as, while it recognises the variable, it meets the conditions for repeating the loop
    while achievements_menu != "1" and achievements_menu != "2": #The while loop will repetitively ask the user to enter a valid response for progression if their reply to the input prompt isn't either "1" or "2". The user cannot progress until a valid response is submitted
        achievements_menu = str(input("To view all possible achievements, enter 1. To exit the achievements menu, enter 2 ")) #Ask their user what choice they wish to make and inform them of possible/valid inputs
        if achievements_menu != "1" and achievements_menu != "2": #If statement that activates if the user does not input a valid response, reminding the user of the two valid inputs ("1" and "2")
            print()
            print("Please enter either 1 or 2.")
            print()
    if achievements_menu == "1": #If in the above while loop, the user selected "1", perform this section of the code, showing the user a list of all possible achievements. If they selected "2", this is not carried out, and they are returned to the point in the code from which they accessed the function
        print(new_stage)
        print()
        print("A L L    A C H I E V E M E N T S")
        print(new_stage)
        print()
        print("ADDICT:             Find All Possible Endings")
        print("BORN WINNER:        Win Forest Adventure in Two Different Manners")
        print("CHAMPION:           Win Forest Adventure")
        print("ENGINEER:           Create a Bridge")
        print("INVINCIBLE:         Defeat a Monster flawlessly")
        print("NAVIGATOR:          Recover from being Lost")
        print("ORB OF CAGIM:       Find the Orb of Cagim")
        print("PERFECT CITIZEN:    Help Everyone while Winning the Game")
        print("UNDEFEATABLE:       Defeat a Monster")
        print("WEREWOLF HUNTER:    Defeat a Werewolf")
        print("WORDSMITH:          Solve a Riddle")
        print("5+ A DAY:           Find a Tomato") #A list of all possible achievements
        print()
        enter = input("Press Enter to exit ") #Prevents the game from progressing to the next level until the user has pressed the 'enter' key, thus answering the input prompt and continuing the game. Having an "enter" variable not used for anything else means they are able to type before pressing enter without changing anything in the game
    

#KARMA TASKS
#Tasks throughout the game which don't particularly affect the outcome of the game but give the user karma points

#karma_1()
def karma_1():
    print("Before long, you come across a bear.")
    print()
    enter = input("Press Enter to introduce yourself to the bear ") #Prevents the game from progressing to the next level until the user has pressed the 'enter' key, thus answering the input prompt and continuing the game. Having an "enter" variable not used for anything else means they are able to type before pressing enter without changing anything in the game
    print()
    print("The bear replies:   \"Hello there, {}! My name is Roger.\"".format(name)) #The .format(name) here inputs the player's username in the {} space in the print statement
    print("                    \"Can you help me with something?\"")
    print()
    karmatask1 = "undefined" #Sets the variable as a value that is not one of those accepted, meaning the while loop is able to run as, while it recognises the variable, it meets the conditions for repeating the loop
    while karmatask1 != "help" and karmatask1 != "continue": #The while loop will repetitively ask the user to enter a valid response if their reply to the input prompt is neither "help" nor "continue". The user cannot progress until a valid response is submitted
        karmatask1 = str(input("To help Roger, enter \"help\". To ignore him, enter \"continue\" ")) #Ask the user what choice they wish to make in this situation and inform them of possible/valid inputs. Store their answer in a variable to check the answer's validity
        karmatask1 = karmatask1.strip() #Removes all spaces from the front and end of the user's response 
        karmatask1 = karmatask1.lower() #Removes all upper case letters. The above 2 lines are in order to ensure that the user needs to simply spell the word correctly, as the .strip() and .lower() make the variable non-case-sensitive
        if karmatask1 != "help" and karmatask1 != "continue": #Remind the user of the valid responses to the question if they do not answer with one of the two options, using an if loop that activates if their response is invalid
            print()
            print("Please choose either \"help or \"continue\".")
            print()
    global karma #Import the variable karma into the function so it is seen as global, and thus able to be altered
    print(new_stage)
    print()
    if karmatask1 == "continue": #This if loop activates if the user selected the continue option in the while loop
        karma -= 1 #Decrease the player's karma score by one for ignoring a bear in need of help
        print("You ignore Roger's pleas and continue down the path.")
        print("Roger wanders into the bushes, dejected.") #This is the end of the function if you choose to continue. The player is returned from here back to the point in the code from which they came
    elif karmatask1 == "help": #THis if loop activates if the user chose help in the while loop
        karma += 1 #Increase the player's karma score by one for offering to help Roger the bear
        print("Roger replies:      \"Thank you {}! I haven't had any food in several days, and my cubs are starving.".format(greet)) #THe .format(greet) here inserts the player's greeting variable into the {} space
        print("                    \"Can you find some for me?\"")
        print()
        roger_left_right = "undefined" #Sets the variable as a value that is not one of those accepted, meaning the while loop is able to run as, while it recognises the variable, it meets the conditions for repeating the loop
        while roger_left_right != "forward" and roger_left_right != "back": #The while loop will repetitively ask the user to enter a valid response if their reply to the input prompt is neither "forward" nor "back". The user cannot progress until a valid response is submitted
            roger_left_right = input("To search further down the path, enter \"forward\". To go back and look, enter \"back\" ") #Ask the user what choice they wish to make in this situation and inform them of possible/valid inputs. Store their answer in a variable to check the answer's validity
            roger_left_right.strip() #Removes all spaces from the front and end of the user's response 
            roger_left_right.lower() #Removes all upper case letters. The above 2 lines are in order to ensure that the user needs to simply spell the word correctly, as the .strip() and .lower() make the variable non-case-sensitive
            if roger_left_right != "forward" and roger_left_right != "back": #Remind the user of the valid responses to the question if they do not answer with one of the two options, using an if loop that activates if their response is invalid
                print()
                print("Please choose either \"forward\" or \"back\".")
                print()
        print(new_stage)
        print()
        if roger_left_right == "forward": #This part of the code will activate if the player chose to go forward. The player can achieve nothing from doing this. It simply adds time, due to poor decision making
            print("You wander further along the path.")
            print("After several minutes of searching, you have been unable to find anything.")
            print("You return to Roger, dejected.")
            print()
            enter = input("Press Enter to check in the other direction ") #Prevents the game from progressing to the next level until the user has pressed the 'enter' key, thus answering the input prompt and continuing the game. Having an "enter" variable not used for anything else means they are able to type before pressing enter without changing anything in the game
            print()
        print("You walk back along the path.") #Regardless of the player's choice in the while loop, they will access this point in the code, as it is the only direction with lasagna
        print("After a few minutes, you glance into the bushes.")
        print("You see a sign.")
        print("It reads:")
        print()
        print("       LASAGNA:  BACKUP")
        print("     In case of emergency")
        print()
        print("Next to it sits a steaming lasagna.")
        print()
        enter = input("Press Enter to return to Roger with the lasagna ") #Prevents the game from progressing to the next level until the user has pressed the 'enter' key, thus answering the input prompt and continuing the game. Having an "enter" variable not used for anything else means they are able to type before pressing enter without changing anything in the game
        print()
        print("You return to Roger with the lasagna in your arms.")
        print("He smiles at you gratefully.")
        print("Roger says:         \"Thank you {}, you are a true hero.\"".format(name)) #The .format(name) in this print statement prints the user's name in the {} space
        print("                    \"As a sign of my gratitude, please take this item I found.")
        print("                    \"I don't know what to do with it.")
        print()
        print("Roger hands you a surprisingly expensive-looking torch.")
        global torch_owned #Import the variable torch_owned into the function so it is seen as global, and thus able to be altered
        torch_owned = True
        print()
        enter = input("Press Enter to thank Roger and continue down the path ") #Prevents the game from progressing to the next level until the user has pressed the 'enter' key, thus answering the input prompt and continuing the game. Having an "enter" variable not used for anything else means they are able to type before pressing enter without changing anything in the game
        print(new_stage)
        print()
        print("You continue down the path.") #The player is returned from here to the point in the code from which they accessed the function

#karma_2()
def karma_2():
    global karma #Import the variable karma into the function so it is able to be recognised when altering it
    print("You soon come across a squirrel.")
    print("It looks relatively distressed.")
    squirrel = "undefined" #Sets the variable as a value that is not one of those accepted, meaning the while loop is able to run as, while it recognises the variable, it meets the conditions for repeating the loop
    while squirrel != "talk" and squirrel != "ignore": #The while loop will repetitively ask the user to enter a valid response if their reply to the input prompt is neither "talk" nor "ignore". The user cannot progress until a valid response is submitted
        print()
        squirrel = input("To introduce yourself to the squirrel, enter \"talk\". To continue walking, enter \"ignore\" ") #Ask the user what choice they wish to make in this situation and inform them of possible/valid inputs. Store their answer in a variable to check the answer's validity
        squirrel = squirrel.strip() #Removes all spaces from the front and end of the user's response
        squirrel = squirrel.lower() #Removes all upper case letters. The above 2 lines are in order to ensure that the user needs to simply spell the word correctly, as the .strip() and .lower() make the variable non-case-sensitive
        if squirrel != "talk" and squirrel != "ignore": #Remind the user of the valid responses to the question if they do not answer with one of the two options, using an if loop that activates if their response is invalid
            print()
            print("Please select either \"talk\" or \"ignore\".")
    print(new_stage)
    print()
    if squirrel == "ignore": #This section of the code will activate if, in the while loop, the user selected "ignore"
        karma -= 1 #Deduct one from the user's karma score as they made an immoral decision
        print("You continue along the path.") #This is the end of the function if they selected this option, and the player will be returned from here to the section from which they arrived in this function
    elif squirrel == "talk": #This section of code will run if the user selected talk in the enquiry stage
        enter = input("Press Enter to introduce yourself to the squirrel ") #Prevents the game from progressing to the next level until the user has pressed the 'enter' key, thus answering the input prompt and continuing the game. Having an "enter" variable not used for anything else means they are able to type before pressing enter without changing anything in the game
        print()
        print("Squirrel replies:   \"Hello {}, my name's Darryl.\"".format(name)) #The .format(name) here inserts the player's username into the {} space
        print("                    \"Can you please help me?\"")
        print("                    \"I'm stranded on the ground and cannot reach my acorn stash in this tree.\"")
        acorns = "undefined" #Sets the variable as a value that is not one of those accepted, meaning the while loop is able to run as, while it recognises the variable, it meets the conditions for repeating the loop
        while acorns != "help" and acorns != "continue": #The while loop will repetitively ask the user to enter a valid response if their reply to the input prompt is neither "help" nor "continue". The user cannot progress until a valid response is submitted
            print()
            acorns = input("To help Darryl, enter \"help\". To ignore him, enter \"continue\" ") #Ask the user what choice they wish to make in this situation and inform them of possible/valid inputs. Store their answer in a variable to check the answer's validity
            acorns = acorns.strip() #Removes all spaces from the front and end of the user's response
            acorns = acorns.lower() #Removes all upper case letters. The above 2 lines are in order to ensure that the user needs to simply spell the word correctly, as the .strip() and .lower() make the variable non-case-sensitive
            if acorns != "help" and acorns != "continue": #Remind the user of the valid responses to the question if they do not answer with one of the two options, using an if loop that activates if their response is invalid
                print()
                print("Please choose either \"help\" or \"continue\".")
        print(new_stage)
        print()
        if acorns == "continue": #If in the above while loop the user selected to continue, this if loop will be carried out
            karma -= 1 #Deduct one from the user's karma score as they made an immoral decision
            print("You continue along the path.") #This is the end of the function if they selected this option, and the player will be returned from here to the section from which they arrived in this function
        if acorns == "help": #If the user responded to the enquiry with "help", this section of the code will be ran
            karma += 1 #Add one from the user's karma score as they made a moral decision
            print("You allow Darryl to hop into your hand, from which position he then hops onto your shoulder.")
            print()
            enter = input("Press Enter to climb the tree ") #Prevents the game from progressing to the next level until the user has pressed the 'enter' key, thus answering the input prompt and continuing the game. Having an "enter" variable not used for anything else means they are able to type before pressing enter without changing anything in the game
            print()
            print("You start to climb the tree, clambering from branch to branch.")
            print("Around 8 metres off the ground, Darryl taps on your head, and you stop.")
            print("In the tree trunk is a spacious hole, full of acorns.")
            print()
            print("Darryl says:        \"This is my branch.\"")
            print("                    \"Thanks, friend!\"")
            print()
            enter = input("Press enter to descend back down the tree ") #Prevents the game from progressing to the next level until the user has pressed the 'enter' key, thus answering the input prompt and continuing the game. Having an "enter" variable not used for anything else means they are able to type before pressing enter without changing anything in the game
            print()
            print("You reach the ground, back on the path.")
            print("You recommence your walking.") #This is the end of the function if they selected this option, and the player will be returned from here to the section from which they arrived in this function

#karma_3
def karma_3():
    global karma #Import the variable karma into the function so it is able to be recognised when altering it
    print("Sitting on the side of the path is a rabbit.")
    print("It looks rather forlorn.")
    rabbit = "undefined" #Sets the variable as a value that is not one of those accepted, meaning the while loop is able to run as, while it recognises the variable, it meets the conditions for repeating the loop
    while rabbit != "talk" and rabbit != "continue": #The while loop will repetitively ask the user to enter a valid response if their reply to the input prompt is neither "talk" nor "continue". The user cannot progress until a valid response is submitted
        print()
        rabbit = input("Enter \"talk\" to talk to the rabbit. Enter \"continue\" to ignore the rabbit ") #Ask the user what choice they wish to make in this situation and inform them of possible/valid inputs. Store their answer in a variable to check the answer's validity
        rabbit = rabbit.strip() #Removes all spaces from the front and end of the user's response
        rabbit = rabbit.lower() #Removes all upper case letters. The above 2 lines are in order to ensure that the user needs to simply spell the word correctly, as the .strip() and .lower() make the variable non-case-sensitive
        if rabbit != "talk" and rabbit != "continue": #Remind the user of the valid responses to the question if they do not answer with one of the two options, using an if loop that activates if their response is invalid
            print()
            print("Please enter either \"talk\" or \"continue\".")
    print(new_stage)
    print()
    if rabbit == "continue": #If, in the above while loop, the user selected to continue, this code will be carried out
        karma -= 1 #Deduct one from the user's karma score as they made an immoral decision
        print("You turn your attention back to the river.") #This is the end of the function if they selected this option, and the player will be returned from here to the section from which they arrived in this function
    if rabbit == "talk": #If, in the while loop relevant to this question, the player selected to talk, this section of code will be ran
        print("You decide to help the rabbit.")
        print()
        enter = input("Press Enter to introduce yourself to the rabbit ") #Prevents the game from progressing to the next level until the user has pressed the 'enter' key, thus answering the input prompt and continuing the game. Having an "enter" variable not used for anything else means they are able to type before pressing enter without changing anything in the game
        print()
        print("Rabbit replies:     \"Hello there {}, my name is Barbara.\"".format(name)) #The .format(name) here inserts the player's username into the {} space in the print statement
        print("                    \"My carrot here is stuck in the ground, and I can't get it out!\"")
        print("Barbara gestures to the tip of a rabbit sticking out of the Earth to her side.")
        carrot = "undefined" #Sets the variable as a value that is not one of those accepted, meaning the while loop is able to run as, while it recognises the variable, it meets the conditions for repeating the loop
        while carrot != "help" and carrot != "ignore": #The while loop will repetitively ask the user to enter a valid response if their reply to the input prompt is neither "help" nor "ignore". The user cannot progress until a valid response is submitted
            print()
            carrot = input("Enter \"help\" to assist Barbara, or \"ignore\" to carry on with your day ") #Ask the user what choice they wish to make in this situation and inform them of possible/valid inputs. Store their answer in a variable to check the answer's validity
            carrot = carrot.strip() #Removes all spaces from the front and end of the user's response
            carrot = carrot.lower() #Removes all upper case letters. The above 2 lines are in order to ensure that the user needs to simply spell the word correctly, as the .strip() and .lower() make the variable non-case-sensitive
            if carrot != "help" and carrot != "ignore": #Remind the user of the valid responses to the question if they do not answer with one of the two options, using an if loop that activates if their response is invalid
                print()
                print("Please enter either \"help\" or \"ignore\".")
        print(new_stage)
        print()
        if carrot == "ignore": #If, in the above while loop, the user selected "ignore", carry out this section of the code
            karma -= 1 #Deduct one from the user's karma score as they made an immoral decision
            print("You turn your attention back to the river.") #This is the end of the function if they selected this option, and the player will be returned from here to the section from which they arrived in this function
        if carrot == "help": #This if loop will be activated if the user selected help in the above while loop
            karma += 1#Add one to the user's karma score as they made a moral decision
            print("You decide to help Barbara.")
            print()
            print("Press Enter to try and pull the carrot out of the ground.")
            print()
            print("It's stuck.")
            print("This isn't going to work.")
            print("You're going to have to look for something else to get the carrot out with.")
            rabbit_left_right = "undefined" #Sets the variable as a value that is not one of those accepted, meaning the while loop is able to run as, while it recognises the variable, it meets the conditions for repeating the loop
            while rabbit_left_right != "back" and rabbit_left_right != "forward": #The while loop will repetitively ask the user to enter a valid response if their reply to the input prompt is neither "back" nor "forward". The user cannot progress until a valid response is submitted
                print()
                rabbit_left_right = input("Enter \"back\" to look for something behind you along the path, or enter \"forward\" to look further along ") #Ask the user what choice they wish to make in this situation and inform them of possible/valid inputs. Store their answer in a variable to check the answer's validity
                rabbit_left_right = rabbit_left_right.strip() #Removes all spaces from the front and end of the user's response
                rabbit_left_right = rabbit_left_right.lower() #Removes all upper case letters. The above 2 lines are in order to ensure that the user needs to simply spell the word correctly, as the .strip() and .lower() make the variable non-case-sensitive
                if rabbit_left_right != "back" and rabbit_left_right != "forward": #Remind the user of the valid responses to the question if they do not answer with one of the two options, using an if loop that activates if their response is invalid
                    print()
                    print("Please choose either \"back\" or \"forward\".")
            print(new_stage)
            print()
            if rabbit_left_right == "forward": #If the user selected forward in the inquiry, run this section of code
                print("You sour along the shores of the river.")
                print("Unfortunately, you are unable to find anything of use.")
                print()
                enter = input("Press Enter to look back down the path ") #Prevents the game from progressing to the next level until the user has pressed the 'enter' key, thus answering the input prompt and continuing the game. Having an "enter" variable not used for anything else means they are able to type before pressing enter without changing anything in the game
                print()
            print("You go further back down the path.") #This code will always be ran. The forward path leads here and adds nothingt o the game but time
            print("In a bush to your side lies a shovel.")
            print()
            enter = input("Press Enter to pick up the shovel and remove the carrot ") #Prevents the game from progressing to the next level until the user has pressed the 'enter' key, thus answering the input prompt and continuing the game. Having an "enter" variable not used for anything else means they are able to type before pressing enter without changing anything in the game
            print()
            print("You return to Barbara and shovel the carrot out of the firm ground with ease.")
            print("That was surprisingly easy.")
            print()
            enter= input("Press Enter to return the carrot to Barbara ") #Prevents the game from progressing to the next level until the user has pressed the 'enter' key, thus answering the input prompt and continuing the game. Having an "enter" variable not used for anything else means they are able to type before pressing enter without changing anything in the game
            print()
            print("You return the carrot to Barbara.")
            print("Barbara replies:    \"Thank you, kind {}!\"".format(greet)) #The .format(greet) here inserts the player's chosen greeting into the {} spa in th print statement
            print("                    \"You truly are a kind and generous soul.\"")
            print("Barbara hops away into the bushes.")
            print()
            enter = input("Press Enter to continue ") #Prevents the game from progressing to the next level until the user has pressed the 'enter' key, thus answering the input prompt and continuing the game. Having an "enter" variable not used for anything else means they are able to type before pressing enter without changing anything in the game
            print()
            print("You return your attention to the river.") #This is the end of the function if they selected this option, and the player will be returned from here to the section from which they arrived in this function


#CHAPTERS
#These functions are all of the game's actual code (for the gameplay). This is all put in functions so that it can be restarted simply by running game(), rather than having to re-run the whole file and go through Setup again. It is also as at some points in the game, I need the player to be able to go back to an earlier stage in the game, and am unsure on how to do this unless I play a function containing code from an earlier region of the game

#INTRODUCTION
def game():
    print("You're lying down, face-up, in a clearing in the middle of a forest. You think you just woke up.")
    print("You think you remember your name... {}, yeah, that seems right".format(name)) #.format statement prints the user's chosen name in the space given by {}
    print("Yes, your memory is starting to come back...")
    print()
    enter = input("Press Enter to remember ") #Prevents the game from progressing to the next level until the user has pressed the 'enter' key, thus answering the input prompt and continuing the game. Having an "enter" variable not used for anything else means they are able to type before pressing enter without changing anything in the game
    print()
    print("You think you came in here with two or three of your friends.")
    print("This is Boilierre Forest, outside your small village of Aubernesse.")
    print("You came in here to find an object from local folklore, what is known as the \"Orb of Cagim\".")
    print("Some say it used to belong to the great wizard Merlin, and even that it was the source of his power.")
    print("However, it is now said to be lost in the forest. Just like you, in fact.")
    print("You should probably try and get home.")
    print()
    enter = input("Press Enter to get up ") #Prevents the game from progressing to the next level until the user has pressed the 'enter' key, thus answering the input prompt and continuing the game. Having an "enter" variable not used for anything else means they are able to type before pressing enter without changing anything in the game
    print()
    print("You get up and look around.")
    print("You're surrounded by trees.")
    print("Funny that.")
    print("On one side of the clearing, to your left, is a path with a slight upwards incline. To your right, another path, going downhill.")
    print()
    path_split() #Once the introduction has been carried out, move to the path splitting choice function - path_split().
            
#PATH SPLITTING CHOICE
def path_split():
    path_split = "undefined" #Sets the variable as a value that is not one of those accepted, meaning the while loop is able to run as, while it recognises the variable, it meets the conditions for repeating the loop
    while path_split != "left" and path_split != "right": #The while loop will repetitively ask the user to enter a valid response for direction if their reply to the input prompt is neither "left" nor "right". The user cannot progress until a valid response is submitted
        path_split = str(input("If you want to go to the left, type \"left\". To go to the right, type \"right\" ")) 
        path_split = path_split.strip() #Removes all spaces from the front and end of the user's response 
        path_split = path_split.lower() #Removes all upper case letters. The above 2 lines are in order to ensure that the user needs to simply spell the word correctly, as the .strip() and .lower() make the variable non-case-sensitive
        if path_split != "left" and path_split != "right": #Remind the user of the valid responses to the question if they do not answer with one of the two options, using an if loop that activates if their response is invalid
            print("Please choose either \"left\" or \"right\".")
    print(new_stage) #The new_stage here is to signify the end of the "Split Path" stage
    print()
    if path_split == "left": #If in the "Split Path" stage the user selected the left-hand path, carry out this section of the code. Otherwise, carry out the right-hand path
        print("You start to meander up the left-hand path, towards where you hope Aubernesse lies.")
        print("The path is long, and seems to stretch on forever. The trees still stretch on for miles.")
        print("After walking for some time, the sun is starting to go down, and the moon is up.")
        print("You hear a rustle in the bushes along the side of the path.")
        print()
        enter = input("Press Enter to look in the bushes ") #Prevents the game from progressing to the next level until the user has pressed the 'enter' key, thus answering the input prompt and continuing the game. Having an "enter" variable not used for anything else means they are able to type before pressing enter without changing anything in the game
        print()
        print("Oh no!")
        print("As soon as your finger brushes against a leaf, a werewolf emerges from behind the bush!")
        print("You are in great danger! What do you do?")
        print()
        left_path() #Once this section of the code has been carried out, move to the Left-Hand Path choice function - left_path()
    if path_split == "right": #This part of the code will be carried out if, in the "Split Path" stage they selected the "right" option
        print("You wander down the right-hand path.")
        karma_1() #Send the user to the point in the code which runs the first of the three karma tasks, karma_1()
        print("After a few hundred metres, the path flattens out, and turns a corner.")
        right_path() #Once this section of the code has been carried out, move to the Right-Hand Path choice function - right_path()

#LEFT-HAND PATH: Werewolf & Lost in the Woods
def left_path():
    werewolf = "undefined" #Sets the variable as a value that is not one of those accepted, meaning the while loop is able to run as, while it recognises the variable, it meets the conditions for repeating the loop
    while werewolf != "stick" and werewolf != "talk" and werewolf != "tickle": #The while loop will repetitively ask the user to enter a valid response for direction if their reply to the input prompt isn't any out of "stick", "talk or "tickle". The user cannot progress until a valid response is submitted
        print("If you want to snap a stick off a nearby bush and try and fight off the werewolf, type \"stick\".")
        print("If you want to attempt to reason with the werewolf, type \"talk\".") 
        werewolf = str(input("If you want to try and tickle the werewolf, type \"tickle\". ")) #Ask their user what choice they wish to make in this situation and inform them of possible/valid inputs
        werewolf = werewolf.strip() #Removes all spaces from the front and end of the user's response 
        werewolf = werewolf.lower() #Removes all upper case letters. The above 2 lines are in order to ensure that the user needs to simply spell the word correctly, as the .strip() and .lower() make the variable non-case-sensitive
        if werewolf != "stick" and werewolf != "talk" and werewolf != "tickle": #Remind the user of the valid responses to the question if they do not answer with one of the three options ("stick", "talk" or "tickle"), using an if loop that activates if their response is invalid
            print("Please choose \"stick\", \"talk\" or \"tickle\".")
    print(new_stage) #The new_stage here signifies the end of the "Werewolf Choice" stage
    print()
    global endings #Import the variable "endings" into the function, so that it is recognised as global and is thus able to be altered
    if werewolf == "stick": #If in the "Werewolf Choice" stage the user chose the "stick" option, carry out this part of the code. Otherwise, carry out one of the other two options ("talk" or "tickle")
        print("You rush to the nearest bush, and attempt to snap off a branch.")
        print("You tug and yank at the bush but nothing comes off.")
        print("This bush has branches tougher than wire!")
        print("The werewolf goes towards you. You don't see its approach until it's too late.")
        global werewolfdeath1 #Import the variable "werewolfdeath1" into the function, so that it is recognised as global and is thus able to be altered
        if werewolfdeath1 == 0:
            werewolfdeath1 += 1
            endings += 1 #If it is the user's first time achieving this ending in the game, add one to the variable which tracks this, and increase the variable tracking the number of endings achieved
        game_over() #Move to the Game Over screen as the player has lost - this is stored in the game_over() function
    if werewolf == "talk": #If in the "Werewolf Choice" stage the user chose the "talk" option, carry out this part of the code. Otherwise, carry out one of the other two options ("stick" or "tickle")
        print("You try to talk to the werewolf, reasoning with it as best you can.")
        print("The werewolf, however, doesn't respond in a language you can understand.")
        print("It sounds like French or Spanish or something.")
        print("Whatever it is, the werewolf doesn't move very Despacito.")
        global werewolfdeath2 #Import the variable "werewolfdeath2" into the function, so that it is recognised as global and is thus able to be altered
        if werewolfdeath2 == 0:
            werewolfdeath2 += 1
            endings += 1 #If it is the user's first time achieving this ending in the game, add one to the variable which tracks this, and increase the variable tracking the number of endings achieved
        game_over() #Move to the Game Over screen as the player has lost - this is stored in the game_over() function
    if werewolf == "tickle": #If in the "Werewolf Choice" stage the user chose the "tickle" option, carry out this part of the code. Otherwise, carry out one of the other two options ("stick" or "talk")
        print("Why... why would you... what? Why did you think that was a good idea?")
        print("Anyway, it worked.")
        print("You dive at the werewolf and start to tickle it.")
        print("The wolf starts howling, and runs off, back into the forest.")
        print()
        global werewolf_playthrough #Import the variable werewolf_playthrough into the function so it is seen as global, and thus able to be altered
        global achievements_list #Import the variable achievements_list into the function so it is seen as global, and thus able to be appended
        if werewolf_playthrough == 0:
            werewolf_playthrough += 1 
            achievements_list.append("WEREWOLF HUNTER:    Defeat a Werewolf") #If this is the first time in this playing session in which the user has defeated the werewolf, add one to the werewolf_playthrough variable and give them the relevant achievement
        enter = input("Press Enter to continue ") #Prevents the game from progressing to the next level until the user has pressed the 'enter' key, thus answering the input prompt and continuing the game. Having an "enter" variable not used for anything else means they are able to type before pressing enter without changing anything in the game
        print(new_stage) #This new_stage is to signify the end of the "Tickle Consequences" stage
        print()
        print("You continue to walk down the path.")
        print("After around half an hour or so, you run out of path in front of you.")
        print("Ahead of you, there is only foliage, so thick that you cannot possibly go through it.")
        print("You have no choice but to turn around and to try the other path")
        print()
        enter = input("Press Enter to turn around ") #Prevents the game from progressing to the next level until the user has pressed the 'enter' key, thus answering the input prompt and continuing the game. Having an "enter" variable not used for anything else means they are able to type before pressing enter without changing anything in the game
        print()
        print("You wander back down the path, towards the direction you came.")
        print("Soon, however, you start to feel lost.")
        print("You're not sure if you've been here before.")
        print()
        path_lost = "undefined" #Sets the variable as a value that is not one of those accepted, meaning the while loop is able to run as, while it recognises the variable, it meets the conditions for repeating the loop
        while path_lost != "forward" and path_lost != "back": #The while loop will repetitively ask the user to enter a valid response for direction if their reply to the input prompt isn't either "forward" or "back". The user cannot progress until a valid response is submitted
            path_lost = str(input("What do you do? If you want to turn around, type \"back\". If you want to carry on, type \"forward\". ")) #Ask the user what choice they wish to make in this situation and inform them of possible/valid inputs. Store their answer in a variable to check the answer's validity
            path_lost = path_lost.strip() #Removes all spaces from the front and end of the user's response 
            path_lost = path_lost.lower() #Removes all upper case letters. The above 2 lines are in order to ensure that the user needs to simply spell the word correctly, as the .strip() and .lower() make the variable non-case-sensitive
            if path_lost != "forward" and path_lost != "back": #Remind the user of the valid responses to the question if they do not answer with one of the options ("forward" or "back"), using an if loop that activates if their response is invalid
                 print("Please choose \"forward\" or \"back\".")
        print(new_stage) #The new_stage here is to signify the end of the "Lost Path" stage
        print()
        if path_lost == "back": #If in the "Lost Path" stage the user chose the "back" option, carry out this part of the code. Otherwise, carry out the other option ("forward")
            print("You're now hopelessly lost.")
            print("You're dehydrated, starving and exhausted.")
            print("You're not sure you can carry on for much longer.")
            print("You can feel your strength seeping away.")
            print("You've just got to sit down...")
            global lostdeath #Import the variable "lostdeath" into the function, so that it is recognised as global and is thus able to be altered
            if lostdeath == 0:
                lostdeath += 1
                endings += 1 #If it is the user's first time achieving this ending in the game, add one to the variable which tracks this, and increase the variable tracking the number of endings achieved
            game_over() #Move to the Game Over screen as the player has lost - this is stored in the game_over() function
        if path_lost == "forward": #If in the "Path Lost" stage the user chose the "forward" option, carry out this part of the code. Otherwise, carry out the other option ("back")
            print("Good choice!")
            print("You soon find your way back to the clearing where you woke up.")
            print("It's probably best to try the other path.")
            print()
            global lost_playthrough #Import the variable lost_playthrough into the function so it is seen as global, and thus able to be altered
            if lost_playthrough == 0:
                lost_playthrough += 1
                achievements_list.append("NAVIGATOR:          Recover from being lost") #If this is the first time in this playing session in which the user has passed this stage in the code, add one to the lost_playthrough variable and give the pplayer the relevant achievement
            enter = input("Press Enter to continue down the path.") #Prevents the game from progressing to the next level until the user has pressed the 'enter' key, thus answering the input prompt and continuing the game. Having an "enter" variable not used for anything else means they are able to type before pressing enter without changing anything in the game
            print(new_stage) #The new_stage here is to signify the end of the "Forward Consequences" stage
            print()
            path1_complete = True #Set the value of path1_complete to "True", as it was previously set to "False". This is to ensure that, even if the player did not choose the right path initially, they can still go through that part of the code, as another condition, regarding the first part of the path's completion, has been added
            print("You wander down the right-hand path.")
            karma_1() #Send the user to the point in the code which runs the first of the three karma tasks, karma_1()
            print("After a few hundred metres, the path flattens out, and turns a corner.")
            print("You cross a bridge over a small stream, and look up.")
            right_path() #Once this section of the code has been carried out, move to the Right-Hand Path choice function - right_path()

#RIGHT-HAND PATH: Riddle
def right_path():
    print("Around 15 metres ahead of you, an ancient, mossy stone wall sits in your path, around 8 feet high.")
    global riddle_occurrence #Imports the riddle_occurrence variable into this function so it is able to be altered from its current value if this is not the player's first time visiting this function in a game
    riddle_occurrence += 1 #Add one to the number of times the player has accessed the function in the current game
    if riddle_occurrence == 1: #Display this text if the player is accessing this function for the first time
        print("The foliage on both sides of the path is too thick to get through.")
        print("The only way to get past: a large oak door at the end of the path.")
        print("You can see a bronze plaque mounted on the gateway.")
    else: #Display this text if the player is returning to this section
        print("You're back at the door with the riddle.")
        print("However, can you remember the answer?")
    print()
    enter = input("Press Enter to get closer and read the sign ") #Prevents the game from progressing to the next level until the user has pressed the 'enter' key, thus answering the input prompt and continuing the game. Having an "enter" variable not used for anything else means they are able to type before pressing enter without changing anything in the game
    print()
    print("The plaque reads:")
    print(new_stage) #The new_stage here is to signify the start of the plaque's text
    print()
    print("     I have cities, but no houses.")
    print("     I have mountains, but no trees.")
    print("     I have water, but no fish.")
    print("     In one word, what am I?")
    print()
    print("     Answer in three attempts or remain forever stranded.")
    print(new_stage) #The new_stage here is to signify the end of the plaque's text
    print()
    riddle_guess = "undefined" #Sets the variable as a value that is not one of those accepted, meaning the while loop is able to run as, while it recognises the variable, it meets the conditions for repeating the loop
    guesses_remain = 3 #Give the user 3 attempts at answering the riddle correctly
    while riddle_guess != "map" and riddle_guess != "a map": #The while loop will repetitively ask the user to enter their guess for the riddle's answer. Until they input the correct answer or run out of guess attempts, they will be asked to guess again 
        riddle_guess = input("What do you think the answer could be? ") #Ask their user what their guess for the riddle's answer is
        riddle_guess = riddle_guess.strip() #Removes all spaces from the front and end of the user's response 
        riddle_guess = riddle_guess.lower() #Removes all upper case letters. The above 2 lines are in order to ensure that the user needs to simply spell the word correctly, as the .strip() and .lower() make the variable non-case-sensitive
        if riddle_guess != "map" and riddle_guess != "a map": #Print an additional message if the user's response to the riddle is incorrect
            print()
            guesses_remain -= 1 #As the user has guessed the answer incorrectly, they have one less attempt to answer the riddle
            if guesses_remain == 2: #If the user has two attempts remaining, inform them of this and give them a clue to aid them in their attempts
                print("Unfortunately, that seems to be incorrect.")
                print("However, you have ", guesses_remain, " more guesses.") #Insert the number of guesses the user has remaining into the gap in the print statement
                print("Also, you have another clue:")
                print(new_stage) #The new_stage here is to signify the start of the new clue
                print()
                print("     The answer you seek is a noun which starts with \"m\".")
                print(new_stage) #The new_stage here is to signify the end of the new clue
                print()
            if guesses_remain == 1: #If the user has one attempt remaining, inform them of this and give them a final clue to aid them in their attempts
                print("Unfortunately, that seems to be incorrect.")
                print("However, you have ", guesses_remain, " more guess.") #Insert the number of guesses the user has remaining into the gap in the print statement
                print("Also, you have one final clue:")
                print(new_stage) #The new_stage here is to signify the start of the new clue
                print()
                print("     The word you seek is but three letters long, an item made by cartographers.")
                print(new_stage) #The new_stage here is to signify the end of the new clue
                print()
            if guesses_remain == 0: #If the user has no remaining attempts, inform them that they have lost, and send them to the Game Over screen
                print("Unfortunately, that seems to be incorrect.")
                print("You are out of guesses.")
                print("The door remains closed.")
                print("As you stand in silence, the only sound is a rustling in the bushes.")
                print("You are stranded in the forest, forever.")
                global riddledeath #Import the variable "riddledeath" into the function so it seen as global and is thus able to be altered
                global endings #Import the variable "endings" into the function so it is seen as global and is thus able to be altered
                if riddledeath == 0:
                    riddledeath += 1
                    endings += 1 #If it is the user's first time achieving this ending in the game, add one to the variable which tracks this, and increase the variable tracking the number of endings achieved
                game_over() #Move to the Game Over screen as the player has lost - this is stored in the game_over() function
    print(new_stage) #This new_stage is to signify the end of the "Riddle Answering" stage
    print()
    if riddle_occurrence == 1: #Display this text if this is the first time the player has been to this function
        print("That seems to be correct!")
    else: #Display this text if this is not the player's first time in this function
        print("Congratulations! You've remembered correctly.")
    print("The very second you said \"{}\", you could hear the whirring and clunking of ancient gears returning to action.".format(riddle_guess))
    print("After a few seconds of loud clattering, the door flies open, showering you with dust and cobwebs.")
    print()
    enter = input("Press Enter to go through the door ")#Prevents the game from progressing to the next level until the user has pressed the 'enter' key, thus answering the input prompt and continuing the game. Having an "enter" variable not used for anything else means they are able to type before pressing enter without changing anything in the game
    print()
    global riddles_playthrough #Import the variable riddles_playthrough into the function so it is seen as global, and thus able to be altered
    riddles_playthrough += 1 #Add one to the number of times in the current playing section the player has made it through this section of the code
    if riddles_playthrough == 1:
        global achievements_list #Import the variable achievements_list into the function so it is seen as global, and thus able to be appended
        achievements_list.append("WORDSMITH:          Solve a Riddle") #If this is the first time in the current playing session the player has completed this section, give them the relevant achievement
    if riddle_occurrence == 1:
        monster() #Once this section of the code has been carried out, move to the Monster Fight choice function - monster()
    else:
        monster_gone() #If the player is returning to this function and has therefore already defeated the monster, go to the monster_gone() function instead of fighting the monster again

#MONSTER FIGHT
def monster():
    print("You walk through the door, emerging on the other side of the wall.")
    print("Compared to the other side, it is much, much darker here.")
    print("You can barely see - just the odd bit of glare off the puddles along the path to guide your way.")
    if torch_owned == True: #An if statement which will activate if, in the karma_1() function, the player received a torch from Roger the Bear
        print()
        enter = input("Press Enter to turn on Roger the Bear's torch ") #Prevents the game from progressing to the next level until the user has pressed the 'enter' key, thus answering the input prompt and continuing the game. Having an "enter" variable not used for anything else means they are able to type before pressing enter without changing anything in the game
        print()
        print("You turn on the torch which your good pal Roger conveniently gave you earlier.")
        print("It sends out a powerful beam, illuminating the path ahead of you.")
        print("However, there is not much to see ahead of you but a long path, lined with dense foliage on both sides.")
    print("In the distance, you can hear running water, but that's just barely, as the sound of your feet in the mud drowns it out.")
    print()
    enter = input("Press enter to continue down the path ") #Prevents the game from progressing to the next level until the user has pressed the 'enter' key, thus answering the input prompt and continuing the game. Having an "enter" variable not used for anything else means they are able to type before pressing enter without changing anything in the game
    print()
    karma_2() #Go to the function containing the second of three karma tasks - karma_2()
    print("After around 10 minutes or so, you hear a *thwack* behind you.")
    if torch_owned == True: #An if statement which will activate if, in the karma_1() function, the player received a torch from Roger the Bear
        print("You spin around, your flashlight finding nothing but lonesome trees.")
    else: #This section will occur if the player did not receive a flashlight from Roger the bear in the karma_1() function.
        print("You spin around, seeing only the darkness.")
    print("There is another *thwack* behind you.")
    print("You look down to your feet, and the mud around you seems to be bubbling.")
    print("You take a step back, and the mud in front of you seems to rise.")
    print("Before long, there is a large, humanoid shape in front of you, dripping mud.")
    print("It seems to be some sort of monster made out of mud.")
    print(new_stage)
    print()
    print("The figure lurches towards you jerkily.")
    print("What do you do?")
    print()
    lives = 2 #Give the user two lives, so they can afford to make one wrong decision durng the fight
    monster_choice_1 = "undefined" #Sets the variable as a value that is not one of those accepted, meaning the while loop is able to run as, while it recognises the variable, it meets the conditions for repeating the loop
    while monster_choice_1 != "under" and monster_choice_1 != "around" and monster_choice_1 != "over": #The while loop will repetitively ask the user to enter a valid response for direction if their reply to the input prompt is not "under", "around, or "over". The user cannot progress until a valid response is submitted
        print("If you want to try and climb one of the trees lining the side of the path, enter \"over\".")
        print("If you want to try and feint your way around the slime monster, enter \"around\".")
        monster_choice_1 = input("If you want to try and dive through the slime monster's legs to get past, enter \"under\" ") #Ask the user what choice they wish to make in this situation and inform them of possible/valid inputs. Store their answer in a variable to check the answer's validity
        monster_choice_1 = monster_choice_1.strip() #Removes all spaces from the front and end of the user's response 
        monster_choice_1 = monster_choice_1.lower() #Removes all upper case letters. The above 2 lines are in order to ensure that the user needs to simply spell the word correctly, as the .strip() and .lower() make the variable non-case-sensitive
        if monster_choice_1 != "under" and monster_choice_1 != "around" and monster_choice_1 != "over": #Remind the user of the valid responses to the question if they do not answer with one of the three options, using an if loop that activates if their response is invalid
            print()
            print("Please select either \"over\", \"around\" or \"under\".")
            print()
    if monster_choice_1 == "under": #This if loop will activate if, in thje while loop, the user chose under
        print()
        print("You try to dive between the legs of the slime monster to get past.")
        print("As you do so, the slime monster collapses.")
        print("The shape of the creature disappears, drowning you in mud.")
        print("On your way down, you only just manage to get a hold of a tree root.")
        print("You pull yourself out, to see the slime monster still standing there, a few metres down the path.")
        print("You don't think you can afford to make a mistake like that again.")
        print()
        enter = input("Press enter to continue ") #Prevents the game from progressing to the next level until the user has pressed the 'enter' key, thus answering the input prompt and continuing the game. Having an "enter" variable not used for anything else means they are able to type before pressing enter without changing anything in the game
        lives -= 1 #As this is an incorrect decision, take away one of the user's two lives
    elif monster_choice_1 == "over": #This if loop activates if the player chose over in the while loop
        print()
        print("You try to climb one of the trees to get over the slime monster.")
        print("The branch, however, after climbing a few metres, snaps.")
        print("You collapse onto the top of the slime monster, and feel it swing its arm at you.")
        print("You go flying away, into the ground with a thud.")
        print("You don't think you can afford to make a mistake like that again.")
        print()
        enter = input("Press enter to continue ") #Prevents the game from progressing to the next level until the user has pressed the 'enter' key, thus answering the input prompt and continuing the game. Having an "enter" variable not used for anything else means they are able to type before pressing enter without changing anything in the game
        lives -= 1 #As this is an incorrect decision, take away one from the user's lives
    elif monster_choice_1 == "around": #This if loop activates if, in the while loop, the user chose around. The user's number of lives are not affected in this function as it is the correct choice
        print()
        print("You sprint around the slime monster.")
        print("It tries to leap on top of you, but you make it through in time, as it collapses inches behind you.")
        print("You've successfully made it around the slime monster.")
        print("However, it sinks back into the ground and reforms a few metres further down the path.")
        print()
        enter = input("Press Enter to continue ") #Prevents the game from progressing to the next level until the user has pressed the 'enter' key, thus answering the input prompt and continuing the game. Having an "enter" variable not used for anything else means they are able to type before pressing enter without changing anything in the game
    print(new_stage)
    print()
    print("It would seem that trying to get around the creature is pointless, if it is able to move like that.")
    print("You'll have to switch up your approach.")
    print()
    monster_choice_2 = "undefined" #Sets the variable as a value that is not one of those accepted, meaning the while loop is able to run as, while it recognises the variable, it meets the conditions for repeating the loop
    while monster_choice_2 != "stick" and monster_choice_2 != "rock" and monster_choice_2 != "attack": #The while loop will repetitively ask the user to enter a valid response for direction if their reply to the input prompt is not "stick", "rock, or "attack". The user cannot progress until a valid response is submitted
        print("If you want pick up a rock off the path and throw it at the creature, enter \"rock\".")
        print("If you want to snap a stick off a nearby tree and hit the mud creature with it, enter \"stick\".")
        monster_choice_2 = input("If you want to go full fisticuffs on the monster, enter \"attack\" ") #Ask the user what choice they wish to make in this situation and inform them of possible/valid inputs. Store their answer in a variable to check the answer's validity
        monster_choice_2 = monster_choice_2.strip() #Removes all spaces from the front and end of the user's response 
        monster_choice_2 = monster_choice_2.lower() #Removes all upper case letters. The above 2 lines are in order to ensure that the user needs to simply spell the word correctly, as the .strip() and .lower() make the variable non-case-sensitive
        if monster_choice_2 != "stick" and monster_choice_2 != "rock" and monster_choice_2 != "attack": #Remind the user of the valid responses to the question if they do not answer with one of the three options, using an if loop that activates if their response is invalid
            print()
            print("Please enter \"rock\", \"stick\" or \"attack\".")
            print()
    global endings #Import the variable "endings" into the function so it is seen as a global and is thus able to be altered
    if monster_choice_2 == "stick": #If in the while loop the player chose stick, perform this section of the code. The number of remaining lives is not affected as it is the correct option
        print()
        print("You snap a stick off the tree, and start swinging it at the monster.")
        print("With each swing, large chunks of mud and slime fly off the organism and splatter over the trees lining the path.")
        print("After 10 or 20 swings, the creature is no longer there.")
        print("However, you can see it reforming slowly further down the path.")
        print()
        enter = input("Press Enter to continue ") #Prevents the game from progressing to the next level until the user has pressed the 'enter' key, thus answering the input prompt and continuing the game. Having an "enter" variable not used for anything else means they are able to type before pressing enter without changing anything in the game
    elif monster_choice_2 == "rock": #If in the while loop the player chose rock, this if loop is performed
        lives -= 1 #As this is an incorrect option, subtract on from the player's total number of lives
        print()
        print("You pick up the rock, and proceed to yeet it at the monster.")
        print("It goes straight through the creature's stomach, leaving a moderately sized hole.")
        print("However, it doesn't stop the creature.")
        print("It swings its arm at you.")
        if lives == 0: #Run this section of code if the player has run out of remaining lives
            print("You don't get back up.")
            global monsterdeath2_1 #Import the variable "monsterdeath2_1" into the function so it is seen as a global and is thus able to be altered
            if monsterdeath2_1 == 0:
                monsterdeath2_1 += 1
                endings += 1 #If it is the user's first time achieving this ending in the game, add one to the variable which tracks this, and increase the variable tracking the number of endings achieved
            game_over() #If the player has no lives remaining at this point, they have lost the game, so therefore take them to the game lost screen
        else: #If the player has one remaining life, perform this section of the code and allow them to participate in question three
            print("You don't think you can afford to maka a mistake like that again.")
            print()
            enter = input("Press Enter to continue ") #Prevents the game from progressing to the next level until the user has pressed the 'enter' key, thus answering the input prompt and continuing the game. Having an "enter" variable not used for anything else means they are able to type before pressing enter without changing anything in the game
    elif monster_choice_2 == "attack": #If in the while loop the user chose attack, perform this section of teh code
        lives -= 1 #As this is an incorrect answer, take away of the player's lives
        print()
        print("You charge at the creature, and proceed to throw punches at it.")
        print("It is made of mud.")
        print("This does nothing.")
        print("It swings its arm at you.")
        if lives == 0: #Run this section of code if the player has run out of remaining lives
            print("You don't get back up.")
            global monsterdeath2_2#Import the variable "monsterdeath2_2" into the function so it is seen as a global and is thus able to be altered
            if monsterdeath2_2 == 0:
                monsterdeath2_2 += 1
                endings += 1 #If it is the user's first time achieving this ending in the game, add one to the variable which tracks this, and increase the variable tracking the number of endings achieved
            game_over() #If the player has no lives remaining at this point, they have lost the game, so therefore take them to the game lost screen
        else: #If the player has one remaining life, perform this section of the code and allow them to participate in question three
            print("You don't think you can afford to maka a mistake like that again.")
            print()
            enter = input("Press Enter to continue ") #Prevents the game from progressing to the next level until the user has pressed the 'enter' key, thus answering the input prompt and continuing the game. Having an "enter" variable not used for anything else means they are able to type before pressing enter without changing anything in the game
    print(new_stage)
    print()
    print("You think the monster now seems weak.")
    print("You are probably capable of defeating it soon.")
    print("From a tree to your left hangs a bell.")
    print("From the tree to your right, a rope swing with a tyre on the end.")
    print()
    monster_choice_3 = "undefined" #Sets the variable as a value that is not one of those accepted, meaning the while loop is able to run as, while it recognises the variable, it meets the conditions for repeating the loop
    while monster_choice_3 != "bell" and monster_choice_3 != "swing" and monster_choice_3 != "rope": #The while loop will repetitively ask the user to enter a valid response for direction if their reply to the input prompt is not "bell", "swing, or "rope". The user cannot progress until a valid response is submitted
        print("To attempt to pull down the tree by pulling on the rope, enter \"rope\".")
        print("To ring the bell, enter \"bell\".")
        monster_choice_3 = input("To swing the tyre at the creature, enter \"swing\" ") #Ask the user what choice they wish to make in this situation and inform them of possible/valid inputs. Store their answer in a variable to check the answer's validity
        monster_choice_3 = monster_choice_3.strip() #Removes all spaces from the front and end of the user's response 
        monster_choice_3 = monster_choice_3.lower() #Removes all upper case letters. The above 2 lines are in order to ensure that the user needs to simply spell the word correctly, as the .strip() and .lower() make the variable non-case-sensitive
        if monster_choice_3 != "bell" and monster_choice_3 != "swing" and monster_choice_3 != "rope": #Remind the user of the valid responses to the question if they do not answer with one of the three options, using an if loop that activates if their response is invalid
            print()
            print("Please choose either \"rope\", \"bell\" or \"swing\".")
            print()
    if monster_choice_3 == "bell": #If in the while loop the user chose the bell option, carry out this section of the code. The user's lives are not affected here as it is teh correct answer
        print()
        print("You ring the bell.")
        print("The creature falls to its knees and screeches, before melting into a puddle.")
        print("You're surprised that worked.")
        print()
        enter = input("Press Enter to continue ") #Prevents the game from progressing to the next level until the user has pressed the 'enter' key, thus answering the input prompt and continuing the game. Having an "enter" variable not used for anything else means they are able to type before pressing enter without changing anything in the game
    elif monster_choice_3 == "swing": #If the user chose swing in the while loop, carry out this section of the code
        lives -= 1 #As this is an incorrect answer, subtract one of the user's lives
        if lives == 0: #Run this section of code if the player has run out of remaining lives
            print()
            print("You swing the tyre at the creature.")
            print("You miss.")
            print()
            print("Damn.")
            print("The monster swings its arm at you.")
            print("You can't escape.")
            global monsterdeath3_1 #Import the variable "monsterdeath3_1" into the function so it is seen as a global and is thus able to be altered
            if monsterdeath3_1 == 0:
                monsterdeath3_1 += 1
                endings += 1 #If it is the user's first time achieving this ending in the game, add one to the variable which tracks this, and increase the variable tracking the number of endings achieved
            game_over() #If the player has no lives remaining at this point, they have lost the game, so therefore take them to the game lost screen
        else: #If the player has one remaining life, perform this section of the code and allow them to continue the game. As this is the last question, they must have a victorious outcome in this part even though their choice was wrong
            print()
            print("The swing clatters into the monster, as it collapses into the ground.")
            print("It oozes into a puddle of mud on the ground.")
            print()
            enter = input("Press Enter to continue ") #Prevents the game from progressing to the next level until the user has pressed the 'enter' key, thus answering the input prompt and continuing the game. Having an "enter" variable not used for anything else means they are able to type before pressing enter without changing anything in the game
    elif monster_choice_3 == "rope": #If in the while loop the user chose rope, perform this section of the code
        lives -= 1 #As this choice was not a correct one, take away one of the user's lives
        print()
        print("You try and pull the tree over using the rope.")
        print("Unfortunately, you are far, far too weak for this.")
        print("The tree has very strong roots and you make exactly no process.")
        if lives == 0: #Run this if loop if the player has no lives remaining
            print("The creature swings its arm at you.")
            print("You can't escape.")
            global monsterdeath3_2 #Import the variable "monsterdeath3_2" into the function so it is seen as a global and is thus able to be altered
            if monsterdeath3_2 == 0:
                monsterdeath3_2 += 1
                endings += 1 #If it is the user's first time achieving this ending in the game, add one to the variable which tracks this, and increase the variable tracking the number of endings achieved
            game_over() #If the player has no lives remaining at this point, they have lost the game, so therefore take them to the game lost screen
        else: #If the player has one remaining life, perform this section of the code and allow them to continue the game. As this is the last question, they must have a victorious outcome in this part even though their choice was wrong
            print("You resort to just swinging the tyre instead.")
            print("The swing clatters into the monster, as it collapses into the ground.")
            print("It oozes into a puddle of mud on the ground.")
            print()
            enter = input("Press Enter to continue ") #Prevents the game from progressing to the next level until the user has pressed the 'enter' key, thus answering the input prompt and continuing the game. Having an "enter" variable not used for anything else means they are able to type before pressing enter without changing anything in the game
    global monster_playthrough #Import the variable monster_playthrough into the function so it is seen as global, and thus able to be altered
    global achievements_list #Import the variable achievements_list into the function so it is seen as global, and thus able to be appended
    if monster_playthrough == 0:
        monster_playthrough += 1
        achievements_list.append("UNDEFEATABLE:       Defeat a Monster") #If this is the player's furst time defeating the monster in the current playing session, add one to the variable which counts how many times this has occurred, and give the player the relevant achievement
    if lives == 2: #Run this section of code if the player went through the monster fight without losing any lives
        global invincible_playthrough #Import the variable invincible_playthrough into the function so it is seen as global, and thus able to be altered
        if invincible_playthrough == 0:
            invincible_playthrough += 1
            achievements_list.append("INVINCIBLE:         Defeat a Monster flawlessly") #If this is the user's first time going through the monster life without losing a life in the current playing session, add one to the variable counting the number of occurrences this has happened, and award the player the relevant achievement
    print(new_stage)
    print()
    river() #Once this section of the code has been carried out, go to the river chapter's function - river()

#NO MORE MONSTER
def monster_gone():
    print("You walk through the door, emerging on the other side of the wall.")
    print("Compared to the other side, it is much, much darker here.")
    print("You can barely see - just the odd bit of glare off the puddles along the path to guide your way.")
    print("In the distance, you can hear running water, but that's just barely, as the sound of your feet in the mud drowns it out.")
    print("15 or so minutes later, you cross a pool of mud and slime all over the path.")
    print("You recognise this area as where you came across the slime creature.")
    print("You stop for a minute to reflect.")
    print()
    enter = input("Press Enter to continue ") #Prevents the game from progressing to the next level until the user has pressed the 'enter' key, thus answering the input prompt and continuing the game. Having an "enter" variable not used for anything else means they are able to type before pressing enter without changing anything in the game
    print(new_stage)
    print()
    print("You continue to stroll down the path.")
    river() #Once this section of the code has been carried out, go to the river chapter

#RIVER
def river():
    global riddle_occurrence #Import the variable riddle_playthrough into the function so it is seen as global, and thus able to be accepted by the function as having a different value in different iterations of the function
    if riddle_occurrence == 1: #If the player has not yet been through this section of the code, display this text
        print("Before long, you come across an opening with a river.")
        print("The water rushes along with pace, and seems very deep.")
        karma_3() #Run the final of the three available karma tasks - karma_3()
        print("You don't think you can swim across - it's around 10 metres wide and fast-flowing.")
    else: #If this is not th player's frst time in this function, display this text
        print("You have found your way back to the river")
    print("To your left, about three metres further down the river, a path of rocks, spaced about two metres apart each.")
    print("To your right, a low branch stretches about 80% of the way across the river.")
    print("What do you do?")
    print(new_stage)
    print()
    river = "undefined" #Sets the variable as a value that is not one of those accepted, meaning the while loop is able to run as, while it recognises the variable, it meets the conditions for repeating the loop
    while river != "river" and river != "branch" and river != "stones" and river != "back": #The while loop will repetitively ask the user to enter a valid response for direction if their reply to the input prompt is not "stones", "branch, "back", or "river". The user cannot progress until a valid response is submitted
        print("To look in the river, enter \"river\".")
        print("To try and climb across the branch, enter \"branch\".")
        print("To clamber across the stones, enter \"stones\".")
        river = input("To go back, enter \"back\" ") #Ask the user what choice they wish to make in this situation and inform them of possible/valid inputs. Store their answer in a variable to check the answer's validity
        river = river.strip() #Removes all spaces from the front and end of the user's response 
        river = river.lower() #Removes all upper case letters. The above 2 lines are in order to ensure that the user needs to simply spell the word correctly, as the .strip() and .lower() make the variable non-case-sensitive
        print()
        if river != "river" and river != "branch" and river != "stones" and river != "back": #Remind the user of the valid responses to the question if they do not answer with one of the four options, using an if loop that activates if their response is invalid
            print("Please enter one out of \"river\", \"branch\", \"stones\" or \"back\".")
            print()
    if river == "branch": #If in the while loop the user chose branch, perform this section of the code
        print("You clamber up onto the branch.")
        print("You slowly shuffle across to the end.")
        print("The bank is still around two metres away.")
        print()
        enter = input("Press Enter to jump ") #Prevents the game from progressing to the next level until the user has pressed the 'enter' key, thus answering the input prompt and continuing the game. Having an "enter" variable not used for anything else means they are able to type before pressing enter without changing anything in the game
        print()
        print("You try to leap off the branch, but slip on the mossy bark.")
        print("You fall into the stream, and get swept away.")
        print("The freezing water makes you lose your consciousness temporarily.")
        print(new_stage)
        print()
        time.sleep(3) #Temporarily pause the code for three seconds as the player is unconscious
        print("You awaken when the river sends you tumbling into a bridge.")
        print("The river is shallower and slower here - more of a stream - so you clamber out.")
        right_path() #Return the player to an earlier point in the code
    if river == "stones": #If the player chose stones in the while loop inquiry, perform this section of the code
        print("You leap onto the stones.")
        print("You successfully hop over to the third or fourth stone.")
        print("However, you roll your ankle on the mossy stone and fall to the side.")
        print("You fall into the stream, and get swept away.")
        print("The freezing water makes you lose your consciousness temporarily.")
        print(new_stage)
        print()
        time.sleep(3) #Temporarily pause the code for three seconds as the player is unconscious
        print("You awaken when the river sends you tumbling into a bridge.")
        print("The river is shallower and slower here - more of a stream - so you clamber out.")
        right_path() #Return the player to an earlier point in the code
    if river == "river": #If, in the question, the user chose river, perform this section of the game
        print("You walk to the edge of the river and peer into the rushing water.")
        print("A few seconds later, a smooth brown dome rises out of the water downstream.")
        print("As it moves towards you, you can see that it is a turtle.")
        print("It stops a few feet in front of you and raises its head into the air so you can see it.")
        print()
        enter = input("Press Enter to ask the turtle for help ") #Prevents the game from progressing to the next level until the user has pressed the 'enter' key, thus answering the input prompt and continuing the game. Having an "enter" variable not used for anything else means they are able to type before pressing enter without changing anything in the game
        print(new_stage)
        print()
        print("The turtle replies: \"Sure thing! I'm Walter by the way.\"")
        print()
        enter = input("Press Enter to introduce yourself to Walter and ask for help across the river ") #Prevents the game from progressing to the next level until the user has pressed the 'enter' key, thus answering the input prompt and continuing the game. Having an "enter" variable not used for anything else means they are able to type before pressing enter without changing anything in the game
        print()
        print("Walter replies:     \"Hi {}! I'd be right happy to help you across. In fact, I know where there's a bridge.\"".format(name)) #The .format(name) here insert's the player's username into the {} space in the print statement
        print()
        enter = input("Press Enter to ask Walter where the bridge is ") #Prevents the game from progressing to the next level until the user has pressed the 'enter' key, thus answering the input prompt and continuing the game. Having an "enter" variable not used for anything else means they are able to type before pressing enter without changing anything in the game
        print()
        print("Walter replies:     \"Look in the underbrush to your left. You should be able to find a lever. Pull it.\"")
        print()
        enter = input("Press Enter to thank Walter ") #Prevents the game from progressing to the next level until the user has pressed the 'enter' key, thus answering the input prompt and continuing the game. Having an "enter" variable not used for anything else means they are able to type before pressing enter without changing anything in the game
        print()
        print("Walter replies:     \"Any time my {}.\"".format(dude)) #The .format(dude) here insert's the player's "dude" value in the {} space in the print statement
        print("Walter floats downstream gracefully.")
        print()
        enter = input("Press Enter to look in the bushes and pull the lever ") #Prevents the game from progressing to the next level until the user has pressed the 'enter' key, thus answering the input prompt and continuing the game. Having an "enter" variable not used for anything else means they are able to type before pressing enter without changing anything in the game
        print(new_stage)
        print()
        print("You look between the shubberies along the forest floor and soon come across a lever, just as Walter had said you would.")
        print("You pull the lever, and an ancient looking stone bridge slowly rises ominously from the depths.")
        global bridge_playthrough #Import the variable bridge_playthrough into the function so it is seen as global, and thus able to be altered
        if bridge_playthrough == 0:
            bridge_playthrough += 1
            global achievements_list #Import the variable achievements_list into the function so it is seen as global, and thus able to be appended
            achievements_list.append("ENGINEER:           Create a Bridge across the River") #If this is the user's first time passing through this section of the code, add one to the variable which tracks the number of times the player has done this, and give them the relevant achievement
        print("The top of the bridge looks slippery and is covered in moss.")
        bridge = "undefined" #Sets the variable as a value that is not one of those accepted, meaning the while loop is able to run as, while it recognises the variable, it meets the conditions for repeating the loop
        while bridge != "cross" and bridge != "swim": #The while loop will repetitively ask the user to enter a valid response for direction if their reply to the input prompt isn't either "cross" or "swim". The user cannot progress until a valid response is submitted
            print()
            bridge = input("Enter \"cross\" to walk across the bridge. Enter \"swim\" to swim across, just in case ") #Ask the user what choice they wish to make in this situation and inform them of possible/valid inputs. Store their answer in a variable to check the answer's validity
            bridge = bridge.strip() #The .strip() here removes all spaces from the start and end of the user's response to the input enquiry
            bridge = bridge.lower() #Removes all upper case letters. The above 2 lines are in order to ensure that the user needs to simply spell the word correctly, as the .strip() and .lower() make the variable non-case-sensitive
            print()
            if bridge != "cross" and bridge != "swim": #Remind the user of the valid responses to the question if they do not answer with one of the two options, using an if loop that activates if their response is invalid
                print("Please enter either \"swim\" or \"cross\".")
        if bridge == "swim": #If, in the enquiry, the user selected swim, carry out this section of the code
            print("You decide to attempt to swim across the river, thinking the bridge looks a bit slippery.")
            print("You manage to make it about halfway across, but your arms start to tire as you fight against the fast current.")
            print("You are too exhausted to continue, and are swept away by the stream.")
            print("The freezing water makes you lose your consciousness temporarily.")
            print(new_stage)
            print()
            time.sleep(3) #Temporarily pause the code for three seconds as the player is unconscious
            print("You awaken when the river sends you tumbling into a bridge.")
            print("The river is shallower and slower here - more of a stream - so you clamber out.")
            right_path() #Return the player to an earlier point in the code
        if bridge == "cross": #If in the while loop the user selected cross, carry out this section of the code
            print("You walk across the bridge easily, with no issue.")
            print("Once on the other side, the path continues and turns left around a bend.")
            print()
            enter = input("Press Enter to walk down the path ") #Prevents the game from progressing to the next level until the user has pressed the 'enter' key, thus answering the input prompt and continuing the game. Having an "enter" variable not used for anything else means they are able to type before pressing enter without changing anything in the game
            print()
            print("You walk around the corner, and there, in the distance, you see an opening in the trees.")
            print("In the distance, you can see the village of Aubernesse.")
            print("Your home.")
            print("You run across the fields seperating you from your residence, until you reach the outskirts of the town.")
            print("You are home.")
            global gamewon #Import the variable gamewon into the function so it is seen as global, and thus able to be altered
            global endings #Import the variable "endings" into the function so it is seen as a global and is thus able to be altered
            global perfect_citizen #Import the variable "perfect_citizen" into the function so it is seen as a global and is thus able to be altered
            gamewon += 1 #Add one to the variable tracking the number of times the player has won the game
            if karma == 3:
                perfect_citizen += 1 #Add one to the variable tracking how many times the player has won the game with maximum karma
            if gamewon == 1:
                achievements_list.append("CHAMPION:           Win Forest Adventure") #Add one to the variable which tracks the number of times the user has won the game. If it is their first time, give them the relevant achievement
            if perfect_citizen == 1:
                achievements_list.append("PERFECT CITIZEN:    Help Everyone while Winning the Game")
            global riverwin #Import the variable riverwin into the function so it is seen as global, and thus able to be altered
            riverwin += 1
            if riverwin == 1:
                endings += 1 #If it is the user's first time achieving this ending in the game, increase the variable tracking the number of endings achieved
            if cavewin > 0:
                if riverwin == 1:
                    achievements_list.append("BORN WINNER:        Win Forest Adventure in Two Different Manners") #If this is the player's first time winning the game through this path, add one to the variable which tracks this, and, if they have also won the game through the other path before, give the user the relevant achievement
            game_won() #Go to the game won screen 
    if river == "back": #This if loop will activate if, in the while loop, the user chose "back"
        cave() #Go to the "cave" chapter

#CAVE
def cave():
    global endings #Import the variable "endings" into the function so it is seen as a global and is thus able to be altered
    global cavedeath #Import the variable "cavedeath" into the function so it is seen as a global and is thus able to be altered
    print("You turn around, and return back down the path.")
    print("A few metres back, tucked behind a tree, you see the entrance to a cave.")
    print()
    enter = input("Press Enter to enter the cave ") #Prevents the game from progressing to the next level until the user has pressed the 'enter' key, thus answering the input prompt and continuing the game. Having an "enter" variable not used for anything else means they are able to type before pressing enter without changing anything in the game
    print(new_stage)
    print()
    print("You walk into the cave.")
    if torch_owned == False: #If the player did not acquire a torch from Roger in karma_1(), play this section of the code. Otherwise, play the alternate (non-indented) path
        print("You wander for several minutes in the darkness.")
        print("Your eyes fail to adjust to the void, and you soon tire.")
        print("As you sit down, you fade into a deep sleep.")
        print(new_stage)
        print()
        time.sleep(2) #Have a temporary 2 second pause as the player is asleep
        print("You awake into more darkness, somehow thicker than before.")
        print("You are now well and truly lost.")
        global cavedeathnotorch #Import the variable "cavedeathnotorch" into the function so it is seen as a global and is thus able to be altered
        global endings #Import the variable "endings" into the function so it is seen as a global and is thus able to be altered
        if cavedeathnotorch == 0:
            cavedeathnotorch += 1
            endings += 1 #If it is the user's first time achieving this ending in the game, add one to the variable which tracks this, and increase the variable tracking the number of endings achieved
        game_over() #As this is a losing path, this will send the player to the game_over() function, and they have lost the game
    print("It is very dark in here, so you take out your flashlight, as you otherwise would not be able to see.")
    print("Along the walls of the cavern are some ancient-looking cave paintings.")
    print("The cave stretches on for a long way, and you walk for some time.")
    print()
    enter = input("Press Enter to continue ") #Prevents the game from progressing to the next level until the user has pressed the 'enter' key, thus answering the input prompt and continuing the game. Having an "enter" variable not used for anything else means they are able to type before pressing enter without changing anything in the game
    print()
    print("Around 15 minutes later, you come across a fork in the cave.")
    print("The cave to your left and the cave to your right seem indistinguishable in everything but direction.")
    print("Standing in front of the fork is a doe, and beside her, her young fawn.")
    cave_fork = "undefined" #Sets the variable as a value that is not one of those accepted, meaning the while loop is able to run as, while it recognises the variable, it meets the conditions for repeating the loop
    while cave_fork != "left" and cave_fork != "right" and cave_fork != "talk": #The while loop will repetitively ask the user to enter a valid response for direction if their reply to the input prompt isn't "left", "right" or "talk". The user cannot progress until a valid response is submitted
        print()
        cave_fork = input("If you want to go down the left path, enter \"left\". To go to the right, enter \"right\". To talk to the doe, enter \"talk\" ") #Ask the user what choice they wish to make in this situation and inform them of possible/valid inputs. Store their answer in a variable to check the answer's validity
        cave_fork = cave_fork.strip() #Removes all spaces from the front and end of the user's response 
        cave.fork = cave_fork.lower() #Removes all upper case letters. The above 2 lines are in order to ensure that the user needs to simply spell the word correctly, as the .strip() and .lower() make the variable non-case-sensitive
        if cave_fork != "left" and cave_fork != "right" and cave_fork != "talk": #Remind the user of the valid responses to the question if they do not answer with one of the two options, using an if loop that activates if their response is invalid
            print("Please enter either \"left\", \"right\" or \"talk\".")
            print()
    print(new_stage)
    print() 
    if cave_fork != "talk": #This if loop will be activated if, in the while loop, the user selected either left or right
        print("You continue down the {}-hand path.".format(cave_fork)) #The .format(cave_fork) at the end of this print statement inserts the user's choice from teh while loop into the {} space, as there is only one piece of code for the two directions
        print("After 5 minutes or so of walking, you start to tire.")
        print("After sitting down to rest, you look back towards the direction that you came from.")
        print()
        enter = input("Press Enter to look back down the cave ") #Prevents the game from progressing to the next level until the user has pressed the 'enter' key, thus answering the input prompt and continuing the game. Having an "enter" variable not used for anything else means they are able to type before pressing enter without changing anything in the game
        print()
        print("That's odd.")
        print("In the direction from which you came, the cave seems to have closed up.")
        print("There is no way to return back.")
        print("What's more, further ahead of you, your torch seems to be striking a wall, signalling the end of the cave.")
        print("How this has happened, you're not sure, but you seem to be well and truly stuck.")
        print("Damn.")
        global cavedeath #Import the variable "cavedeath" into the function so it is seen as a global and is thus able to be altered
        if cavedeath == 0:
            cavedeath += 1
            endings += 1 #If it is the user's first time achieving this ending in the game, add one to the variable which tracks this, and increase the variable tracking the number of endings achieved
        game_over() #Go to the game over screen from this point in the code, as this is a losing path
    print("You approach the doe, and introduce yourself as {}.".format(name)) #The .format(name) here inserts teh player's username into the {} space
    print()
    print("The doe replies:    \"Hello, {}! My name is Solace.\".".format(name)) #The .format(name) here inserts the player's username into the {} space
    print()
    enter = input("Press Enter to ask Solace for the way out ") #Prevents the game from progressing to the next level until the user has pressed the 'enter' key, thus answering the input prompt and continuing the game. Having an "enter" variable not used for anything else means they are able to type before pressing enter without changing anything in the game
    print()
    print("Solace replies:     \"Well {}, that depends on where you're going. Where do you want to go?\".".format(greet)) #The .format(greet) here inserts the relevant greeting for the player into the {} space in the print statement
    print()
    enter = input("Press Enter to tell Solace you're trying to get home to Aubernesse ") #Prevents the game from progressing to the next level until the user has pressed the 'enter' key, thus answering the input prompt and continuing the game. Having an "enter" variable not used for anything else means they are able to type before pressing enter without changing anything in the game
    print()
    print("Solace replies:     \"Oh, an Aubernesse {} are you? Well {}, I can tell you the way, but first I need some help.\"".format(lad, greet)) #The .format(lad, greet) here inserts the player's lad variable into the first {} gap in the print statement, and the player's chosen greet statement into the second {} space
    print("                    \"I really do need to help my son here, Sean, to find his tomato.\"")
    print("                    \"He's ever so hungry, you see.\"")
    tomato = "undefined" #Sets the variable as a value that is not one of those accepted, meaning the while loop is able to run as, while it recognises the variable, it meets the conditions for repeating the loop
    while tomato != "find" and tomato != "ignore": #The while loop will repetitively ask the user to enter a valid response for direction if their reply to the input prompt isn't either "find" or "ignore". The user cannot progress until a valid response is submitted
        print()
        tomato = input("Enter \"find\" to look for Sean's tomato. Enter \"ignore\" to simply continue down one of the paths ") #Ask the user what choice they wish to make in this situation and inform them of possible/valid inputs. Store their answer in a variable to check the answer's validity
        tomato = tomato.strip() #Removes all spaces from the front and end of the user's response 
        tomato = tomato.lower() #Removes all upper case letters. The above 2 lines are in order to ensure that the user needs to simply spell the word correctly, as the .strip() and .lower() make the variable non-case-sensitive
        if tomato != "find" and tomato != "ignore": #Remind the user of the valid responses to the question if they do not answer with one of the three options, using an if loop that activates if their response is invalid
            print()
            print("Please enter either \"find\" or \"ignore\".")
    print(new_stage)
    print()
    if tomato == "ignore": #If in the above while loop the user selected to ignore Solace, this if loop is activated
        print("You decide to ignore Solace's request for help.")
        left_right = "undefined" #Sets the variable as a value that is not one of those accepted, meaning the while loop is able to run as, while it recognises the variable, it meets the conditions for repeating the loop
        while left_right != "left" and left_right != "right": #The while loop will repetitively ask the user to enter a valid response for direction if their reply to the input prompt isn't either "left" or "right". The user cannot progress until a valid response is submitted
            print()
            left_right = input("If you wish to go down the left path, enter \"left\". To go right, enter \"right\" ") #Ask the user what choice they wish to make in this situation and inform them of possible/valid inputs. Store their answer in a variable to check the answer's validity
            left_right = left_right.strip() #Removes all spaces from the front and end of the user's response 
            left_right = left_right.lower() #Removes all upper case letters. The above 2 lines are in order to ensure that the user needs to simply spell the word correctly, as the .strip() and .lower() make the variable non-case-sensitive
            if left_right != "left" and left_right != "right": #Remind the user of the valid responses to the question if they do not answer with one of the two options, using an if loop that activates if their response is invalid
                print()
                print("Please enter either \"left\" or \"right\".")
        print(new_stage)
        print()
        print("You continue down the {}-hand path.".format(left_right)) #The .format(left_right) here inserts teh user's response to the above while loop into the {} space. This cannot be done by simply typing in a direction as it is the same code regardless of what the player chose in the while loop
        print("After 5 minutes or so of walking, you start to tire.")
        print("After sitting down to rest, you look back towards the direction that you came from.")
        print()
        enter = input("Press Enter to look back down the cave ") #Prevents the game from progressing to the next level until the user has pressed the 'enter' key, thus answering the input prompt and continuing the game. Having an "enter" variable not used for anything else means they are able to type before pressing enter without changing anything in the game
        print()
        print("That's odd.")
        print("In the direction from which you came, the cave seems to have closed up.")
        print("There is no way to return back.")
        print("What's more, further ahead of you, your torch seems to be striking a wall, signalling the end of the cave.")
        print("How this has happened, you're not sure, but you seem to be well and truly stuck.")
        print("Damn.")
        if cavedeath == 0:
            cavedeath += 1
            endings += 1 #If it is the user's first time achieving this ending in the game, add one to the variable which tracks this, and increase the variable tracking the number of endings achieved
        game_over() #Go to the game over screen from this point in the code, as this is a losing path
    print("You decide to look for Sean's tomato.")
    left_right = "undefined" #Sets the variable as a value that is not one of those accepted, meaning the while loop is able to run as, while it recognises the variable, it meets the conditions for repeating the loop
    while left_right != "left" and left_right != "right": #The while loop will repetitively ask the user to enter a valid response for direction if their reply to the input prompt isn't either "left" or "right". The user cannot progress until a valid response is submitted
        print()
        left_right = input("If you wish to look down the left path, enter \"left\". To look down the right, enter \"right\" ") #Ask the user what choice they wish to make in this situation and inform them of possible/valid inputs. Store their answer in a variable to check the answer's validity
        left_right = left_right.strip() #Removes all spaces from the front and end of the user's response 
        left_right = left_right.lower() #Removes all upper case letters. The above 2 lines are in order to ensure that the user needs to simply spell the word correctly, as the .strip() and .lower() make the variable non-case-sensitive
        if left_right != "left" and left_right != "right": #Remind the user of the valid responses to the question if they do not answer with one of the two options, using an if loop that activates if their response is invalid
            print()
            print("Please enter either \"left\" or \"right\".")
    if left_right == "left": #If in the above while loop the user chose left, this part of the game is played. This game has no effect on the game other than adding time.
        print()
        print("You search down the left-hand path, but, after several minutes, are unable to find any tomato.")
        print()
        enter = input("Press Enter to search down the right-hand path.") #Prevents the game from progressing to the next level until the user has pressed the 'enter' key, thus answering the input prompt and continuing the game. Having an "enter" variable not used for anything else means they are able to type before pressing enter without changing anything in the game
    print()
    print("You search for a few minutes, before finally finding Sean's tomato sitting atop a rock.")
    print("How it got there, you're unsure, as it is at your eye level, but Sean is a very short fawn.")
    global tomatoes_found #Import the variable tomatoes_found into the function so it is seen as global, and thus able to be altered
    global achievements_list #Import the variable achievements_list into the function so it is seen as global, and thus able to be appended
    if tomatoes_found == 0:
        tomatoes_found += 1
        achievements_list.append("5+ A DAY:           Find a Tomato") #If this is the first time in the user's current playing session that they have found the tomato, add one to the variable tracking this, so they can only get the achievement for this once, and give them the relevant achievement
    print()
    enter = input("Press Enter to give Solace the tomato ") #Prevents the game from progressing to the next level until the user has pressed the 'enter' key, thus answering the input prompt and continuing the game. Having an "enter" variable not used for anything else means they are able to type before pressing enter without changing anything in the game
    print()
    print("You return to the fork in the path, and hand Solace the tomato.")
    print()
    print("Solace replies:     \"Why thank you, {}! How very kind of you.\"".format(name)) #The .format(name) here inserts the user's username into the empty {} space in the print statement
    if karma == 3: #If the player has achieved the maximum possible karma score, run this section of the code. Otherwise, skip it
        print("                    \"By the way, here's something I found in the cave recently. I don't know what to do with it, maybe you will.\"")
        print("Solace hands you a polished purple orb, filled with swirling images you can barely make out.")
        print("You recognise this as the Orb or Cagim! The very object you came in here to find.")
        global orb_of_cagim #Import the variable "orb_of_cagim" into the function so it is seen as a global and is thus able to be altered
        orb_of_cagim += 1
        if orb_of_cagim == 1:
            achievements_list.append("ORB OF CAGIM:       Find the Orb of Cagim") #Add one to the variable tracking the number of times the player has been awarded the Orb of Cagim. If this is the first occurrence of this, award the player the relevant achievement
        print("You can feel immense power flowing through you.")
        print()
        enter = input("Press Enter to ask Solace the way back to Aubernesse ")
        print()
    print("                    \"To find Aubernesse, you'll want to head down the left-hand path.\"")
    print()
    enter = input("Press Enter to thank Solace and go down the left-hand path ") #Prevents the game from progressing to the next level until the user has pressed the 'enter' key, thus answering the input prompt and continuing the game. Having an "enter" variable not used for anything else means they are able to type before pressing enter without changing anything in the game
    print()
    print("Solace replies:     \"Good luck on your way {}!\"".format(greet)) #The .format(greet) here enters the user's desired greeting into the {} space
    print(new_stage)
    print()
    print("You wander down the left-hand cave, into the dark abyss.")
    print("Exactly how long you walk, you're unsure, as you lose track of time.")
    print("It could have been a matter of minutes, but it could just as easily have been several days.")
    print("Eventually, you see a pale circle in the distance.")
    print("Some time later, you stumble into the blinding light.")
    print()
    enter = input("Press Enter to continue ") #Prevents the game from progressing to the next level until the user has pressed the 'enter' key, thus answering the input prompt and continuing the game. Having an "enter" variable not used for anything else means they are able to type before pressing enter without changing anything in the game
    print()
    print("You right yourself on the outside of the cave, your eyes slowly adjusting to the light.")
    print("In the distance, you can hear children playing and the bustle of people moving around.")
    print("Soon, you're able to see your town in the distance, just one or two hundred metres away.")
    print("You are home.")
    global gamewon #Import the variable gamewon into the function so it is seen as global, and thus able to be altered
    gamewon += 1
    if gamewon == 1:
        achievements_list.append("CHAMPION:           Win Forest Adventure") #Add one to the variable which tracks the number of times the user has won the game. If it is their first time, give them the relevant achievement
    global perfect_citizen #Import the variable "perfect_citizen" into the function so it is seen as a global and is thus able to be altered
    if karma == 3:
        perfect_citizen += 1 #If the player has the maximum possible karma score, increase the variable tracking the number of times this has happened
    if perfect_citizen == 1:
        achievements_list.append("PERFECT CITIZEN:    Help Everyone while Winning the Game")
    global cavewin #Import the variable cavewin into the function so it is seen as global, and thus able to be altered
    cavewin += 1
    if cavewin == 1:
        endings += 1 #If it is the user's first time achieving this ending in the game, increase the variable tracking the number of endings achieved
    if riverwin > 0:
        if cavewin == 1:
            achievements_list.append("BORN WINNER:        Win Forest Adventure in Two Different Manners") #If this is the player's first time winning the game through this path, add one to the variable which tracks this, and, if they have also won the game through the other path before, give the user the relevant achievement
    game_won() #Go to the game win screen
    


#CARRY OUT SETUP
title() #Display the game's title
enter = input("Press Enter to start the game: ") #Prevents the game from progressing to the next level until the user has pressed the 'enter' key, thus answering the input prompt and continuing the game. Having an "enter" variable not used for anything else means they are able to type before pressing enter without changing anything in the game
new_stage = "_______________________________________________________________________________" #Printing the new_stage variable will display a horizontal line (consisting of underscore characters) across the screen. This is useful as it helps to seperate different stages and aspects of the game, making it better to read and making it dislay nicer
print(new_stage) #The new_stage here is to signify the end of the "Welcome" stage of the game
print()
name_valid = False
while name_valid == False: #This while loop ensures that the user's chosen name is, in fact, a name, by ensuring that there is at least one character. Special characters are allowed, as it is only a username, but characters must be used. Until the user submits a name with characters in it, they will be asked to submit a new username
    name = input("Welcome traveller! By what name do you go by? ")
    name = name.strip() #Removes spaces from the front of the username so that there must be at least one character in the username A space is not counted as a character here
    name_length = len(name) #Creates a variable measuring the length of the player's chosen username to assess whether the user has entered any input
    special_characters_list = ["~", "`", "!", "@", "$", "#", "%", "^", "&", "*", "(", ")", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "_", "+", "=", "{", "[", "}", "]", "|", "\\", ":", ";", "\"", "<", ",", ">", ".", "?", "/"] #A list of all invalid characters - the characters on a regular English keyboard other than letters, hyphens and apostrophes
    list_size = len(special_characters_list) #A variable containing the length of the special characters list
    false_character = False #Prior to checking the name, this variable confirms that the name verifier has not yet sensed any invalid characters
    for i in range(list_size): #This for loop repeats in range list size so that for every iteration it checks if a different character in special_characters_list is in the user's inputted name
        if false_character == False: #The for loop will only check the user's name if it has not yet found a special character in the string (as one special character in the strin will have the same outcome as ten, for example)
            character_check = special_characters_list[i] #Creates a variable stating the special character from the list that is being checked in this iteration of the for loop, e.g., the first in the list on the first iteration, or the eleventh in the list during the eleventh iteration
            if character_check in name: #In each iteration of the for loop the program will find if the character in the list it is currently scanning for is in the user's selected name
                false_character = True #If an invalid character is found in the string, the false_character value will be set to True 
    if false_character == True:
        name_valid = False   
        print()
        print("Name cannot contain special characters.") #The above four lines of code assess whether the user's chosen name contains invalid/special characters. If so, the username validity is set to False and the while  loop repeats, as they are asked to enter a new name
    elif name_length == 0:
        name_valid = False
        print()
        print("Please input a name.") #The above four lines of code assess whether the user has entered anything for their desired username. If not, the username validity is set as false and the while loop repeats, as they are asked to enter a new name
    elif name_length > 20 or name_length == 1:
        name_valid = False
        print()
        print("Please select a name containing 2-20 characters.") #The above four lines of code assess whether the user has inputted a username with a valid length. The required length for a name in the game is 2-20 characters, so if the user's name does not fit these parameters, name validity will be set to false and they ill be asked to input a different name
    elif name[0] == "-" or name[0] == "'" or name[name_length - 1] == "-" or name[name_length - 1] == "'":
        name_valid = False
        print()
        print("Hyphens and apostrophes may not appear as the first or last letter of a name") #The above four lines of code check the first and last letter of the string, and see if they contain a hyphen or apostrophe (the only two special characters not checked by the special character loop). If either the first or last character of the name is a hyphen, name validity will be set to false and they will be asked to enter a different name
    else:
        name_valid = True #If the user's selected name fits all parameters (no special characters, 2-20 characters, no hyphens at the start or end), the name validity will be set to true
name = name.title() #Puts the name variable into Title Case, as names gramatically must start with capitals, so the .title() function ensures that the first letter of each word is a capital and the rest are lower-case
print()
print("Nice! {} is a really cool name!".format(name)) #Print the user's name in a sentence to ensure that it has been entered and confirm with the user that their input has been registered
print("Now, what is your preferred gender?")
gender = 0
while gender != "1" and gender != "2" and gender != "3": #As long as the user's input for desired gender is invalid (not one of the three options), ask them for a valid answer by repeating the question inside a while loop
    gender = str(input("Enter 1 to select Female. Enter 2 to select Male. Enter 3 to select Other ")) #Despite asking for number values, in this game I shall always have input lines as str(input. This is to prevent the game from crashing if they decide to enter a string character rather than an integer
    gender = gender.strip()
    if gender == "1": #If the user inputs their preferred gender as female (Option 1), their pronouns/greetings will be set as the feminine options, and the gender variable is changed so that the while loop is ended and the game can progress
        greet = "Madam"
        lad = "lass"
        dude = "dudette"
    elif gender == "2": #If the user inputs their preferred gender as male (Option 2), their pronouns/greetings will be set as the masculine options, and the gender variable is changed so that the while loop is ended and the game can progress
        greet = "Sir"
        lad = "lad"
        dude = "dude"
    elif gender == "3": #If the user inputs their preferred gender as other (Option 3), their pronouns/greetings will be set as the gender-neutral options, and the gender variable is changed so that the while loop is ended and the game can progress
        greet = "traveller"
        lad = "kid"
        dude = "fam"
    else: #Repeat the while loop and once more ask them for their gender if they do not answer with a valid input
        print("Please select one of the three options.")
print()
print("Welcome, {}!".format(greet)) #State the user's gender in a sentence to ensure that it has been entered and confirm with the user that their input has been registered
print("Before we start, it is recommended - but not required - that you have the Python shell in FULL SCREEN MODE while playing this game.")
print("While this will not affect the gameplay, it will greatly improve the layout and aesthetic :)")
tutorial = 0 #Sets the variable as a value that is not one of those accepted, meaning the while loop is able to run as, while it recognises the variable, it meets the conditions for repeating the loop
while tutorial != "yes" and tutorial != "no": #Repetitively ask the user whether they want to go through the tutorial if they do not answer with an appropriate response ("yes" or "no")
    tutorial = str(input("Do you wish to play an extremely brief tutorial? Type \"yes\" to go through the short tutorial. Type \"no\" to start playing. ")) #Asks the user if they want to pla through the tutorial
    tutorial = tutorial.strip() #Removes all spaces from the front and end of the user's response 
    tutorial = tutorial.lower() #Removes all upper case letters. The above 2 lines are in order to ensure that the user needs to simply spell the word correctly, as the .strip() and .lower() make the variable non-case-sensitive
    if tutorial != "yes" and tutorial != "no": #Remind the user of the valid responses to the question if they do not answer with one of the two options ("yes" or "no"), using an if loop that activates if their response is invalid
        print()
        print("Please choose either \"yes\" or \"no\".") #The above 7 lines of code are the primary decision-making code structure in this game
        print()
print(new_stage) #The new_stage here is to signify the end of the "Set Up" stage
print()
if tutorial == "yes": #If in the "Set Up" stage the user asked to undergo the tutorial, the "Tutorial" stage will commence. Otherwise, the code shall skip this section and go straight to the game's start ("Path Split" stage)
    tutorial_code()


#PLAY GAME
game() #Start playing the game
