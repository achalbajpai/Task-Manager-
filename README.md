# Task-Manager-
  

The project is a simple task manager implemented using Python programming language. It provides a command-line interface for users to manage their tasks by adding, deleting, viewing, and marking them as complete. The task manager consists of two classes, Task and Task Manager, to represent a single task and manage the list of tasks respectively. The main() function provides a menu of options for the user to perform different actions on the tasks. The program makes use of the datetime module to track the due dates of tasks and uses a data structure, such as a dictionary, to store the details of tasks. 

The task manager has the ability to save and load tasks to/from a file, enabling the persistence of tasks across sessions. The current implementation serves as a basic model with ample room for improvements and extensions, such as adding reminders and categorizing tasks based on type or priority.







The code is a simple task manager that allows users to add, delete, complete, and list tasks. It uses two classes, Task and TaskManager. The Task class represents a single task, with a description, due date, and completion status. The TaskManager class manages a list of tasks.

The code starts by creating a TaskManager object. Then, it enters a loop where the user can choose from a menu of options. The options are:

Add task
Delete task
Complete task
List tasks
Quit
The user enters their choice, and the code then executes the corresponding action. For example, if the user chooses to add a task, the code prompts the user for the task description and due date, and then creates a new Task object and adds it to the list of tasks.

The code also handles invalid choices gracefully. If the user enters an invalid choice, the code prints a message and prompts the user to enter a new choice.

The code is a good example of how to use classes in Python. It also shows how to create a simple user interface with a menu of options.
