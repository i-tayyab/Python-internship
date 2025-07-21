import argparse
import json
import os
from colorama import Fore, Style

TASKS_FILE = "tasks.json"

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as f:
        json.dump(tasks, f)

def add_task(task):
    tasks = load_tasks()
    tasks.append({"task": task})
    save_tasks(tasks)
    print(Fore.GREEN + "Task added!" + Style.RESET_ALL)

def view_tasks():
    tasks = load_tasks()
    if not tasks:
        print(Fore.YELLOW + "No tasks found." + Style.RESET_ALL)
    for i, t in enumerate(tasks, 1):
        print(f"{i}. {t['task']}")

def delete_task(index):
    tasks = load_tasks()
    if 0 <= index - 1 < len(tasks):
        removed = tasks.pop(index - 1)
        save_tasks(tasks)
        print(Fore.RED + f"Deleted: {removed['task']}" + Style.RESET_ALL)
    else:
        print("Invalid task number.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simple CLI To-Do List Manager")
    parser.add_argument("command", choices=["add", "view", "delete"])
    parser.add_argument("arg", nargs='?', help="Task or task number")

    args = parser.parse_args()

    if args.command == "add" and args.arg:
        add_task(args.arg)
    elif args.command == "view":
        view_tasks()
    elif args.command == "delete" and args.arg:
        try:
            delete_task(int(args.arg))
        except ValueError:
            print("Provide a valid task number.")
    else:
        parser.print_help()
