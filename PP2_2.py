'''
    Practice Questions: If and Else
    Author: Johnny Zhao
    Date Created: October 15, 2024
    Date Last Modified: October 16, 2024
'''

def q1(): 
  numQ1 = (int(input("Input an integer: "))) #asking the user to input an integeter, turning their result into a integer datatype
  if numQ1 == 5: #checking wether if the number is equal to 5, if it is, then
    print("The number is Five") #outputting "The number is Five"
  else: #if the number is not five, then
    print("The number is not Five") #outputting "The number is not Five"
    
def q2():
  numQ2 = (float(input("Input a number: "))) #asking the user to input a number, turning their result into a float datatype
  if numQ2 > 0: #checking wether if their number is greater than 0, if it is, then
    print("Positive") #outputting "Positive"
  else: #if not, then
    print("Negative") #outputting "Negative"

def q3(): 
  numQ3 = (int(input("Input an integer: "))) #asking the user to input a integer, turning their result into a integer datatype
  if numQ3 % 2 == 0: #dividing the number by two and checking its remainder to see if the number is even or odd, if even, then
    print("Even") #outputting "Even"
  else: #if not, then
    print("Odd") #outputting "Odd"

def q4(): 
  wordQ4 = (str(input('Type "Hello": '))) #asking the user to type Hello, turning their result into a string datatype
  if wordQ4 == "Hello": #checking wether if their word is "Hello", if it is, then
    print("The word is Hello") #outputting "The word is Hello"
  else: #if not, then
    print("The word is not Hello") #outputting "The word is not Hello"

#Do not alter the following code
#Comment out the following code when running your tests

#q1()
#q2()
#q3()
#q4()