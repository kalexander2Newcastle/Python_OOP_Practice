class TradingCardManager:

    cardList = []

    @staticmethod
    def addCard(card):
        TradingCardManager.cardList.append(card)

    @staticmethod
    def getCardList():
        return TradingCardManager.cardList

    @staticmethod
    def displayAllCards():

        printBuffer = ""

        for card in TradingCardManager.cardList:
            printBuffer += (str(card) + '\n')

        print(printBuffer)

# ======================================================================================================================

    @staticmethod # Error handling/ input tidying
    def findByName():

        # Good Case - Find
        print("Enter the name of the card you want to find: ")
        userInputN = str(input("Name: "))
        userInputN = userInputN.strip()

        localList = []

        for card in TradingCardManager.cardList:
            if userInputN == card.getName():
                localList.append(card)

        # Bad Case - We don't find the card
        if not localList:
            print("Could not try card")
            return None

        return localList

    @staticmethod
    def findByHP():

        # Good Case - Find
        print("Enter the hp of the card you want to find: ")
        userInputH = int(input("HP: "))
        userInputH = userInputH.strip()

        # TODO

        for card in TradingCardManager.cardList:
            if userInputH == card.HP():
                return card

        # Bad Case - We don't find the card
        print("Could not try card")
        return None

    @staticmethod
    def findByAttack():

        # Good Case - Find
        print("Enter the attack of the card you want to find: ")
        userInputA = int(input("Attack: "))
        userInputA = userInputA.strip()

        # TODO

        for card in TradingCardManager.cardList:
            if userInputA == card.Attack():
                return card

        # Bad Case - We don't find the card
        print("Could not try card")
        return None

    @staticmethod
    def findByDefense():

        # Good Case - Find
        print("Enter the defense of the card you want to find: ")
        userInputD = int(input("Defense: "))
        userInputD = userInputD.strip()

        # TODO

        for card in TradingCardManager.cardList:
            if userInputD == card.Defense():
                return card

        # Bad Case - We don't find the card
        print("Could not try card")
        return None

# ======================================================================================================================

@staticmethod
def amdendCards():

    # Find Card by Name
    print("Enter the name of the card you want to ammend: ")
    userInput = input("Name: ")
    userInput = userInput.strip()

    localCard = None
    for myCard in TradingCardManager.cardList:
        if myCard.getName() == userInput:
            localCard = myCard
            break # Early exit for loops

    # Change all details
    print("Enter New Details: ")
    newName = input("Name: ")

    newHP = None
    while newHP is None:
        try:
            newHP = int(input("New HP: "))
        except ValueError: # If input is not a number
            print("Not an integer")
            newHP = None


    localCard.setName(newName)
    localCard.setHp(newHP) # Sets new details onto the card




