import sys
from PyQt6 import QtWidgets, QtCore, QtGui
from ui.main_window import Ui_MainWin
from ui.addtask import Ui_TaskWin
from main import TodoList

class TaskWindow(QtWidgets.QDialog):
    def __init__(self, parent=None, todo_app=None, task_id=None):
        super().__init__(parent)
        self.ui = Ui_TaskWin()
        self.ui.setupUi(self)
        
        self.todo_app = todo_app
        self.task_id = task_id
        self.is_edit_mode = task_id is not None
        
        self.setup_connections()
        self.load_task_data()
        
    def setup_connections(self):
        self.ui.savetask.clicked.connect(self.save_task)
        self.ui.deletetask.clicked.connect(self.delete_task)
        
    def load_task_data(self):
        """Загружает данные задачи если это режим редактирования"""
        if self.is_edit_mode and self.task_id in self.todo_app.todo.tasks:
            task = self.todo_app.todo.tasks[self.task_id]
            self.ui.nametask.setText(task['name'])
            self.ui.abouttask.setPlainText(task['text'])
            
    def save_task(self):
        """Сохраняет новую или редактируемую задачу"""
        name = self.ui.nametask.text().strip()
        text = self.ui.abouttask.toPlainText().strip()
        
        if not name:
            QtWidgets.QMessageBox.warning(self, "Ошибка", "Введите название задачи!")
            return
            
        if self.is_edit_mode:
            # Редактируем существующую задачу
            self.todo_app.todo.edit_task(self.task_id, name, text)
        else:
            # Добавляем новую задачу
            self.todo_app.todo.add_task(name, text)
            
        self.todo_app.update_task_list()
        self.accept()
        
    def delete_task(self):
        """Удаляет задачу"""
        if self.is_edit_mode:
            reply = QtWidgets.QMessageBox.question(
                self, 'Подтверждение', 
                'Вы уверены, что хотите удалить эту задачу?',
                QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No
            )
            
            if reply == QtWidgets.QMessageBox.StandardButton.Yes:
                self.todo_app.todo.delete_task(self.task_id)
                self.todo_app.update_task_list()
                self.accept()
        else:
            # Если это создание новой задачи - просто закрываем окно
            self.reject()

class MainWindow(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWin()
        self.ui.setupUi(self)

        # Инициализируем переменные ДО вызова методов
        self.todo = TodoList()
        self.show_completed = True

        self.add_sample_tasks()
        self.update_task_list()

        # Подключаем сигналы
        self.ui.addnewtask.clicked.connect(self.add_new_task)
        self.ui.marktask.clicked.connect(self.mark_task_done)
        self.ui.radioButton.toggled.connect(self.toggle_completed_tasks)
        self.ui.listtask.itemDoubleClicked.connect(self.edit_task_double_click)
        
        # Настраиваем контекстное меню
        self.setup_context_menu()

    def setup_context_menu(self):
        """Настраивает контекстное меню для списка задач"""
        self.ui.listtask.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.CustomContextMenu)
        self.ui.listtask.customContextMenuRequested.connect(self.show_context_menu)
        
        # Создаем меню
        self.context_menu = QtWidgets.QMenu(self)
        
        # Создаем действия
        self.edit_action = QtGui.QAction("Изменить", self)
        self.delete_action = QtGui.QAction("Удалить", self)
        
        # Подключаем действия
        self.edit_action.triggered.connect(self.edit_task_context)
        self.delete_action.triggered.connect(self.delete_task_context)
        
        # Добавляем действия в меню
        self.context_menu.addAction(self.edit_action)
        self.context_menu.addAction(self.delete_action)

    def show_context_menu(self, position):
        """Показывает контекстное меню по правому клику"""
        item = self.ui.listtask.itemAt(position)
        if item:
            self.context_menu.exec(self.ui.listtask.mapToGlobal(position))

    def edit_task_double_click(self, item):
        """Редактирует задачу по двойному клику ЛКМ"""
        if item:
            self.edit_task(item)

    def edit_task_context(self):
        """Редактирует задачу из контекстного меню"""
        current_item = self.ui.listtask.currentItem()
        if current_item:
            self.edit_task(current_item)

    def edit_task(self, item):
        """Основной метод редактирования задачи"""
        item_text = item.text()
        task_id = int(item_text.split('.')[0])
        
        task_window = TaskWindow(self, self, task_id)
        task_window.exec()

    def delete_task_context(self):
        """Удаляет задачу из контекстного меню"""
        current_item = self.ui.listtask.currentItem()
        if current_item:
            item_text = current_item.text()
            task_id = int(item_text.split('.')[0])
            
            reply = QtWidgets.QMessageBox.question(
                self, 'Подтверждение удаления', 
                'Вы уверены, что хотите удалить эту задачу?',
                QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No
            )
            
            if reply == QtWidgets.QMessageBox.StandardButton.Yes:
                self.todo.delete_task(task_id)
                self.update_task_list()

    def add_sample_tasks(self):
        """Тестовые задачи для отладки"""
        self.todo.add_task("Купить продукты", "Молоко, хлеб, яйца")
        self.todo.add_task("Сделать домашку", "По математике и физике")
        self.todo.add_task("Встреча с друзьями", "В кальянке в 18:00")

    def update_task_list(self):
        """Обновляет список задач в интерфейсе"""
        self.ui.listtask.clear()

        for task_id, task in self.todo.tasks.items():
            # Фильтруем выполненные задачи если нужно
            if not self.show_completed and task['done']:
                continue
                
            status = "✓" if task['done'] else "✗"
            task_text = f"{task_id}. [{status}] {task['date']} - {task['name']}"
            item = QtWidgets.QListWidgetItem(task_text)
            
            # Визуально отличаем выполненные задачи
            if task['done']:
                item.setBackground(QtGui.QColor(220, 255, 220))  # светло-зеленый
                
            self.ui.listtask.addItem(item)

    def add_new_task(self):
        """Открывает окно для создания новой задачи"""
        task_window = TaskWindow(self, self)
        task_window.exec()

    def mark_task_done(self):
        """Отмечаем выбранную задачу как выполненную/не выполненную"""
        current_item = self.ui.listtask.currentItem()
        if current_item:
            item_text = current_item.text()
            task_id = int(item_text.split('.')[0])
            
            if task_id in self.todo.tasks:
                # Переключаем статус выполнено/не выполнено
                current_status = self.todo.tasks[task_id]['done']
                self.todo.mark_done(task_id, not current_status)
                self.update_task_list()

    def toggle_completed_tasks(self, checked):
        """Показывает/скрывает выполненные задачи"""
        self.show_completed = checked
        self.update_task_list()

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()