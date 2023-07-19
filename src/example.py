# a python script to demonstrate coding mistakes
def Greet(name):
    msg="Hello " + name + "! How are you?" # Using a "+" operator for string concatenation
    return msg

def add(n1,n2):
  result=n1+n2 # Inconsistent indentation
    return result

def is_even(n):
    if n%2 == 0: # No space around the operator
        return true # Using "true" instead of "True"
    else
        return false # Missing colon, using "false" instead of "False"

print(Greet('John'))
print(add(3,5))
print(is_even(4))
