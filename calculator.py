def calculator():
    n1=float(input("enter the first number:"))
    n2=float(input("enter the second number:"))
             
             
    print("select operation:")
    print("1. Addition(+)")
    print("2. Subtarction(-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    operation=input("enter choice (1/2/3/4): ")
             
    if operation == '1':
        result=n1+n2
        print(f"The result of {n1}+{n2} is {result}")
    elif operation == '2':
        result=n1-n2
        print(f"The result of {n1}-{n2} is {result}")
    elif operation == '3':
        result=n1*n2
        print(f"The result of {n1}*{n2} is {result}")
    elif operation == '4':
        if n2!=0:
            result=n1/n2
            print(f"The result of {n1}/{n2} is {result}") 
        else: 
            print("Error! Division by zero.")
                     
    else:
        print("invalid input") 
if __name__ == "__main__": 
    calculator()             

                                 
                 
                     