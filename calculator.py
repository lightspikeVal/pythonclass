# Calculator function
#Authorship and license agreement
import re
def authorship():
    """This module is built by Smart Bob, under license of Creative Commons 1.0 Native."""
    print("Authorship| This module is built by Smart Bob, under license of Creative Commons 1.0 Native.")

#Start of module
call="From calculator library|"
#Addition
def add(a,b):
    """Adds two numbers and returns the result.

    Parameters:
        a (int or float): The first number.
        b (int or float): The second number.

    Returns:
        int or float: The sum of a and b."""
    return a+b

#Subtract function
def subtract(a,b):
    """Subtracts two numbers and returns the result.

    Parameters:
        a (int or float): The first number.
        b (int or float): The second number.

    Returns:
        int or float: The subtraction of a and b."""
    return a-b

#Multipy function
def multi(a,b):
    """Multiplies two numbers and returns the result.

    Parameters:
        a (int or float): The first number.
        b (int or float): The second number.

    Returns:
        int or float: The multiplication of a and b."""
    return a*b

#Division function
def divide(a,b):
    """Divides two numbers and returns the result.

    Parameters:
        a (int or float): The first number.
        b (int or float): The second number.

    Returns:
        int or float: The division of a and b."""
    if b==0:
        raise ValueError("Unable to divide by zero. Infinity calculation error")
    return a/b

#Division Integer Only Function
def divint(a,b):
    """Divide two numbers and returns interger only result.

    Parameters:
        a (int or float): The first number.
        b (int or float): The second number.

    Returns:
        int or float: The division(int) of a and b."""
    if b==0:
        raise ValueError("Unable to divide by zero. Infinity calculation error")
    return a//b

#Power function
def pwr(a,b):
    """Power up two numbers and returns the result.

    Parameters:
        a (int or float): The first number.
        b (int or float): The second number.

    Returns:
        int or float: a to the power b."""
    return a**b
#None related to calculator module
def strint(a):
    """Change integer to string if possible

    Parameters:
        a (str) Any string in number

    Returns:
        int or float: The conversion is a."""
    if re.search("[0-9]",a):
        a=int(a)
        return a
    else:
        print(call, "Non convertable string, str is unknown, must be a integer")

def display(a,b,c,d):
    """For use in calculator style printing
    ------------------------------------------
    Parameters:
        a= First number from your input field
        b= Second number from your input field
        c= Any function from this library
        d = Operator type (+,-,*,/)
        -------
        Returns:
            Calculator style: int/float (+,-,*,/) int/float (=) int/float"""
    style= f"{a} {d} {b} = {c}"
    return style
    
#---------------End of library-----------------#
