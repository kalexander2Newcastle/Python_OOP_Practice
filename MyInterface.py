from HelperClass.MyReader import *

class MyInterface:

    @staticmethod
    def run():


        # Read In Contacts
        MyReader.readInFiles('InputFiles/input.txt')

        # Display the interface
        MyInterface.displayMenu()

    @staticmethod
    def displayMenu():
        print("\n")
        print("*************************** MAIN MENU ***************************")
        print("\n")
        print("1. Display Cards")
        print("2. Search Cards")
        print("3. Amend Cards")
        print("\n")

        userInput = int(input("Please select a menu option: "))

        if userInput == 1:
            MyInterface.displayCards()
        elif userInput == 2:
            pass
        elif userInput == 3:
            pass

    @staticmethod
    def displayCards():
        TradingCardManager.displayAllCards()



