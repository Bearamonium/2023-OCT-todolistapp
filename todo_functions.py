import csv

def add_todo(file_name):
    print("Add TODO item.")
    # Ask the title of the todo
    todo_name = input("Enter name of task for TODO list: ")
    # Insert that value in to the file - list.csv
    with open(file_name, "a") as f: 
        writer = csv.writer(f)
    # while insterting - title = user entered
                     # - completed = False
        writer.writerow([todo_name, "False"])
    

def remove_todo(file_name): 
    print("Remove TODO item.")

def mark_todo(file_name):
    print("Mark item as completed.")

def view_todo(file_name):
    print("View TODO.")

