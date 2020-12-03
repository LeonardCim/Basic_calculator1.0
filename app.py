#fucntion with the input and the operators
def main(argument1, argument2, ope):

    result = None

    try:
        argument1 = float(input("Enter your fist number: "))
        argument2 = float(input("Enter your second number: "))
        ope = input("Enter the operator: ")

    except ValueError:
        print("Error in your input number: {} or {}. "
              "Check if the inserted objects are a number.".format(argument1, argument2))
        exit()

    num1 = argument1
    num2 = argument2

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


print(main(argument1=None, argument2=None, ope=None))


