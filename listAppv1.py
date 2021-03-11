"""
Program goals:
3. Pull the values stored at specific indexes
4. Convert input to INTS
5. Put all action in a while loop
6. Add an exit option

"""
myList = []

def mainProgram():
    #build our while loop here
       while True:
        myList = []
         print("Hello, there! Let's work with lists!")
         print("Please choose from the following options.  Type the number of the choice")
         choice = input("1. Add to a list, 2. Return a value in a list   ")
         if choice == "1":
             addToList()
         elif choice == "2":
             indexValues()
         elif choice == "3":
             break 
       
                    
def addToList():
    print("Adding to a list! Great choice!")
    newItem = input("Type an integer here!   ")
    myList.append(int(newItem))
    #we need to think about errors!

def indexValues():
    print("At what inbox position do you want to search?")
    indexPos = input("Type an index position here:   ")
    print (myList[int(indexPos)])



if_name_ == "__main__":
    mainProgram()
