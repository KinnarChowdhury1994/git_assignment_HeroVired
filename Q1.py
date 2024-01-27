"""Summary
Q.1: You are part of a development team working on a Python application called "CalculatorPlus." The application provides basic arithmetic operations, such as addition, subtraction, multiplication, and division. Your task is to implement a new feature that adds support for calculating the square root of a number.
"""
'''
#! a. Create a repository name: git_assignment_HeroVired

        Link :- https://github.com/KinnarChowdhury1994/git_assignment_HeroVired

#! b. Create a ‘dev’ branch and add this code.

        Link :- https://github.com/KinnarChowdhury1994/git_assignment_HeroVired/tree/dev
'''

import math
class Calculator:
    #! Add Function
    def add(self, a, b):
        return a + b
    #! Substract Function
    def subtract(self, a, b):
        return a - b
    #! Multiply Function
    def multiply(self, a, b):
        return a * b
    #! Divide Function
    def divide(self, a, b):
        return a / b

    # TODO: Implement the following function to calculate the square root of a number.
    
    # def square_root(self, x):
    #   return math.sqrt(x)

    # You need to uncomment the above function and complete its implementation to add the square root feature.

if __name__ == "__main__":
    calculator = Calculator()
    num1 = 16
    num2 = 4
    print(f"{num1} + {num2} = {calculator.add(num1, num2)}")
    print(f"{num1} - {num2} = {calculator.subtract(num1, num2)}")
    print(f"{num1} * {num2} = {calculator.multiply(num1, num2)}")
    print(f"{num1} / {num2} = {calculator.divide(num1, num2)}")

    # TODO: Uncomment and test the square root feature.
    
    # num3 = 25
    # print(f"The square root of {num3} = {calculator.square_root(num3)}")

'''
c. Merge this branch with the main branch and make a release of version 1 of the ‘calculator plus app’.
'''
'''
d. Add any of your classmates as collaborators.

e. Implement a feature by creating a new branch called ‘feature/sqrt’.

f. Add the ‘sqrt’ code to it.

g. While you are working on this feature, imagine that one critical bug is reported in the main branch, and you need to switch back to the ‘dev’ branch, create fixes, and apply them while keeping your ‘feature/sqrt’ branch up-to-date. For this, you need to create

The bug fixation is in the divide function and the new function should be: def divide(self, a, b):

if b == 0:

raise ValueError("Cannot divide by zero.")

return a / b

h. After completing the feature implementation and ensuring that the application works correctly, create a pull request targeting the main branch.

i. Request a code review from a team member and make any necessary improvements based on the review feedback.

j. Once the code reviewer approves your pull request, merge the "feature/sqrt" branch into the ‘dev’ branch.

k. Finally, do the testing in the ‘dev’ branch itself and merge it into the ‘main’ branch and create a ‘version 2’ release.
'''
#! ===================================== EOD OF SUMMARY =========================================