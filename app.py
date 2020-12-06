#fucntion with the input and the operators
def main(num1=None, num2=None, ope=None):

    result = None

    try:
        num1 = float(input("Enter your fist number: "))
        num2 = float(input("Enter your second number: "))
        ope = input("Enter the operator: ")

    except ValueError:
        print("Error in your input number: {} or {}. "
              "Check if the inserted objects are a number.".format(num1, num2))
        exit()
        
    if ope == "+":
        result = (num1 + num2)
    elif ope == "-":
        result = (num1 - num2)
    elif ope == "*":
        result = (num1 * num2)
    elif ope == "/":
        result = (num1 / num2)
    else:
        print("Error in your input operator: {}. Make sure it's an operator.".format(ope))
        exit()
    return result


print(main())



def main(circum=None, diame=None):

    result = None

    try: 
        circum = float(input("Enter the circumference:  "))
        diame = float(input("Enter your diameter: "))

    except ValueError:
        print("Error in your input number: {}, {}. Make sure if they are number.".format(circum, diame))
        
    result = circum / diame

    return result



while True:
    
    quest = input("If you want calculate the pi greek, (Type yes, otherwise no): ")
    
    if quest == "no":
        print("See you soon!")
        exit()
    
    elif quest == "yes":
        print("Here your result:" ,main())
        
    break



