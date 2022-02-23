import csv
from MyObjects.TradingCardManager import *
from MyObjects.TradingCard import *

class MyReader:

    @staticmethod
    def readInFiles(readPath):

        with open(readPath, newline= '') as csvfile:
            reader = csv.reader(csvfile, delimiter = ',') # Storing rows to vars in reader

            for row in reader:
                TradingCardManager.addCard(TradingCard(*row))


    @staticmethod
    def writeContentToFile(writePath):

        localCardList = TradingCardManager.getCardList()

        writeBuffer = ""
        for card in localCardList:
            writeBuffer += (str(card) + '\n')

        with open(writePath, 'w', encoding='UTF8') as csvfile:
            csvfile.write(writePath)




