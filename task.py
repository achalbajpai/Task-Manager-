import datetime

class Task:
    def __init__(self, description, due_date):
        self.description = description
        self.due_date = datetime.datetime.strptime(due_date, '%Y-%m-%d')
        self.completed = False

    def __str__(self):
        return f'{self.description} ({self.due_date})' + ("" if self.completed else " - Not Completed")

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, due_date):
        task = Task(description, due_date)
        self.tasks.append(task)

    def delete_task(self, index):
        del self.tasks[index]

    def complete_task(self, index):
        self.tasks[index].completed = True

    def list_tasks(self):
        return self.tasks

def main():
    task_manager = TaskManager()

    while True:
        print('1. Add task')
        print('2. Delete task')
        print('3. Complete task')
        print('4. List tasks')
        print('5. Quit')

        choice = input('Enter your choice: ')

        if choice == '1':
            description = input('Enter the task description: ')
            due_date = input('Enter the due date (YYYY-MM-DD): ')
            task_manager.add_task(description, due_date)

        elif choice == '2':
            index = int(input('Enter the task index:'))
            task_manager.delete_task(index)

        elif choice == '3':
            index = int(input('Enter the task index:'))
            task_manager.complete_task(index)

        elif choice == '4':
            tasks = task_manager.list_tasks()
            for i, task in enumerate(tasks):
                print(f'{i}. {task}')

        elif choice == '5':
            break

        else:
            print('Invalid choice')

if __name__ == "__main__":
    main()
