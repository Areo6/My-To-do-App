from src.validation import valid_task


todo_list = []

def view_tasks():
    """
    This method Displays the All the tasks i the Todo List
    """
    if len(todo_list) == 0:
        return "Empty list. There are no tasks yet"
    return todo_list

def create_task(task):
    """
    This function Creates todo task and appends it to the todo list
    """
    if valid_task(task) != "Valid":
        return valid_task(task)
    todo_task = [x for x in todo_list if x["task"] == task]
    if len(todo_task) != 0:
        return "Task already exist. Input a different task"
    id = len(todo_list) + 1
    todo_item = {
        "id": id,
        "task": task
    }
    todo_list.append(todo_item)
    return "Successfully Created Todo task"

def delete_task(id):
    """
    This function deletes the task given the task id
    """
    if len(todo_list) == 0:
        return "Empty Todo List. Nothing to delete"
    todo_item = [x for x in todo_list if x["id"] == id]
    if len(todo_item) == 0:
        return "{} does not exist in the todo list. Please enter an existing id".format(id)
    todo_list.remove(todo_item[0])
    i = 1
    for todo in todo_list:
        todo["id"] = i
        i += 1
    return "Task Number {} successfuly deleted".format(id)

def mark_as_finished(id):
    """
    This function append the string [finished] at the end of a task if finished
    """
    if len(todo_list) == 0:
        return "Empty Todo List. No tasks yet"
    todo_item = [x for x in todo_list if x["id"] == id]
    if len(todo_item) == 0:
        return "{} does not exist in the todo list. Please enter an existing id".format(id)
    todo_item = [x for x in todo_list if x["id"] == id]
    if "[Finished]" in todo_item[0]["task"]:
        return "This task was already finished"
    todo_item[0]["task"] += "[Finished]"
    return "Successfully Marked task {} as Finished".format(id)

def delete_all_tasks():
    """
    This function empties the Todo list
    """
    if len(todo_list) == 0:
        return "The Todo list is empty. There is no task Yet"
    
    i = len(todo_list)
    while i > 0:
        todo_list.remove(todo_list[i-1])
        i = len(todo_list)
    return "Successfully emptied Todo list"