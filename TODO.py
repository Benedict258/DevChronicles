import sys

# Initialize the file name to store tasks
file_name = "todo.txt"

# Function to load tasks from a file
def load_tasks():
    try:
        with open(file_name, "r") as file:
            tasks = file.readlines()
        # Remove any extra newline characters
        return [task.strip() for task in tasks]
    except FileNotFoundError:
        # If the file doesn't exist, return an empty list
        return []

# Function to save tasks to a file
def save_tasks():
    with open(file_name, "w") as file:
        for task in to_do:
            file.write(task + "\n")

# Load the to-do list from the file when the program starts
to_do = load_tasks()

# Function to display the menu of options
def operation():
    print("Welcome To your TODO list!!!\n")
    # Shows the user available actions: add, view, delete tasks, or exit.
    operation = input("1.VIEW\n 2.ADD\n 3.DEL\n 4.EXIT\n")

    if operation == "1":
        display_tasks()
    elif operation == "2":
        add_task()
    elif operation == "3":
        del_task()
    elif operation == "4":
        print("Exiting the program. Goodbye!")
        sys.exit()  # Exit the program
    else:
        print("Invalid choice, please select a valid option.")

# Function to display the list of tasks
def display_tasks():
    # Check if the to-do list is empty
    if not to_do:
        print("Your to-do list is empty!")
    else:
        print("\nHere are your tasks:")
        # Enumerate through the list to display tasks with numbers
        for index, task in enumerate(to_do, start=1):
            print(f"{index}. {task}")

# Function to add a task to the list
def add_task():
    task = input("Enter a task: ")
    to_do.append(task)  # Append each task to the list
    save_tasks()  # Save the updated list to the file

# Function to delete a task from the list
def del_task():
    # Check if the to-do list is empty
    display_tasks()
    # Ask the user for the task number to delete
    try:
        task_number = int(input("\nEnter the number of the task to delete: "))
        if 1 <= task_number <= len(to_do):
            # Delete the selected task
            deleted_task = to_do.pop(task_number - 1)
            print(f"Task '{deleted_task}' has been deleted.")
            save_tasks()  # Save the updated list to the file
        else:
            print("Invalid task number. Please try again.")
    except ValueError:
        print("Invalid input! Please enter a number.")

# Function to ask for another operation
def extra_op():
    op_enquiry = input("Would you like to make another operation [Y/N]? ")
    if op_enquiry == 'Y' or op_enquiry == 'y':
        operation()  # Run the operation again
    else:
        print("Exiting the program. Goodbye!")
        sys.exit()  # Exit the program

# Main loop of the program
while True:
    operation()
    extra_op()
