'''
This is a docstring tutorials!
'''

myInt = 9

myFloat = 5.8

GHC = 2

myString = 'cisco'

stringLiteral = 'network programming and linux'

myList = ['macintosh', 'processor', 'cpu', 'ram', 'hdd', 'video']

myTuple = (1, 4, 'IOS', 'NX-OS')

mySet = {3, 5, 10}

myDict = {'make': 'Apple','' 
          'model': 'Macbook',
          'protocol': 'OSPF'
          }


def greet(*names):
    """This function greets all
       the person in the names tuple."""
    # names is a tuple with arguments
    for name in names:
        print("Hello", name)


greet("Monica","Luke","Steve","John")