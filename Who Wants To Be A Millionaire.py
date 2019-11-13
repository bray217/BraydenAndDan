#INITIALISATIONS
import random
import sys
import time
line = "________________________________________________________________________________"
audience = 1
audience_list = []
fifty = 1
fifty_list = []
phone = 1
phone_list = ["Sam", "Holly", "Anne", "Kayla", "Brayden", "Dylan", "Tom"]
topic_list = ["Planet Earth", "Pop Culture", "History", "Art", "Science", "Sport", "Food"]
questions_answered = 0


#FUNCTION DEFINITION

#TITLE SCREEN
def title():
    print("                  __  __ _ _ _ _                   _           ")
    print("                 |  \/  (_) | (_)                 (_)          ")
    print("                 | \  / |_| | |_  ___  _ __   __ _ _ _ __ ___  ")
    print("                 | |\/| | | | | |/ _ \| '_ \ / _` | | '__/ _ \ ")
    print("                 | |  | | | | | | (_) | | | | (_| | | | |  __/ ")
    print("                 |_|  |_|_|_|_|_|\___/|_| |_|\__,_|_|_|  \___| ")
    print(line)
    print()
    global audience
    audience = 1
    global audience_list
    audience_list = []
    global fifty
    fifty = 1
    global fifty_list
    fifty_list = []
    global phone
    phone = 1
    global phone_book
    phone_book = []
    global topic_book
    topic_book = []
    global phone_list
    phone_list = ["Sam", "Holly", "Anne", "Kayla", "Brayden", "Dylan", "Tom"]
    global topic_list
    topic_list = ["Planet Earth", "Pop Culture", "History", "Art", "Science", "Sport", "Food"]
    global questions_answered
    questions_answered = 0

#SETUP
def setup():
    print("Welcome to Who Wants To Be A Millionaire?")
    print("My name's Dan.")
    name_valid = False
    while name_valid == False: #This while loop ensures that the user's chosen name is, in fact, a name, by ensuring that there is at least one character. Special characters are allowed, as it is only a username, but characters must be used. Until the user submits a name with characters in it, they will be asked to submit a new username
        name = input("What's your name? ")
        name = name.strip() #Removes spaces from the front of the username so that there must be at least one character in the username A space is not counted as a character here
        name_length = len(name) #Creates a variable measuring the length of the player's chosen username to assess whether the user has entered any input
        special_characters_list = ["~", "`", "!", "@", "$", "#", "%", "^", "&", "*", "(", ")", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "_", "+", "=", "{", "[", "}", "]", "|", "\\", ":", ";", "\"", "<", ",", ">", ".", "?", "/"]
        list_size = int(len(special_characters_list))
        false_character = False
        for i in range(list_size):
            if false_character == False:
                character_check = special_characters_list[i]
                if character_check in name:
                    false_character = True
        if false_character == True:  
            name_valid = False 
            print()
            print("Name cannot contain special characters.") #The above four lines of code run as a way of checking whether there is a special character in the user's chosen name. If there is, the while loop will repeat as the name validity will be false. It is formatted as it is, as it did not work when I simply had all of the special characters inside a bracket with an "in name" afterwards, and this, while convoluted, was the only solution I could find
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
            print("Hyphens or apostrophes may not appear as the first or last letter of a name") #The above four lines of code check the first and last letter of the string, and see if they contain a hyphen or apostrophe (the only two special characters not checked by the special character loop). If either the first or last character of the name is a hyphen, name validity will be set to false and they will be asked to enter a different name
        else:
            name_valid = True #If the user's selected name fits all parameters (no special characters, 2-20 characters, no hyphens at the start or end), the name validity will be set to true
    name = name.title() #Puts the name variable into Title Case, as names gramatically must start with capitals, so the .title() function ensures that the first letter of each word is a capital and the rest are lower-case
    print()
    print("Welcome, {}.".format(name))
    enter = input("Press Enter to play Who Wants To Be A Millionaire? ")
    print()
    print("Starting...")
    for i in range(3):
        print(".")
        time.sleep(1)
    print(line)
    print()
    global audience
    audience = 1
    global audience_list
    audience_list = []
    global fifty
    fifty = 1
    global fifty_list
    fifty_list = []
    global phone
    phone = 1
    global questions_answered
    questions_answered = 0

