from Packages.calculations.numericCalculations import calculations

def addList():
    mylist = [2,3,4,5]
    result = newCalc.addition(mylist)
    print("result is -->" + str(result))

if __name__ == "__main__":
    newCalc = calculations()
    addList()
