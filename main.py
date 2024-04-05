class Task:
    def __init__(self, description, due_date):
        self.description = description
        self.due_date = due_date
        self.status = False  # False означает, что задача не выполнена

    def mark_as_done(self):
        self.status = True

    def __str__(self):
        return f"{self.description} (до {self.due_date}) - {'Выполнено' if self.status else 'Не выполнено'}"


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, due_date):
        task = Task(description, due_date)
        self.tasks.append(task)
        print(f"Задача '{task.description}' добавлена.")

    def mark_task_done(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_as_done()
            print(f"Задача '{self.tasks[index].description}' отмечена как выполненная.")
        else:
            print("Неверный индекс задачи.")

    def list_pending_tasks(self):
        print("Текущие задачи:")
        for index, task in enumerate(self.tasks):
            if not task.status:
                print(f"{index}. {task}")

def main():
    task_manager = TaskManager()

    while True:
        print("\n1. Добавить задачу")
        print("2. Отметить задачу выполненной")
        print("3. Вывести список не выполненных задач")
        print("4. Выйти")
        choice = input("Выберите действие: ")

        if choice == '1':
            description = input("Введите описание задачи: ")
            due_date = input("Введите срок выполнения задачи (гггг-мм-дд): ")
            task_manager.add_task(description, due_date)
        elif choice == '2':
            index = int(input("Введите индекс задачи для отметки о выполнении: "))
            task_manager.mark_task_done(index)
        elif choice == '3':
            task_manager.list_pending_tasks()
        elif choice == '4':
            print("До свидания!")
            break
        else:
            print("Неправильный выбор, пожалуйста, введите число от 1 до 4.")

if __name__ == "__main__":
    main()