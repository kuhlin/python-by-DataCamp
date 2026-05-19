""" Context:
The purpose of child classes -- or sub-classes, as they are usually called - is to customize and extend functionality of the parent class.

Recall the Employee class from earlier in the course. In most organizations, managers enjoy more privileges and more responsibilities than a regular employee. 
So it would make sense to introduce a Manager class that has more functionality than Employee.

But a Manager is still an employee, so the Manager class should be inherited from the Employee class.
int() will convert a string into a number, e.g. int("2019") is 2019 .

Note: For each step, at the end of the class add a multiline comments explaining your solution
"""

# Instructions: 

""" Step 1:
- Add an empty Manager class that is inherited from Employee.
- Create an object mng of the Manager class with the name Debbie Lashko and salary 86500.
- Print the name of mng.
"""

""" Step 2:
- Remove the pass statement and add a display() method to the Manager class that just prints the string "Manager" followed by the full name, e.g. "Manager Katie Flatcher"
- Call the .display()method from the mnginstance.
"""


class Employee:
  MIN_SALARY = 30000    

  def __init__(self, name, salary=MIN_SALARY):
      self.name = name
      if salary >= Employee.MIN_SALARY:
        self.salary = salary
      else:
        self.salary = Employee.MIN_SALARY
        
  def give_raise(self, amount):
      self.salary += amount      
        
# Step1: Define a new class Manager inheriting from Employee
# Step2: MODIFY Manager class and add a display method
class Manager(Employee):
    def display(self):
        print(f"Manager: {self.name}")

"""
Explanation for Step 1:
The Manager class inherits from Employee, allowing it to use all methods and attributes of Employee.
Since it's empty (using pass), it behaves exactly like Employee but can be extended later.
"""

# Define a Manager object
mng = Manager("Debbie Lashko", 86500)

# Print mng's name
# print(mng.name)

# Call mng.display()
mng.display()

"""Explanation for Step 2:
The display method in the Manager class prints a formatted string indicating the role and name of the manager.
"""