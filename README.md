# Graded Assignment on Git and GitHub for Course 2: Git and GitHub | DevOps B4
### Repository Name - 
[git_assignment_HeroVired](https://github.com/KinnarChowdhury1994/git_assignment_HeroVired "git_assignment_HeroVired")
###### Submitted by - Kinnar Chowdhury

### Timeline
```
    * Opened    : Friday, 19 January 2024, 12:00 AM
    * Due       : Saturday, 3 February 2024, 11:59 PM
    * Submitted : Saturday, 3 February 2024, 3:23 AM
```
### Collaborator
[Name](https://github.com/KinnarChowdhury1994/git_assignment_HeroVired "Collaborator")

### Marking Scheme & Submission Guideline:
###### Create a text file and add your GitHub repository link (the name of the GitHub repository should be: ‘git_assignment_HeroVired’ and it should be a private repository) into it and upload that file in the submission section in Vlearn.
```
a. Each question is mandatory to solve.

b. Question number 1 consists of 20 points in total where 18 points are for completing the task and 2 points are for helping at least one of your classmates in their GitHub repository by reviewing code.

c. Question number 2 consists of 10 points.

d. Question number 3 consists of 20 points in total where 18 points are for completing the task and 2 points are for helping at least one of your classmates in their GitHub repository by reviewing code.

e. Assignment related steps should be clearly mentioned in the README.md file of the GitHub repository with steps performed to complete each task.

f. Make the GitHub repository private and after the due submission date, make it public for the assignment to be corrected.

g. No commitment after the due date will be considered as part of the submission.
```
*--*
##### Q.1: You are part of a development team working on a Python application called "CalculatorPlus". The application provides basic arithmetic operations, such as addition, subtraction, multiplication, and division. Your task is to implement a new feature that adds support for calculating the square root of a number.

```python
import math

class Calculator:
    def add(self, a, b):
        return a + b
    def subtract(self, a, b):
        return a - b
    def multiply(self, a, b):
        return a * b
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
    print(f"{num1} - {num2} = {calculator.subtract(num1, num2)}") print(f"{num1} * {num2} = {calculator.multiply(num1, num2)}")
    print(f"{num1} / {num2} = {calculator.divide(num1, num2)}")

    # TODO: Uncomment and test the square root feature.
    # num3 = 25
    # print(f"The square root of {num3} = {calculator.square_root(num3)}")
```
```
a. Create a repository name: git_assignment_HeroVired

        - Link :- https://github.com/KinnarChowdhury1994/git_assignment_HeroVired
```
```
b. Create a ‘dev’ branch and add this code.

        - Link :- https://github.com/KinnarChowdhury1994/git_assignment_HeroVired/tree/dev
```
```
c. Merge this branch with the main branch and make a release of version 1 of the ‘calculator plus app’.

        - git checkout main
        - git merge dev
        - git push
```
```
d. Add any of your classmates as collaborators.

        - Added harshithuppar and Sumant-Mahto
```
```
e. Implement a feature by creating a new branch called ‘feature/sqrt’.

        - git branch feature/sqrt
```
```
f. Add the ‘sqrt’ code to it.

        - git checkout feature/sqrt
        - uncommented the square_root function and saved the file.
        - git add .
        - git commit -m "Message can be seen in the Github"
        - git push
```
```
g. While you are working on this feature, imagine that one critical bug is reported in the main branch, and you need to switch back to the ‘dev’ branch, create fixes, and apply them while keeping your ‘feature/sqrt’ branch up-to-date. For this, you need to create

The bug fixation is in the divide function and the new function should be: 

#   def divide(self, a, b):
#       if b == 0:
#           raise ValueError("Cannot divide by zero.")
#       return a / b

        - uncommented & save.
        - commit and push to main branch.
```
```
h. After completing the feature implementation and ensuring that the application works correctly, create a pull request targeting the main branch.
```
```
i. Request a code review from a team member and make any necessary improvements based on the review feedback.
        - code reviewed by Sumant-Mahto.
```
```
j. Once the code reviewer approves your pull request, merge the "feature/sqrt" branch into the ‘dev’ branch.
        - git checkout dev
        - git merge feature/sqrt
        - git push
```
```
k. Finally, do the testing in the ‘dev’ branch itself and merge it into the ‘main’ branch and create a ‘version 2’ release.
        - python Q1.py
        - git checkout main
        - git pull
        - git merge dev
        - git push
```
*** Answer:
```bash
$ python Q1.py           
16 + 4 = 20
16 - 4 = 12
16 * 4 = 64
16 / 4 = 4.0
The square root of 25 = 5.0
```
*--*
##### Q.2: For a project that deals with large binary files, integrate Git LFS (Large File Storage) to handle these files efficiently. Demonstrate how to add, commit, and push binary files to the repository, ensuring they are tracked by Git LFS correctly. Clone the repository on another machine to verify that the binary files are downloaded correctly.

```
In the repository ‘git_assignment_HeroVired’, create a branch ‘lfs’. Upload any large file whose size is over ‘200mb’ and try to push this file into the repository.
```
*** Answer:
```bash
$ git branch
$ git branch lfs
$ git checkout lfs
$ echo "First Install the git lfs in your prefered os. Reference - https://docs.github.com/en/repositories/working-with-files/managing-large-files/installing-git-large-file-storage"
$ git lfs install
$ git lfs track big_file_256mb.pdf
$ git add .gitattributes
$ git add big_file_256mb.pdf
$ git add Q2.txt
$ git commit -m "Git LFS integration in lfs branch"
```

*--*
##### Q.3: In this same GitHub repository, create a new branch ‘geometry-calculator’, we'll work on a simple Python program that calculates the area of a circle and the area of a rectangle. We'll use Git stash to switch between working on multiple features (calculating circle area and calculating rectangle area) without committing incomplete changes.

```python
import math

class GeometryCalculator:

    def calculate_circle_area(self, radius):
    return math.pi * radius ** 2

    def calculate_rectangle_area(self, length, width):
        return length * width

if __name__ == "__main__":
    calculator = GeometryCalculator()
    # TODO: Implement the feature to calculate the area of a circle
    radius = 5
    print (f"The area of the circle with radius {radius} = {calculator.calculate_circle_area(radius)}")

    # TODO: Implement the feature to calculate the area of a rectangle # length = 10
    # width = 6
    # print(f"The area of the rectangle with length {length} and width {width} = {calculator.calculate_rectangle_area(length, width)}")

'''
#! Workflow Steps:

a. Create a New Branch:
    - Create a new branch named "feature/circle-area" to work on the circle area feature

b. Stash Changes for Circle Area Feature:
    - Before committing the changes, stash them using git stash to save the incomplete feature implementation.
    - Verify that the working directory is clean

c. Create a New Branch for Rectangle Area Feature:
    - Create a new branch named "feature/rectangle-area" to work on the rectangle area

d. Stash Changes for Rectangle Area Feature:
    - Before committing the changes, stash them using git stash to save the incomplete feature implementation.
    - Verify that the working directory is clean

e. Switch Back to Circle Area Branch:
    - Switch back to the "feature/circle-area" branch to continue working on the circle area feature.
    - Retrieve the stashed changes
    - Complete the circle area feature implementation and save the changes.

f. Commit and Push Circle Area Feature:

g. Switch Back to Rectangle Area Branch:
    - Switch back to the "feature/rectangle-area" branch to continue working on the rectangle area feature.
    - Retrieve the stashed changes
    - Complete the rectangle area feature implementation and save the changes.
    
h. Commit and Push Rectangle Area Feature

i. Create Pull Requests:
    - Create a pull request to the ‘dev’ branch.

j. Review and Merge
    - Have another team member or reviewer review your pull requests.
    - After receiving approval, merge both pull requests into the main branch.

'''
```
*** Answer:
```bash
$ git branch
$ git branch feature/circle-area
$ git checkout feature/circle-area
$ git stash
$ git branch feature/rectangle-area
$ git checkout feature/rectangle-area
$ git stash list
$ git stash
$ git checkout feature/circle-area
$ git stash list
$ git stash pop 1
$ git add .
$ git commit -m "Stash changes retrieved and ready to push in feature/circle-area branch."
$ git push
$ git checkout feature/rectangle-area
$ git stash list
$ git stash pop 0
$ git add .
$ git commit -m "Stash changes retrieved and ready to push in feature/rectangle-area branch."
$ git checkout dev
$ git pull
$ git merge feature/circle-area
$ git push
$ git checkout feature/rectangle-area
$ git merge dev
$ git push
$ git checkout dev
$ git merge feature/rectangle-area
$ Resolved Conflict and pushed in dev branch.
$ git status
$ git checkout main
$ git pull
$ git merge dev
$ git push
```
*** Ootput
```bash
$ python Q3.py           
The area of the circle with radius 5 = 78.53981633974483
The area of the rectangle with length 10 and width 6 = 60
```

### Submission Instructions:

```
To submit your assignment, please follow these guidelines:

    - Ensure that your assignment is fully completed.
    - Push your code to a GitHub repository.
    - Share the repository link by including it in a text, Word, or PDF file format.

Submit the file/text containing the repository link via Vlearn.
```
