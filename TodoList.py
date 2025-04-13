class TodoList:
    def __init__(self, name, done):
        self.name = name
        self.done = done

    def display(self):
        return f"Task: {self.name}, Completed: {self.done}"


# Global list to store TodoList objects
todolists = []


def create_task():
    name = input("Enter your task: ")
    done = input("Is it complete? (yes/no): ")
    task = TodoList(name, done)
    todolists.append(task)
    print("✅ Task added successfully!")


def view_tasks():
    if not todolists:
        print("📭 No tasks found!")
    else:
        for task in todolists:
            print(task.display())


def main():
    while True:
        print("\n=== To-Do App ===")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Exit")

        option = input("Choose an option (1/2/3): ")

        if option == "1":
            create_task()
        elif option == "2":
            view_tasks()
        elif option == "3":
            print("👋 Goodbye!")
            break
        else:
            print("⚠️ Invalid option. Please try again.")


main()
