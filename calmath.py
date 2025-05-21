# Calculator function
#Authorship and license agreement
import re
import math
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
def sqrt(a):
    """Find Square root from fiven number
    Parameters:
        A= Any integer or float
    Return:
        Square root of the number."""
    return math.sqrt(a)
def pi():
    return math.pi

def circle(a,b):
    """Find the area of the circle.
        Rounded up to 3.14.
    Parameters:
        a = Radius of a circle  (int/float)
        b= Precise 'pi' or rounded (P for precise, A for default)
    Return:
        The area of the circle"""
    if b.lower()=='p':
        return math.pi*a*a
    else:
        return 3.14*a*a

def rec(a,b):
    """Accepts two int/float & returns the area of a rectangle
    Parameters:
        a= Length (int/float)
        b= Width(int/float)
    Returns:
        Returns the area of a rectangle a*b"""
    return a*b

def tri(a,b):
    """Accepts two int/float % retuns the area of a triangle
    Parameters:
        a= base of a triangle (int/float)
        b= height of a triangle (int/float)
    Process:
        Formula: 1/2 * base * height
    Return:
        Returns the area of the triangle."""
    return 0.5*a*b

def volume(a,b):
    """Convert the volume in any type
    Parameters:
        a = The original volume you want to convert
        b = The type of volume you want to convert to.
            You HAVE to write in single or double quote
            Write like this 'l-ml','ml-l', and so on.
            """
    if b=="l-ml":
        return a*1000
    elif b=='ml-l':
        return a/1000
    elif b=='l-gal':
        return a/3.785
    elif b=='gal-l':
        return a*3.785
    else:
        return "Invalid Conversion!"
    
#Additional Variables
pivalue=3.14
#Documentation
# -> https://squarepy.framer.wiki/libraries/calmath#doc
# -> https://awakentech.framer.wiki/sign-up
#   For more libraries like this:
#       https://squarepy.framer.wiki/libraries/viacalmath
#---------------End of library-----------------#
