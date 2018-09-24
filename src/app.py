from accounts import login, add_account
from tasks import create_task, delete_task, delete_all_tasks, mark_as_finished, view_tasks


def loggedin_user():
    prompt = """
                (C)reate Task  
                (M)ark Task as Finished
                (V)iew Tasks
                (D)elete Task
                d(E)lete All Tasks
                (Q)uit

    Please Make your choice : """

    done = False
    while not done:
        chosen = False
        while not chosen:
            try:
                choice = input(prompt).strip()[0].lower()
            except(IOError, KeyboardInterrupt) :
                choice = 'q'
            if choice not in 'cmdveq':
                print("Wrong choice. Try again")
            else:
                chosen = True
        if choice == 'c':
            loggedin = False
            while not loggedin:
                try:
                    task = input("Please enter the task : ").strip()
                except(IOError, KeyboardInterrupt):
                    loggedin = True
                create = create_task(task)
                if create != "Successfully Created Todo task":
                    print(create)
                    print("Please Try again")
                else:
                    print(create)
                    loggedin = True
        if choice == 'm':
            loggedin = False
            while not loggedin:
                try:
                    id = input("Please enter the task id : ")
                    id = int(id)
                except(IOError, KeyboardInterrupt, Exception):
                    loggedin = True
                mark = mark_as_finished(id)
                if mark != "Successfully Marked task {} as Finished".format(id):
                    print(mark)
                    print("Please Try again")
                else:
                    print(mark)
                    loggedin = True
        if choice == 'd':
            loggedin = False
            while not loggedin:
                try:
                    id = input("Please enter the task id : ")
                    id = int(id)
                except(IOError, KeyboardInterrupt, Exception):
                    loggedin = True
                delete = delete_task(id)
                if delete != "Task Number {} successfuly deleted".format(id):
                    print(delete)
                    print("Please Try again")
                else:
                    print(delete)
                    loggedin = True
        if choice == 'e': 
            delete_all_tasks()
        if choice == 'q':
            done = True
        if choice == 'v':
            view = view_tasks()
            print(view)

def register():
    loggedin = False
    while not loggedin:
        try:
            name = input("Name : ")
            email = input("Email : ")
            password = input("Password : ")
        except(KeyboardInterrupt, IOError):
            loggedin = True
        log = add_account(name, email, password)
        if log != "Successfully Added an account":
            print(log)
            print("Please Try again")
        else:
            print(log)
            loggedin_user()
            loggedin = True

def signin():
    loggedin = False
    while not loggedin:
        try:
            email = input("Email : ")
            password = input("Password : ")
        except(KeyboardInterrupt, IOError):
            loggedin = True
        log = login(email, password)
        if log != "You have successfully logged in":
            print(log)
            p = input("Do you want to create an account? Y/N : ").strip()[0].lower()
            if p == 'y':
                register()
                break
        else:
            print(log)
            loggedin_user()
            loggedin = True 

def menu():
    prompt = """Login if you have a Todo account. Register if you don't
    
        (L)ogin
        (R)egister
        (Q)uit

    Enter your choice:"""
    done = False
    while not done:
        chosen = False
        while not chosen:
            try:
                choice = input(prompt).strip()[0].lower()
            except(IOError, KeyboardInterrupt) :
                choice = 'q'
            if choice not in 'lrq':
                print("Wrong choice. Try again")
            else:
                chosen = True
        if choice == 'l':
                signin()
        if choice == 'r':
            register()
        if choice == 'q':
            done = True

if __name__ =='__main__':
    menu()
            