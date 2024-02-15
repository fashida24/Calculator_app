#calculator app
#This is a basic calculator app

#ADDITION
def add(num1, num2):
    addition= num1+num2
    return addition

#SUBTRACTION
def subtract(num1, num2):
    subtraction= num1-num2
    return subtraction

#MULTIPLICATION
def multiply(num1, num2):
    multiplication= num1*num2
    return multiplication

#DIVISION
def divide(num1, num2):
    if num2== 0:
       print ("error")
    else:
     division= num1/num2    
     return division

def main():   #This runs the calculator app
    while True:
        ans=input(" Do you want to carry out an arithmetic operation? y or n ")
        if ans == "y":
            print("Choose an operation ")
            print("1. add")
            print("2. Subtract")
            print("3. Multiply")
            print("4. Divide")
            pick= input("Pick a choice between 1-4 ")

            if pick== "1":
              num1=float(input("Enter a number: "))
              num2=float(input("Enter another number: "))
              result=add(num1, num2)
              print("Your result is " + str(result))
            elif pick== "2":
              num1=float(input("Enter a number: "))
              num2=float(input("Enter another number: "))
              result=subtract(num1, num2)
              print("Your result is " + str(result))
            elif pick== "3":
              num1=float(input("Enter a number: "))
              num2=float(input("Enter another number: "))
              result=multiply(num1, num2)
              print("Your result is " + str(result))
            elif pick== "4":
              num1=float(input("Enter a number: "))
              num2=float(input("Enter another number: "))
              result=divide(num1, num2)
              print("Your result is " + str(result))
            else:
              print("invalid!! pick between 1 and 4")
        elif ans== "n":
            print("Okay!")
            break
        else:
            print("No choice like that! please enter y or n ")
                
       
main()
  