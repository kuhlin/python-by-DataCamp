#You learned how to define class attributes and how to access them from class instances. 
#So what will happen if you try to assign another value to a class attribute when accessing it from an instance? 
#The answer is not as simple as you might think!

#The Player class from the previous exercise is pre-defined. 
#Recall that it has a position instance attribute, and MAX_SPEED and MAX_POSITION class attributes. 
#The initial value of MAX_SPEED is 3.

from Player import Player

# Instrucctions:

""" # Step1:

1.Create two Player objects p1 and p2.
 2.Print p1.MAX_SPEED and p2.MAX_SPEED.
 3.Assign 7 to p1.MAX_SPEED.
 4.Print p1.MAX_SPEED and p2.MAX_SPEED again.
 5.Print Player.MAX_SPEED.
 6.At the end of the class add a multiline comments explaining your solution
"""

""" # Step 2:

Even though MAX_SPEED is shared across instances, assigning 7 to p1.MAX_SPEED didn't change the value of MAX_SPEED in p2, or in the Player class.

So what happened? In fact, Python created a new instance attribute in p1, also called it MAX_SPEED, and assigned 7 to it, without touching the class attribute.

Now let's change the class attribute value for real.

    Modify the assignment to assign 7 to Player.MAX_SPEED instead.

"""


# Create Players p1 and p2
p1 = Player()
p2 = Player()

print("MAX_SPEED of p1 and p2 before assignment:")
# Print p1.MAX_SPEED and p2.MAX_SPEED
print(p1.MAX_SPEED)
print(p2.MAX_SPEED)
# Print Player.MAX_SPEED
print(Player.MAX_SPEED)

# Assign 7 to Player.MAX_SPEED
Player.MAX_SPEED = 7

print("MAX_SPEED of p1 and p2 after assignment:")
# Print p1.MAX_SPEED and p2.MAX_SPEED
print(p1.MAX_SPEED)
print(p2.MAX_SPEED)
# Print Player.MAX_SPEED
print(Player.MAX_SPEED)

"""
Explanation:
In Step 1, assigning 7 to p1.MAX_SPEED created a new instance attribute for p1, 
leaving the class attribute unchanged. This is why p2.MAX_SPEED remained 3, 
and Player.MAX_SPEED was still 3.

In Step 2, by assigning 7 to Player.MAX_SPEED, we changed the class attribute, 
which affects all instances that don't have their own instance attribute for MAX_SPEED.
Now p1.MAX_SPEED is still 7 (its instance attribute), p2.MAX_SPEED becomes 7 (from class), 
and Player.MAX_SPEED is 7.
"""

print("MAX_SPEED of Player:")
# Print Player.MAX_SPEED
print(Player.MAX_SPEED)

"""
When you assign a value to a class attribute through an instance (like p1.MAX_SPEED = 7), 
it creates a new instance attribute on that instance with the assigned value, 
rather than modifying the class attribute. 
This is why p1.MAX_SPEED becomes 7, but p2.MAX_SPEED remains 3 (the class attribute value), 
and Player.MAX_SPEED also remains 3.
"""