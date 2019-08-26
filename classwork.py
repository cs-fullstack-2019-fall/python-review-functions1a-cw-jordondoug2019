#Problem 1
def numberPrint(): # function to print numbers -25-20
    for x in range(-25,21,1): #for loop that defines that range of -25 to 20 w/increments of 1
        print(x) #displays numbers

numberPrint()

#Problem 2
def checkPassword(): #function that prints the 2nd function password
    print(password())
def password(): #function to check if passwords are equal
    userInput=input("Enter password  ") #input of password
    userInput2=input("Confirm password  ") #input to confirm password
    if userInput !=userInput2: #condition if input is not true, return false
        return ("False")
    if userInput==userInput2: #condition is input is true, return true
        return ("True")

checkPassword() #function that runs in terminal

#Problem 3
def oddorEven (): #function that tells if input is even or odd
    numberInput=int(input("Enter a number:  ")) #number input by user
    if numberInput%2==0: #conditonal using modulo to determine if number is even. if modulo is equal to 0, then it is even
        print("Even")
    else: #if modulo not equal to 0, prints odd
        print("odd")

oddorEven() #function runs in terminal

#Problem 4
def main(): #main function to be run in terminal
    prob4()

def prob4(): #second function that has no parameters
    noParam()

def noParam(): #third function that calls the greeting function
    print(greeting("howdy"))

def greeting(howdy): #fourth function that displays howdy world
    return(howdy+" "+ "world")

main()

#Problem 5
loopInput=input("Enter a word or q to quit:  ") #userInput
while(loopInput!="q"): #condition if user input is not equal to q
    loopInput=input("Enter a word or q to quit: ") #repeat prompt
    #Im finally getting loops 

#Challenge
def acceptNums(var1,var2):
    sum=var1+var2
    sub=var1-var2
    multi=var1*var2
    divide=var1/var2
    return sum,sub,multi,divide


var1= int(input("Enter a number:  "))
var2=int(input("Enter a number:  "))

# r1,r2,r3,r4=acceptNums(var1,var2) #seperate different returns

f" The sum of {var1} + {var2} is {sum} \n"
f"The difference of {var1} - {var2} is {sub} \n "
f" The product of {var1} * {var2} is {multi}\n "
f"The quotient of {var1} / {var2} = {divide} \n"\

r1,r2,r3,r4=acceptNums(var1,var2)