import math
# enter the required numbers
x1 = float(input("Enter x1:"))
y1 = float(input("Enter y1:"))
x2 = float(input("Enter x2:"))
y2 = float(input("Enter y2:"))
# calculate the final distance
distance = math.sqrt(math.pow(x2 - x1 , 2) + math.pow(y2 - y1 , 2))
# giving the user the distance between their two points
print("The distance between the two points is:", distance)


#Reflection:
""" 
Using a library is more is more practical than writing everything from scratch
because functions like sqrt() and pow() already exist and are
reliable. In this program, I didn't have to write my own square root logic
I just called math.sqrt() and math.pow() ajnd got the correct distance right away.
"""
