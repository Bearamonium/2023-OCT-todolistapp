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
    todo_name = input("Enter a todo that you want to remove: ")
    # copy all the contents of the csv into a new csv
    # while doign this, we constantly check for the condition
    # when we encounter ther todo to be removed, we don't copy that one
    # the final new todo will be written in the csv file
    todo_lists = []
    with open(file_name, "r") as f: 
        reader = csv.reader(f)
        for row in reader: 
            if (todo_name != row[0]): 
                todo_lists.append(row)
    with open(file_name, "w") as f: 
        writer = csv.writer(f)
        writer.writerows(todo_lists)

def mark_todo(file_name):
    print("Mark item as completed.")
    todo_name = input("Enter the todo name to mark as completed: ")
    todo_lists = []
    with open(file_name, "r") as f:
        reader = csv.reader(f)
        for row in reader: 
            if (todo_name != row[0]): 
                todo_lists.append(row)
            else: 
                todo_lists.append([row[0], "True"])
    with open(file_name, "w") as f: 
        writer = csv.writer(f)
        writer.writerows(todo_lists)

def view_todo(file_name):
    print("View TODO.")
    with open(file_name, "r") as f: 
        reader = csv.reader(f)
        reader.__next__()
        for row in reader: 
            if (row[1] == "True"):
                print(f"Todo {row[0]} is completed")
            else: 
                print(f"Todo {row[0]} is not completed")

