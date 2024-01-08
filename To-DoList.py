import heapq

class ToDoList:
    def __init__(self):
        self.tasks = []
        self.completed_tasks = []

    def add_task(self, task, priority=1):
        heapq.heappush(self.tasks, (priority, task))
        print(f'Task "{task}" added successfully with priority {priority}.')

    def view_tasks(self):
        if not self.tasks:
            print('No tasks available.')
        else:
            print('Tasks:')
            for index, (priority, task) in enumerate(self.tasks, start=1):
                print(f'{index}. {task} - Priority: {priority}')

    def mark_completed(self):
        if not self.tasks:
            print('No tasks available to mark as completed.')
        else:
            _, completed_task = heapq.heappop(self.tasks)
            self.completed_tasks.append(completed_task)
            print(f'Task "{completed_task}" marked as completed.')

    def view_completed_tasks(self):
        if not self.completed_tasks:
            print('No completed tasks.')
        else:
            print('Completed Tasks:')
            for index, task in enumerate(self.completed_tasks, start=1):
                print(f'{index}. {task}')

def main():
    todo_list = ToDoList()

    while True:
        print('\n1. Add Task\n2. View Tasks\n3. Mark Completed\n4. View Completed Tasks\n5. Quit')
        choice = input('Enter your choice (1/2/3/4/5): ')

        if choice == '1':
            task = input('Enter the task: ')
            priority = int(input('Enter the priority value: '))
            todo_list.add_task(task, priority)
        elif choice == '2':
            todo_list.view_tasks()
        elif choice == '3':
            todo_list.mark_completed()
        elif choice == '4':
            todo_list.view_completed_tasks()
        elif choice == '5':
            print('Exiting program. Goodbye!')
            break
        else:
            print('Invalid choice. Please enter a valid option.')

if __name__ == "__main__":
    main()
