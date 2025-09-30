import datetime
import json
import os

class TodoList:
    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.tasks = {}
        self.next_id = 1
        self.load_tasks()

    def load_tasks(self):
        """Загружает задачи из JSON файла"""
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    self.tasks = {int(k): v for k, v in data.get('tasks', {}).items()}
                    self.next_id = data.get('next_id', 1)
                    print(f"Задачи загружены из {self.filename}")
            except (json.JSONDecodeError, KeyError, ValueError) as e:
                print(f"Ошибка загрузки файла: {e}. Создаю новый список задач.")
                self.tasks = {}
                self.next_id = 1
        else:
            print("Файл с задачами не найден. Создаю новый список задач.")

    def save_tasks(self):
        """Сохраняет задачи в JSON файл"""
        data = {
            'tasks': self.tasks,
            'next_id': self.next_id
        }
        try:
            with open(self.filename, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            print(f"Задачи сохранены в {self.filename}")
        except Exception as e:
            print(f"Ошибка сохранения: {e}")

    def add_task(self, name, text, date=None):
        """Добавляет задачу с возможностью указать дату"""
        if date is None:
            date = datetime.datetime.now().strftime("%d-%m-%Y %H:%M")
        
        self.tasks[self.next_id] = {
            'date': date,
            'name': name, 
            'text': text, 
            'done': False
        }
        print(f"Задача добавлена (ID: {self.next_id})")
        self.next_id += 1
        self.save_tasks()  # Автосохранение
        return self.next_id - 1

    def delete_task(self, task_id):
        if task_id in self.tasks:
            del self.tasks[task_id]
            print(f"Задача {task_id} удалена")
            self.save_tasks()  # Автосохранение
            return True
        else:
            print("Задача не найдена")
            return False

    def edit_task(self, task_id, new_name, new_text, new_date=None):
        if task_id in self.tasks:
            self.tasks[task_id]['name'] = new_name
            self.tasks[task_id]['text'] = new_text
            if new_date:
                self.tasks[task_id]['date'] = new_date
            print(f"Задача {task_id} обновлена")
            self.save_tasks()  # Автосохранение
            return True
        else:
            print("Задача не найдена")
            return False

    def mark_done(self, task_id, done=True):
        if task_id in self.tasks:
            self.tasks[task_id]['done'] = done
            status = "выполнена" if done else "снята с выполнения"
            print(f"Задача {task_id} помечена как {status}")
            self.save_tasks()  # Автосохранение
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