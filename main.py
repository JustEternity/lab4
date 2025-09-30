import datetime

class TodoList:
    def __init__(self):
        self.tasks = {}
        self.next_id = 1

    def add_task(self, name, text):
        self.tasks[self.next_id] = {'date': datetime.datetime.now().strftime("%d-%m-%Y %H:%M"),'name': name, 'text': text, 'done': False}
        print(f"Задача добавлена (ID: {self.next_id})")
        self.next_id += 1

    def delete_task(self, task_id):
        if task_id in self.tasks:
            del self.tasks[task_id]
            print(f"Задача {task_id} удалена")
        else:
            print("Задача не найдена")

    def edit_task(self, task_id, new_name, new_text):
        if task_id in self.tasks:
            self.tasks[task_id]['name'] = new_name
            self.tasks[task_id]['text'] = new_text
            print(f"Задача {task_id} обновлена")
        else:
            print("Задача не найдена")

    def mark_done(self, task_id, done=True):
        if task_id in self.tasks:
            self.tasks[task_id]['done'] = done
            status = "выполнена" if done else "снята с выполнения"
            print(f"Задача {task_id} помечена как {status}")
        else:
            print("Задача не найдена")

    def show_tasks(self):
        if not self.tasks:
            print("Список задач пуст")
            return

        print("\nСписок задач:")
        for task_id, task in self.tasks.items():
            status = "✓" if task['done'] else "✗"
            print(f"{task_id}. [{status}] {task['date']} {task['name']} {task['text']}")

def main():
    todo = TodoList()

    while True:
        print("\n1. Добавить задачу")
        print("2. Удалить задачу")
        print("3. Редактировать задачу")
        print("4. Отметить выполненной")
        print("5. Снять отметку")
        print("6. Показать задачи")
        print("7. Выйти")

        choice = input("\nВыберите действие: ")

        if choice == '1':
            name = input("Введите название задачи: ")
            text = input("Введите описание задачи: ")
            todo.add_task(name, text)
        elif choice == '2':
            task_id = int(input("Введите ID задачи: "))
            todo.delete_task(task_id)
        elif choice == '3':
            task_id = int(input("Введите ID задачи: "))
            new_name = input("Введите новое название: ")
            new_text = input("Введите новое описание: ")
            todo.edit_task(task_id, new_name, new_text)
        elif choice == '4':
            task_id = int(input("Введите ID задачи: "))
            todo.mark_done(task_id)
        elif choice == '5':
            task_id = int(input("Введите ID задачи: "))
            todo.mark_done(task_id, False)
        elif choice == '6':
            todo.show_tasks()
        elif choice == '7':
            break
        else:
            print("Неверный ввод")

if __name__ == "__main__":
    main()