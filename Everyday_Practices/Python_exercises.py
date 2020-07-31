"""
Given three integers, in which two are 
equal to each other and the third one is different. 
Print the order number of this different one - 1, 2 or 3.
"""

num1 = int(input())
num2 = int(input())
num3 = int(input())

if num1 == num2:
    print (3)
elif num1 == num3:
    print (2)
elif num2 == num3:
    print (1)
elif num1 == num2 and num1==num3:
    print('plz reinput')
elif num1 != num2 and num1 != num3 and num2 != num3:
    print ('plz reinput')
