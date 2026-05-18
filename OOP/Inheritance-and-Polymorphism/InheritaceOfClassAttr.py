""" Context:
In the beginning of this chapter, you learned about class attributes and methods that are shared among all the instances of a class. How do they work with inheritance?

In this exercise, you'll create subclasses of the Player class from the first lesson of the chapter, and explore the inheritance of class attributes and methods.

The Player class has been defined for you. Recall that the Player class had two class-level attributes: MAX_POSITION and MAX_SPEED, with default values 10 and 3.

Note: For each step, at the end of the class add a multiline comments explaining your solution
"""

class Player:
    MAX_POSITION = 10
    MAX_SPEED = 3
    
    def __init__(self, position=0):
        self.position = position

# Instructions: 

""" Step 1:
- Create a class Racer inherited from Player,
- Assign 5 to MAX_SPEED in the body of the class.
- Create a Player object p and a Racer object r (no arguments needed for the constructor).
"""



# Create a Racer class and set MAX_SPEED to 5
class Racer(Player):
    MAX_SPEED = 5

"""
Explanation for Step 1:
The Racer class inherits from Player and overrides the MAX_SPEED class attribute to 5.
This means Racer instances will have MAX_SPEED = 5, while Player instances keep MAX_SPEED = 3.
MAX_POSITION is inherited as 10 for both.
"""
 
# Create a Player and a Racer objects
p = Player()
r = Racer()

print("p.MAX_SPEED = ", p.MAX_SPEED)
print("r.MAX_SPEED = ", r.MAX_SPEED)

print("p.MAX_POSITION = ", p.MAX_POSITION)
print("r.MAX_POSITION = ", r.MAX_POSITION)