#START
def start():
    q1 = random.randint(1,8)
    if q1 == 1:
        question("Which city contains the Eiffel Tower?", "Sydney", "New York", "Los Angeles", "Paris", "D", "C", "B", "A", 0, 100, "Planet Earth")
    elif q1 == 2:
        question("Who wasn't a member of The Beatles?", "John Lennon", "Justin Timberlake", "Paul McCartney", "Ringo Starr", "B", "D", "A", "C", 0, 100, "Pop Culture")
    elif q1 == 3:
        question("In what century was the First World War?", "18th", "19th", "20th", "21st", "C", "B", "A", "D", 0, 100, "History")
    elif q1 == 4:
        question("Who painted the Mona Lisa?", "Leonardo DiCaprio", "Lionel Messi", "Leo Tolstoy", "Leonardo da Vinci", "D", "A", "C", "B", 0, 100, "Art")
    elif q1 == 5:
        question("What gas makes voices sound higher when inhaled?", "Helium", "Oxygen", "Nitrogen", "Sulfur Hexafluoride", "A", "D", "C", "B", 0, 100, "Science")
    elif q1 == 6:
        question("Which of the following sports has multiple balls in play at one time?", "Soccer", "Rugby", "Pool", "Golf", "C", "B", "D", "A", 0, 100, "Sport")
    else:
        question("Which restaurant chain is famous for the \"Big Mac\"?", "McDonalds", "Taco Bell", "Subway", "Wendy's", "A", "D", "C", "B", 0, 100, "Food")

