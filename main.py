import datetime

class TodoList:
    def __init__(self):
        self.tasks = {}
        self.next_id = 1

    def add_task(self, name, text):
        self.tasks[self.next_id] = {
            'date': datetime.datetime.now().strftime("%d-%m-%Y %H:%M"),
            'name': name, 
            'text': text, 
            'done': False
        }
        print(f"Задача добавлена (ID: {self.next_id})")
        self.next_id += 1
        return self.next_id - 1  # Возвращаем ID добавленной задачи

    def delete_task(self, task_id):
        if task_id in self.tasks:
            del self.tasks[task_id]
            print(f"Задача {task_id} удалена")
            return True
        else:
            print("Задача не найдена")
            return False

    def edit_task(self, task_id, new_name, new_text):
        if task_id in self.tasks:
            self.tasks[task_id]['name'] = new_name
            self.tasks[task_id]['text'] = new_text
            print(f"Задача {task_id} обновлена")
            return True
        else:
            print("Задача не найдена")
            return False

    def mark_done(self, task_id, done=True):
        if task_id in self.tasks:
            self.tasks[task_id]['done'] = done
            status = "выполнена" if done else "снята с выполнения"
            print(f"Задача {task_id} помечена как {status}")
            return True
        else:
            print("Задача не найдена")
            return False

    def show_tasks(self):
        if not self.tasks:
            print("Список задач пуст")
            return

        print("\nСписок задач:")
        for task_id, task in self.tasks.items():
            status = "✓" if task['done'] else "✗"
            print(f"{task_id}. [{status}] {task['date']} {task['name']} {task['text']}")