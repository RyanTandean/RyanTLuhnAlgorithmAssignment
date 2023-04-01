# Throughout this project, the use of data structures are not permitted 
# Minimal built in functions are to be used and the majority of functions must be
# created yourself

# More packages may be imported in the space below if approved by your instructor
import os

def printMenu():
    print('''
          Customer and Sales System\n
          1. Enter Customer Information\n
          2. Generate Customer data file\n
          3. Report on total Sales (Not done in this part)\n
          4. Check for fraud in sales data (Not done in this part)\n
          9. Quit\n
          Enter menu option (1-9)
          ''')

'''
    This function is to be edited to achieve the task.
    It is your decision to make this function a procedural or functional type
    You may place as many or as few parameters as needed
    This function may also be broken down further depending on your algorithm/approach
'''
def enterCustomerInfo():
    '''
    Asks user for first name, last name, city, postal code, credit card number

    For first name, last name, city, uses a while loop to make sure the user is submiting nothing

    For credit card and postal code, calls on the other 2 functions, validatePostalCode() and validateCreditCard()

    Then uses a while loop so until postal code and credit card are validated, the user cannot progress
    After everything is validated, returns all of the customer information as a tuple so it can be used for 
    generating the CSV for the user
    '''
    print()
    firstName = input("First name: ")
    while firstName == "":
        print("This field cannot be left empty")
        print()
        firstName = input("First name: ")
    lastName = input("Last name: ")
    while lastName == "":
        print("This field cannot be left empty")
        print()
        lastName = input("Last name: ")
    city = input("City: ")
    while city == "":
        print("This field cannot be left empty")
        print()
        city = input("City: ")
    postalCode = str(input("Postal Code: "))
    postalCodeThree = postalCode[:3]
    while (validatePostalCode(postalCode, postalCodeThree) == False):
        print()
        postalCode = str(input("Postal Code: "))
        postalCodeThree = postalCode[:3]
    creditCard = str(input("Credit Card Number: "))
    while (validateCreditCard(creditCard) == False):
        print()
        creditCard = str(input("Credit Card Number: "))
    print("All information validated, information saved")
    return firstName, lastName, city, postalCode, creditCard

'''
    This function is to be edited to achieve the task.
    It is your decision to make this function a procedural or functional type
    You may place as many or as few parameters as needed
    This function may also be broken down further depending on your algorithm/approach
'''

def validatePostalCode(a, b):
    '''
    First, checks if the postal code submitted is less than 3 characthers

    Then opens and reads the postal codes CSV to compare the first 3 characters of the postal code submitted 
    agaisnt any of the first 3 characters of the postal codes in the CSV

    if there is a match, return True for validated

    if there is no match, return False for not validated
    
    
    '''
    if len(a)<3:
        print("Invalid postal code")
        return False
    else:
        folder = os.getcwd()
        fileName = folder + "\\RyanTLuhnAlgorithmAssignment\\postal_codes.csv"
        file = open(fileName, "r")
        text = file.readline()
        while text != "":
            text = file.readline()
            postalData = text[:3]
            if b == postalData:
                return True
            
        if b != postalData:
            print("Invalid postal code")
            return False
        file.close()   
    
    

    
'''
    This function is to be edited to achieve the task.
    It is your decision to make this function a procedural or functional type
    You may place as many or as few parameters as needed
    This function may also be broken down further depending on your algorithm/approach
'''
def validateCreditCard(a):
    '''
    First checks if the length of the credit card number is valid

    Then checks if the credit card is valid, (if the sum after going through the Luhn algorithm ends with 0)

    return True if valid

    return False if not valid

    
    '''
    if len(a) < 9 or len(a) > 16:
        print("Invalid Credit Card Number")
        return False
    else:
        sum1 = 0
        sum2 = 0
        reverseCredit = a[::-1]
        cardCharCount = len(reverseCredit)
        for i in range(cardCharCount):
            if int(i) % 2 == 0: #Since position of strings starts from 0. every "odd digit position" will be every "even digit position" in code
                sum1 = sum1 + int(reverseCredit[i])
            elif int(i) % 2 != 0:
                doubleDigit = int(reverseCredit[i])*2
                if doubleDigit > 9:
                    firstDigit = str(doubleDigit)[0]
                    secondDigit = str(doubleDigit)[1]
                    newSum = int(firstDigit) + int(secondDigit)
                    sum2 = sum2 + newSum
                else:
                    sum2 = sum2 + doubleDigit
        finalSum = sum1 + sum2
        endZero = str(finalSum)[1]
        if int(endZero) != 0:
            print("Invalid credit card")
            return False
        else:
            return True
'''      
    This function is to be edited to achieve the task.
    It is your decision to make this function a procedural or functional type
    You may place as many or as few parameters as needed
    This function may also be broken down further depending on your algorithm/approach
'''
def generateCustomerDataFile():
    '''
    If it does not exist, creates a file called "CustomerInformation.csv" as write

    If it does exist, opens a file called "CustomerInformation.csv" as append

    Eitheir way, it adds the current saved information of the customer

    It does this by taking the tuple returned from the enterCustomerInfo() function and seperating the items
    
    id is assigned using line count

    
    '''
    first_name, last_name, city_, postal_code, credit_card = info
    folder = os.getcwd()
    fileName = folder + "\\RyanTLuhnAlgorithmAssignment\\CustomerInformation.csv"
    isFile = os.path.isfile(fileName)
    print("Information added to CSV")

    if isFile == False:
        file = open(fileName, "w")
        file.writelines("ID | First Name | Last Name | City | Postal Code | Credit Card Number"+"\n")
        file.writelines("1"+" | "+first_name+" | "+last_name+" | "+city_+" | "+postal_code+" | "+credit_card+"\n")
        file.close
    elif isFile == True:
        file = open(fileName, "r")
        line = file.readlines()
        lineCount = int(len(line))
        file.close
        id = str(lineCount) + " | "
        file = open(fileName, "a")
        file.writelines(id+first_name+" | "+last_name+" | "+city_+" | "+postal_code+" | "+credit_card+"\n" )
        file.close

####################################################################
#       ADDITIONAL METHODS MAY BE ADDED BELOW IF NECESSARY         #
####################################################################




####################################################################
#                            MAIN PROGRAM                          #
#           DO NOT EDIT ANY CODE EXCEPT WHERE INDICATED            #
####################################################################

# Do not edit any of these variables
userInput = ""
enterCustomerOption = "1"
generateCustomerOption = "2"
exitCondition = "9"

# More variables for the main may be declared in the space below


while userInput != exitCondition:
    printMenu()                 # Printing out the main menu
    userInput = input();        # User selection from the menu

    if userInput == enterCustomerOption:
        # Only the line below may be editted based on the parameter list and how you design the method return
        # Any necessary variables may be added to this if section, but nowhere else in the code
        info = enterCustomerInfo()

    elif userInput == generateCustomerOption: 
        # Only the line below may be editted based on the parameter list and how you design the method return
        generateCustomerDataFile()

    else:
        print("Please type in a valid option (A number from 1-9)")

#Exits once the user types 
print("Program Terminated")