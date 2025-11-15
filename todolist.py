#To Do List Application

#Import necessary libraries
import datetime
import random


#Task Options 
TypeTask = [
    'Sports',
    'Study',
    'Shopping',
    'Work',
    'Others'
]

Create_Your_Own_Task = 'Create My Own Task Type'

#Phylosofiucal Quotes
quotes = [
    "The secret of getting ahead is getting started.",
    "It's not whether you get knocked down, it's whether you get up.",
    "The harder you work for something, the greater you'll feel when you achieve it.",
    "Don't watch the clock; do what it does. Keep going.",
    "Success is not in what you have, but who you are."
]


#Class to manage
class ToDoList:

    #Initialize the to-do list
    def __init__(self):
        self.tasks = []

    #Add a new task
    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})

    #Remove a task
    def remove_task(self, task):
        self.tasks = [t for t in self.tasks if t["task"] != task]

    #Mark a task as completed
    def mark_completed(self, task):
        for t in self.tasks:
            if t["task"] == task:
                t["completed"] = True
                break

    #Mask a task as not completed
    def marj_not_completed(self, task):
        for t in self.tasks: 
            if t['task'] == task:
                t['completed'] = False
                break

    #Get all tasks
    def get_tasks(self):
        return self.tasks

TodoListApp = ToDoList()

user_input = ""
while user_input != "exit":
    print("\nTo-Do List Application")
    print("1. Add Task")
    print('2. See my tasks')
    print('3. See my completed tasks')
    print('4. See my not completed tasks')
    
    user_input = input("Choose an option: ")

    if user_input == "1":
        type_choice = input(f"Choose task type {TypeTask} or type '{Create_Your_Own_Task}': ")
        task = input("Enter the task: ")
        TodoListApp.add_task(f"[{type_choice}] {task}")
        print(f"Task '{task}' added under type '{type_choice}'.\n")

        #Motivational Quote with italic style and color red 
        print("Here's a motivational quote for you:")
        quote = random.choice(quotes)
        print(f"\033[3;31m{quote}\033[0m")



    elif user_input == "2":
        tasks = TodoListApp.get_tasks()
        print("All Tasks:")
        for t in tasks:
            status = "Completed" if t["completed"] else "Not Completed"
            print(f"- {t['task']} [{status}]")
            print("\n")
            print('--------------------------------------')
            print('Chose an option:')
            print('1. Would you like to mark any task as completed or not completed?')
            print('2. Delete a task')
            choice = input().lower()
            if choice == '1':
                update_task = input("Enter the task you want to update: ")
                mark_choice = input("Type 'complete' to mark as completed or 'not complete' to mark as not completed: ")
                if mark_choice == 'complete':
                    TodoListApp.mark_completed(update_task)
                    print(f"Task '{update_task}' marked as completed.")
                elif mark_choice == 'not complete':
                    TodoListApp.marj_not_completed(update_task)
                    print(f"Task '{update_task}' marked as not completed.")
            print('--------------------------------------')

            if choice == '2':
                delete_task = input(f'Select the task you want to delete:{tasks} ')
                TodoListApp.remove_task(delete_task)
                print(f"Task '{delete_task}' has been deleted.")
        

    
