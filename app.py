import sys
from PyQt6 import QtWidgets, QtCore
from ui.main_window import Ui_MainWin
from main import TodoList

class MainWindow(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWin()
        self.ui.setupUi(self)

        self.todo = TodoList() # Подтягиваем логику с основного файла

        self.add_sample_tasks() # тут добавляются таски для теста

        self.update_task_list()

        self.ui.addnewtask.clicked.connect(self.add_new_task)
        self.ui.marktask.clicked.connect(self.mark_task_done)

    def add_sample_tasks(self):
        """Тестовые задачи для отладки"""
        self.todo.add_task("Купить продукты", "Молоко, хлеб, яйца")
        self.todo.add_task("Сделать домашку", "По математике и физике")
        self.todo.add_task("Встреча с друзьями", "В кальянке в 18:00")

    def update_task_list(self):
        """Обновляет список задач в интерфейсе"""
        self.ui.listtask.clear()

        for task_id, task in self.todo.tasks.items():
            status = "✓" if task['done'] else "✗"
            task_text = f"{task_id}. [{status}] {task['date']} - {task['name']}"
            self.ui.listtask.addItem(task_text)

    def add_new_task(self):
        """Добавляет новую задачу через диалоговое окно"""
        name, ok1 = QtWidgets.QInputDialog.getText(self, "Новая задача", "Введите название:")
        if ok1 and name:
            text, ok2 = QtWidgets.QInputDialog.getText(self, "Описание задачи", "Введите описание:")
            if ok2:
                self.todo.add_task(name, text)
                self.update_task_list()

    def mark_task_done(self):
        """Отмечаем выбранную задачу как выполненную"""
        current_row = self.ui.listtask.currentRow()
        if current_row >= 0:
            item_text = self.ui.listtask.item(current_row).text()
            task_id = int(item_text.split('.')[0])

            self.todo.mark_done(task_id)
            self.update_task_list()

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()