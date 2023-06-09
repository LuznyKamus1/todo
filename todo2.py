import sys
import json

file = open("/home/kamus/Langs/python/todo/list.json", "r+", encoding='utf-8')
contents = json.load(file)

def rm_todo():
    try: del contents["todo"][sys.argv[3]]
    except: print("the todo with that name doesnt exist")
def rm_task():
    try: del contents["todo"][sys.argv[3]]["tasks"][sys.argv[4]]
    except: print("the todo/task with that name doesnt exist")

#add a new todo to list.json
def new_todo():
    #ask for the title and check if its main if true ask again
    x=input("title of new todo: ")
    while x=="main" : x=input("title cannot be 'main', please input another title: ")
    
    try:
        y=contents["todo"][x]
        print("there is a todo with the same name!")
    except:
        #declare some objects?
        contents["todo"].update({x:{}})
        contents["todo"][x].update({"desc":input("description of new todo: ")})
        contents["todo"][x].update({"tasks":{}})
    
    #add tasks
    match input("do you want to add tasks now (y/n)? "):
        case "y":
            for y in range(int(input("how many tasks do you want to add? "))):
                new_task(x)
        case _:
            print("not adding any tasks...")
    print("new todo succesfully added!")

#add a new task
def new_task(x):
    try:
        contents["todo"][x]["tasks"].update({input("title of new task: "):False})
    except: print("something went wrong! (most likely it was a wrong title!)")

#change main todo
def new_main():
    contents["main"] = input("title of the new main: ")

#read all task from todo
def read_tasks():
    try:
        for x in contents["todo"][sys.argv[3]]["tasks"]:
            match contents["todo"][sys.argv[3]]["tasks"][x]:
                case True: print("task "+x+" done")
                case False: print("task "+x+" not done")
    except:
        print("something went wrong! (most likely you didnt specify the todo name or the todo with this name doesnt exist!)")

def read_task_percent():
    try:
        y=0
        for x in contents["todo"][sys.argv[3]]["tasks"]:
            match contents["todo"][sys.argv[3]]["tasks"][x]:
                case True: y+=1
        print(str(len(contents["todo"][sys.argv[3]]["tasks"])/y*10)+"%")
    except: print("something went wrong! (most likely you didnt specify the todo name or the todo with this name doesnt exist!)")

#read the description of todo
def read_desc():
    try:
        match sys.argv[3]:
            case "main": print(contents["todo"][contents["main"]]["desc"])
            case _: print(contents["todo"][sys.argv[3]]["desc"])
    except: print("something went wrong! (most likely you didnt specify the todo name or the todo with this name doesnt exits!)")

def read_todos():
    for x in contents["todo"]: print(x)

def read_main():
    print(contents["main"])

def done_task():
    contents["todo"][sys.argv[3]]["tasks"][sys.argv[4]]=True

def help():
    print("")

match sys.argv[1]:
    case "new":
        match sys.argv[2]:
            case "todo": new_todo()
            case "task": new_task(input("name of todo: "))
            case "main": new_main()
            case _: print("wrong subcommand!")
    case "remove":
        match sys.argv[2]:
            case "todo": rm_todo()
            case "task": rm_task()
            case _: print("wrong subcommand!")
    case "read":
        match sys.argv[2]:
            case "main": read_main()
            case "task_percent": read_task_percent()
            case "tasks": read_tasks()
            case "desc": read_desc()
            case "todos": read_todos()
            case _: print("wrong subcommand!")
    case "done":
        match sys.argv[2]:
            case "task": done_task()
            case _: print("wrong subcommand!")
    case "help":
        help()
    case _:
        print("wrong command!")

file.seek(0)
file.truncate()
json.dump(contents, file)
file.close()
