#CALCULATOR FOR THE nTH FIBONACCI NUMBER

import locale
locale.setlocale(locale.LC_ALL, 'en_US')
digits = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "."] #List of characters that can be in the number entered by the user

#PHI CALCULATION
import math #Import math so that the math.sqrt() and math.pow() operators work
phi = (1 + math.sqrt(5)) / 2 #Set up definition of Phi

#CALCULATOR
def fibonacci_calculator(): #Calculator, played on repeat
    number_checked = 0.1 #Initialise value with invalid value so the variable is recognised but activates the loop
    while number_checked % 1 != 0 or number_checked > 1474 or number_checked < 0: #Repeat the loop while the user has not entered a valid integer
        number_real = False #Number is initially invalid prior to input
        while number_real == False: #Repeat until number is valid
            number_checked = str(input("Enter any integer value ")) #Get user's input for number and store it in a string
            digit_check = len(number_checked) #Get number of characters in the user's number
            decimals = 0 #Variable that checks the number of decimal points in the number
            for i in range(digit_check): #Check each of the characters in the user's number and see if it only contains the 11 valid characters so there will be no error in converting it to a float value
                if number_checked[i] == ".":
                    decimals += 1 #Increase the number of decimals points detected in the number
                if number_checked[i] not in digits:
                    number_real = False #Number is not valid if a character does not appear in the valid characters list
                else:
                    if decimals > 1:
                        number_real = False #Number is not valid if there are two or more decimal points in the number
                    else:
                        number_real = True #If all of the characters in the user's number are valid and tehre is less than two decimal points, the number is valid and can be used. 
            if number_real == False:
                print()
                print("That is not an integer value")
                print("(Note: please do not include commas if writing longer numbers)")
                print() #Inform the user that their chosen number was invalid
            else:
                number_checked = float(number_checked) #Number is converted to float so that n.0 is supported
        if number_checked % 1 != 0: #Check to see if the number is divisible by one (and is therefore an integer). If not, ask them to enter a new number.
            print()
            print("That is not an integer value")
            print()
        if number_checked > 1474: #Check to see if the number selected is so large that the resulting calculation will crash Python. If so, ask the user to enter a new number.
            print()
            print("Python isn't powerful enough to handle numbers with over 110,000 digits, which your Fibonacci number has")
            print("Please enter a smaller number (maximum of 1474)")
            print()
        if number_checked < 0: #Check to see if the user's number is negative. If so, ask the user to enter a new number.
            print()
            print("That is not a valid number")
            print("Please enter a number greater than or equal to zero")
            print()
    fib_number = (math.pow(phi, number_checked) - math.pow((0 - phi), (0 - number_checked))) / math.sqrt(5) #Calculate Fibonacci number using Binet's Formula
    fib_number = round(fib_number) #Round the resultant number to the nearest whole number to prevent rounding error from rationality of Phi in the program
    fib_number = f'{fib_number:n}'
    number_checked = round(number_checked) #Change the user's number to an integer value
    number_checked = f'{number_checked:n}'
    print("Fibonacci number #{} is: {}".format(number_checked, fib_number)) #Put the user's number and the resulting Fibonacci number in the {} spaces
    print("_________________________________________________________")
    print()
    fibonacci_calculator() #Repeat the calculation

#STARTUP
print("  ______ _ _                                _ ")
print(" |  ____(_) |                              (_)")
print(" | |__   _| |__   ___  _ __   __ _  ___ ___ _ ")
print(" |  __| | | '_ \ / _ \| '_ \ / _` |/ __/ __| |")
print(" | |    | | |_) | (_) | | | | (_| | (_| (__| |")
print(" |_|    |_|_.__/ \___/|_| |_|\__,_|\___\___|_|")
print("   _____      _            _       _            ")
print("  / ____|    | |          | |     | |           ")
print(" | |     __ _| | ___ _   _| | __ _| |_ ___  _ __ ")
print(" | |    / _` | |/ __| | | | |/ _` | __/ _ \| '__|")
print(" | |___| (_| | | (__| |_| | | (_| | || (_) | |   ")
print("  \_____\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|   ")
print("_________________________________________________")
print()
print("Welcome to the Fibonacci Calculator")
print("This calculator will find the value of whichever Fibonacci number you desire")
print("Simply enter any integer value")
print()
enter = input("Press Enter to begin ")
print()
fibonacci_calculator() #Commence the calculation
