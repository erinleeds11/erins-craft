
#constants of beer cost in dollars
IPA_COST = 5.0
LAGER_COST = 4.5
STOUT_COST = 6.0
PILSNER_COST = 5.75

#Class definition for a single beer client
class BeerClient:
    #constructor initializes variables
    def __init__(self, name):
        self.clientName = name
        self.numIPA = 0
        self.numLager = 0
        self.numStout = 0
        self.numPilsner = 0
        self.address = ""

    #Running total for number of beers
    def addIPA(self, numIPA):
        self.numIPA += numIPA

    def addLager(self, numLager):
        self.numLager += numLager

    def addStout(self, numStout):
        self.numStout += numStout

    def addPilsner(self, numPilsner):
        self.numPilsner += numPilsner

    def addAddress(self, address):
        self.address += address

    def getAddress(self):
        return self.address

    #Returns total number of beers a customer ordered
    def getTotalBeerCount(self):
        return self.numStout + self.numIPA + self.numLager + self.numPilsner
    #Returns total cost of beer
    def getTotalBeerCost(self):
        return self.numIPA*IPA_COST + self.numPilsner*PILSNER_COST + self.numLager*LAGER_COST + self.numStout*STOUT_COST

#Main function creates an object and stores information about the client
def main():
    objList = [] #Creates a list of objects that will hold client info
    moreClients = "yes"
    while moreClients == "yes":
        print("Welcome to Erin's Craft! \nWe are a small business that sells unique craft beers!")
        client_name = input("What is your name?: ")
        print("")
        thisClient = BeerClient(client_name)
        if ageCheck(client_name) == True:
            showMenu()
            beerList(thisClient)
            print("The total number of beers is:  ",(thisClient.getTotalBeerCount()))
            print("")
            print("The price of the beers is: ", "$" + str(thisClient.getTotalBeerCost()))
            print("")
            address(thisClient)
            objList.append(thisClient) #adds client info to list
            moreClients = input("Are there more clients? (yes/no): ")
            print("")
        else:
            print("You are not of age.")
            print("Come back when you are!")
    # Prints out name, total cost, and address for each client
    print("Summary:")
    print("")
    print("Name            Total Cost ($)        Address ")
    print("************************************************")
    for obj in objList:
        print(obj.clientName, obj.getTotalBeerCost(), obj.getAddress(), sep = "            ")
    print("Thank you for ordering from Erin's Craft!")

#Prints beer menu with prices
def showMenu():
    print("      Craft Beer Menu")
    print("****************************")
    print("Juicy Hazy DIPA:      $5.00")
    print("Light Lager:          $4.50")
    print("Super Strong Stout:   $6.00")
    print("Ol' Pilsner:          $5.75")
    print("")

#Checks to see if user is above 21
def ageCheck(name):
    print("Hi", name+",", "we have to make sure you are over 21 years old.")
    print("")
    age = eval(input("How old are you?: "))
    print("")
    if age >= 21:
        return True
    else:
        return False

#Adds number of each beer to client information
def beerList(thisClient):
    num_IPA = int(input("How many Juicy Hazy DIPAs do you want?: "))
    thisClient.addIPA(num_IPA)
    print("")
    num_Lager = int(input("How many Light Lagers do you want?: "))
    thisClient.addLager(num_Lager)
    print("")
    num_Stout = int(input("How many Super Strong Stouts do you want?: "))
    thisClient.addStout(num_Stout)
    print("")
    num_Pilsner = int(input("How many Ol' Pilsners do you want?: "))
    thisClient.addPilsner(num_Pilsner)
    print("")

#Adds address to client information
def address(thisClient):
    address = input("What is the address you would like your beers to be shipped?: ")
    thisClient.addAddress(address)

#call to main
main()