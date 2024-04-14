class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})

    def view_tasks(self):
        if not self.tasks:
            print("No tasks in the to-do list.")
        else:
            print("Tasks:")
            for index, task in enumerate(self.tasks, start=1):
                print(f"{index}. [{task['completed'] and 'X' or ' '}] {task['task']}")

    def mark_task_completed(self, task_number):
        try:
            task_index = int(task_number) - 1
            self.tasks[task_index]["completed"] = True
            print("Task marked as completed.")
        except (IndexError, ValueError):
            print("Invalid task number.")

    def delete_task(self, task_number):
        try:
            task_index = int(task_number) - 1
            del self.tasks[task_index]
            print("Task deleted.")
        except (IndexError, ValueError):
            print("Invalid task number.")


def main():
    todo_list = ToDoList()
    while True:
        print("\n1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter the task: ")
            todo_list.add_task(task)
            print("Task added.")
        elif choice == "2":
            todo_list.view_tasks()
        elif choice == "3":
            task_number = input("Enter the task number to mark as completed: ")
            todo_list.mark_task_completed(task_number)
        elif choice == "4":
            task_number = input("Enter the task number to delete: ")
            todo_list.delete_task(task_number)
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
