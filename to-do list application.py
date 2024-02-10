class ToDoListApp:
    def __init__(self):
        self.tasks = []

    def run(self):
        print("Welcome to the To-Do List App!")

        while True:
            print("\n1. Add Task")
            print("2. Remove Task")
            print("3. Clear All Tasks")
            print("4. View Tasks")
            print("5. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                self.add_task()
            elif choice == '2':
                self.remove_task()
            elif choice == '3':
                self.clear_tasks()
            elif choice == '4':
                self.view_tasks()
            elif choice == '5':
                print("Exiting the app. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

    def add_task(self):
        task = input("Enter the task: ")
        if task:
            self.tasks.append(task)
            print("Task added successfully.")

    def remove_task(self):
        if self.tasks:
            print("Tasks:")
            for i, task in enumerate(self.tasks):
                print(f"{i + 1}. {task}")
            index = int(input("Enter the index of the task to remove: ")) - 1
            if 0 <= index < len(self.tasks):
                self.tasks.pop(index)
                print("Task removed successfully.")
            else:
                print("Invalid index.")
        else:
            print("No tasks to remove.")

    def clear_tasks(self):
        self.tasks = []
        print("All tasks cleared.")

    def view_tasks(self):
        if self.tasks:
            print("\nTasks:")
            for i, task in enumerate(self.tasks):
                print(f"{i + 1}. {task}")
        else:
            print("No tasks available.")

def main():
    app = ToDoListApp()
    app.run()

if __name__ == "__main__":
    main()