#QUESTION
def question(question, optiona, optionb, optionc, optiond, correct_option, wronga, wrongb, wrongc, money_got, money_getting, topic):
    global audience
    global audience_list
    global fifty
    global fifty_list
    global phone
    global phone_book
    global phone_list
    global topic_list
    global topic_book
    lifelines = audience + fifty + phone
    print("For ${}, here is your question.".format(money_getting))
    print("Your number of remaining lifelines is: {}".format(lifelines))
    time.sleep(1)
    print(line)
    print()
    print(question)
    print()
    time.sleep(3)
    print("A: {}".format(optiona))
    time.sleep(0.5)
    print("B: {}".format(optionb))
    time.sleep(0.5)
    print("C: {}".format(optionc))
    time.sleep(0.5)
    print("D: {}".format(optiond))
    print(line)
    print()
    time.sleep(1)
    fifty_question = False
    answer = ""
    while answer != "a" and answer != "b" and answer != "c" and answer != "d":
        print("What do you think the answer could be?")
        if fifty_question == False:
            print("You may enter A, B, C or D to answer.")
        else:
            print("You may enter either {} or {} to answer.".format(letter1, letter2))
        if audience == 1:
            print("To ask the audience, enter \"Audience\".")
        if fifty == 1:
            print("To go for a 50-50, enter \"Fifty\".")
        if phone == 1:
            print("To phone a friend, enter \"Phone\".")
        print()
        answer = str(input("What do you want to do? "))
        answer = answer.strip()
        answer = answer.lower()
        if answer == "audience":
            if audience == 1:
                audience -= 1
                print()
                print("The audience is voting...")
                for i in range(3):
                    time.sleep(1)
                    print(".")
                print()
                time.sleep(1)
                print("The audience has decided:")
                if fifty_question == False:
                    if money_getting < 2000:
                        pcent_1 = random.randint(70, 81)
                        pcent_2 = random.randint(8, 11)
                        pcent_3 = random.randint(8, 10)
                    elif money_getting < 64000:
                        pcent_1 = random.randint(30, 46)
                        pcent_2 = random.randint(25, 31)
                        pcent_3 = random.randint(15, 20)
                    else:
                        pcent_1 = random.randint(23, 29)
                        pcent_2 = random.randint(21, 27)
                        pcent_3 = random.randint(19, 25)
                    pcent_4 = 100 - pcent_1 - pcent_2 - pcent_3
                    audience_list.append("{}: {}%".format(correct_option, pcent_1))
                    audience_list.append("{}: {}%".format(wronga, pcent_2))
                    audience_list.append("{}: {}%".format(wrongb, pcent_3))
                    audience_list.append("{}: {}%".format(wrongc, pcent_4))
                else:
                    if money_getting < 2000:
                        pcent_1 = random.randint(80,91)
                    elif money_getting < 64000:
                        pcent_1 = random.randint(65, 76)
                    else:
                        pcent_1 = random.randint(46, 58)
                    pcent_2 = 100 - pcent_1
                    audience_list.append("{}: {}%".format(correct_option, pcent_1))
                    audience_list.append("{}: {}%".format(fifty_letter, pcent_2))
                audience_list.sort()
                for i in range(len(audience_list)):
                    print(audience_list[i])
                print(line)
                print()
                time.sleep(1)
            else:
                print()
                print("You've already used that lifeline, unfortunately!")
                print(line)
                print()
                time.sleep(1)
        elif answer == "fifty":
            if fifty == 1:
                fifty -=1
                fifty_question = True
                print()
                print("The computer will now remove two random incorrect options...")
                for i in range(3):
                    print(".")
                    time.sleep(1)
                print()
                print("Your two remaining options are:")
                fifty_keep = random.randint(1,4)
                if correct_option == "A":
                    fifty_list.append("A: {}".format(optiona))
                    if fifty_keep == 1:
                        fifty_list.append("B: {}".format(optionb))
                        fifty_letter = "B"
                    if fifty_keep == 2:
                        fifty_list.append("C: {}".format(optionc))
                        fifty_letter = "C"
                    else:
                        fifty_list.append("D: {}".format(optiond))
                        fifty_letter = "D"
                elif correct_option == "B":
                    fifty_list.append("B: {}".format(optionb))
                    if fifty_keep == 1:
                        fifty_list.append("A: {}".format(optiona))
                        fifty_letter = "A"
                    if fifty_keep == 2:
                        fifty_list.append("C: {}".format(optionc))
                        fifty_letter = "C"
                    else:
                        fifty_list.append("D: {}".format(optiond))
                        fifty_letter = "D"
                elif correct_option == "C":
                    fifty_list.append("C: {}".format(optionc))
                    if fifty_keep == 1:
                        fifty_list.append("A: {}".format(optiona))
                        fifty_letter = "A"
                    if fifty_keep == 2:
                        fifty_list.append("B: {}".format(optionb))
                        fifty_letter = "B"
                    else:
                        fifty_list.append("D: {}".format(optiond))
                        fifty_letter = "D"
                elif correct_option == "D":
                    fifty_list.append("D: {}".format(optiond))
                    if fifty_keep == 1:
                        fifty_list.append("A: {}".format(optiona))
                        fifty_letter = "A"
                    if fifty_keep == 2:
                        fifty_list.append("B: {}".format(optionb))
                        fifty_letter = "B"
                    else:
                        fifty_list.append("C: {}".format(optionc))
                        fifty_letter = "C"
                fifty_list.sort()
                letters_left = []
                letters_left.append(correct_option)
                letters_left.append(fifty_letter)
                letters_left.sort()
                letter1 = letters_left[0]
                letter2 = letters_left[1]
                for i in range(2):
                    print(fifty_list[i])
                print(line)
                print()
                time.sleep(1)
            else:
                print()
                print("You've already used that lifeline, unfortunately!")
                print(line)
                print()
                time.sleep(1)
        elif answer == "phone":
            if phone == 1:
                phone -= 1
                print()
                for i in range(3):
                    removal = random.randint(0, len(phone_list) - 1)
                    name_change = phone_list[removal]
                    topic_change = topic_list[removal]
                    phone_list.remove(phone_list[removal])
                    topic_list.remove(topic_list[removal])
                    phone_book.append(name_change)
                    topic_book.append(topic_change)
                print("Your available friends to call are:")
                for i in range(3):
                    print("{}. {}: The {} Expert".format(i + 1, phone_book[i], topic_book[i]))
                    time.sleep(0.5)
                print()
                choice = ""
                while choice != "1" and choice != "2" and choice != "3":
                    choice = str(input("Which friend do you want to call about this question? (enter either 1, 2 or 3) "))
                    choice = choice.strip()
                    if choice != "1" and choice != "2" and choice != "3":
                        print()
                        print("That's not an option here.")
                        print()
                        time.sleep(1)
                choice = int(choice)
                print()
                print("Now calling {}...".format(phone_book[choice - 1]))
                for i in range(3):
                    print(".")
                    time.sleep(1)
                enter = str(input("Press Enter to ask {} the question ".format(phone_book[choice - 1])))
                time.sleep(1)
                for i in range(3):
                    print(".")
                    time.sleep(1)
                odds = random.randint(1,41)
                if fifty_question == False:
                    if money_getting < 2000:
                        if odds < 36 and topic == topic_book[choice - 1]:
                            print("Oh! That's easy! The answer is {}!".format(correct_option))
                        elif odds < 32:
                            print("Oh! That's easy! The answer is {}!".format(correct_option))
                        else:
                            guess = random.randint(1,5)
                            if guess == 1:
                                guess_letter == "A"
                            elif guess == 2:
                                guess_letter == "B"
                            elif guess == 3:
                                guess_letter == "C"
                            else:
                                guess_letter == "D"
                            print("Damn... for some reason I just can't seem to remember right now, sorry. My best guess would be {}.".format(guess_letter))
                    elif money_getting < 64000:
                        if odds < 28 and topic == topic_book[choice - 1]:
                            print("Good question... I'm fairly sure the answer is {}.".format(correct_option))
                        elif odds < 20:
                            print("Good question... I'm fairly sure the answer is {}.".format(correct_option))
                        else:
                            guess = random.randint(1,5)
                            if guess == 1:
                                guess_letter == "A"
                            elif guess == 2:
                                guess_letter == "B"
                            elif guess == 3:
                                guess_letter == "C"
                            else:
                                guess_letter == "D"
                            print("That's tricky... I can't remember right now, sorry. My best guess would be {}.".format(guess_letter))
                    else:
                        if odds < 20 and topic == topic_book[choice - 1]:
                            print("What a difficult question! The answer is {}, I think. But don't quote me on that.".format(correct_option))
                        elif odds < 14:
                            print("What a difficult question! The answer is {}, I think. But don't quote me on that.".format(correct_option))
                        else:
                            guess = random.randint(1,5)
                            if guess == 1:
                                guess_letter == "A"
                            elif guess == 2:
                                guess_letter == "B"
                            elif guess == 3:
                                guess_letter == "C"
                            else:
                                guess_letter == "D"
                            print("That's hard... I'm not sure in all honesty. My best guess would be {}.".format(guess_letter))
                else:
                    if money_getting < 2000:
                        if odds < 38 and topic == topic_book[choice - 1]:
                            print("Oh! That's easy! The answer is {}!".format(correct_option))
                        elif odds < 36:
                            print("Oh! That's easy! The answer is {}!".format(correct_option))
                        else:
                            guess = random.randint(1,3)
                            if guess == 1:
                                print("Damn... for some reason I just can't seem to remember right now, sorry. My best guess would be {}.".format(correct_option))
                            else:
                                print("Damn... for some reason I just can't seem to remember right now, sorry. My best guess would be {}.".format(fifty_letter))
                    elif money_getting < 64000:
                        if odds < 34 and topic == topic_book[choice - 1]:
                            print("Good question... I'm fairly sure the answer is {}.".format(correct_option))
                        elif odds < 30:
                            print("Good question... I'm fairly sure the answer is {}.".format(correct_option))
                        else:
                            guess = random.randint(1,3)
                            if guess == 1:
                                print("That's tricky... I can't remember right now, sorry. My best guess would be {}.".format(correct_option))
                            else:
                                print("That's tricky... I can't remember right now, sorry. My best guess would be {}.".format(fifty_letter))
                    else:
                        if odds < 30 and topic == topic_book[choice - 1]:
                            print("What a difficult question! The answer is {}, I think. But don't quote me on that.".format(correct_option))
                        elif odds < 24:
                            print("What a difficult question! The answer is {}, I think. But don't quote me on that.".format(correct_option))
                        else:
                            guess = random.randint(1,3)
                            if guess == 1:
                                print("That's hard... I'm not sure in all honesty. My best guess would be {}.".format(correct_option))
                            else:
                                print("That's hard... I'm not sure in all honesty. My best guess would be {}.".format(fifty_letter))
                for i in range(3):
                    print(".")
                    time.sleep(1)
                enter = str(input("Press Enter to thank {} ".format(phone_book[choice - 1])))
                print(line)
                print()
                time.sleep(1)
            else:
                print()
                print("You've already used that lifeline, unfortunately!")
                print(line)
                print()
                time.sleep(1)
        elif answer != "a" and answer != "b" and answer != "c" and answer != "d":
            print()
            print("That's not a valid answer.")
            print(line)
            print()
            time.sleep(1)
        elif fifty_question == True:
            if answer.upper() != letters_left[0] and answer.upper() != letters_left[1]:
                print()
                print("Those options have already been removed!")
                answer = ""
                print(line)
                print()
                time.sleep(1)
                          
#START RUNNING CODE
title()
setup()
start()

