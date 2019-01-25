from array import *
import os, sys

"""
This is a docstring tutorials!
"""

myInt = 9

myFloat = 5.8

GHC = 2

myString = 'cisco'

stringLiteral = 'network programming and linux'

myList = ['macintosh', 'processor', 'cpu', 'ram', 'hdd', 'video', 'batt']

myTuple = (1, 4, 'IOS', 'NX-OS')

mySet = {3, 5, 10}

myDict = {'make': 'Apple','' 
          'model': 'Macbook',
          'protocol': 'OSPF'
          }

# def greet(*names):
#     """This function greets all
#        the person in the names tuple."""
#     # names is a tuple with arguments
#     for name in names:
#         print("Hello", name)

# greet("Monica","Luke","Steve","John")

# myList2 = myList.copy()
# print(myList2)
#
# for names in myList:
#     print(names)
#
# import fractions
#
# # Output: 3/2
# print(fractions.Fraction(1.5))

# for i in range(4):
#     for j in range(4):
#         print('#', end='')
#     print()

# print all Exception error
# print(locals()['__builtins__'])


# class Error(Exception):
#     """" Base class for my custom Exception """
#     pass
#
#
# arr = array('i',[])
#
# try:
#     number = int(input('Enter length of your array: '))
#
#     for i in range(number):
#         user_input = int(input('Now enter integer number: '))
#         arr.append(user_input)
#     print('\nTotal Array is: ',arr)
#
# except AttributeError as e:
#     print('Please import the proper array module', e)
#
# except (ValueError, AttributeError):
#     print('\nPlease enter Integer number: Process Aborted')
#
# finally:
#     print('\n.........')
#
#

# OS = os.rmdir('/Users/apple/testDirectory')
#
# print(OS)
# print(os.listdir())


with open('text.txt', mode='r+', encoding='utf-8') as f:
    print(f.read())
    f.write('\nPlease make sure you check out cisco"s Devnet website ')
    print(f.read())


