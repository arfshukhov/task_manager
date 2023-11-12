import threading


import sys


import textwrap


from functools import partial


from PySide6.QtCore import QModelIndex
from PySide6.QtGui import QStandardItem, QStandardItemModel


from middleware import *


from design import *


from PySide6.QtWidgets import QApplication, QMainWindow


class MainWindow(Ui_TaskManager):
    def __init__(self):
        super().__init__()
        self.model_list = [QStandardItemModel() for _ in range(7)]
        self.setupUi(self)
        self.retranslateUi(self)
        self.week_list = [
            self.monday_list,
            self.tuesday_list,
            self.monday_list,
            self.thursday_list,
            self.friday_list,
            self.saturday_list,
            self.sunday_list
        ]
        self.add_task_button.clicked.connect(self.show_add_task_dialog)
        self.set_model_for()
        self.fill_task_list()
        self.set_untriggers()

    def clear_columns(self):
        for i in self.model_list:
            i.clear()

    def set_untriggers(self):
        for i in self.week_list:
            i.setEditTriggers(QAbstractItemView.NoEditTriggers)

    def set_model_for(self):
        for i in range(len(self.week_list)):
            self.week_list[i].setModel(self.model_list[i])

    def show_add_task_dialog(self):
        dlg = AddTaskWidget()
        dlg.exec()
        self.clear_columns()
        self.fill_task_list()

    def get_tasks(self):
        return WeekProcessor.get_week_tasks()

    def fill_task_list(self):
        for i, k in enumerate(self.get_tasks()):
            trigger = partial(self.open_task, graph=i)
            self.week_list[i].clicked[QModelIndex].connect(trigger)
            for g in k:
                s = "\n".join(textwrap.wrap(g.text, 22))
                self.model_list[i].appendRow(QStandardItem(f"{g.time}\n{s}"))

    def open_task(self, index, graph):
        task = self.get_tasks()[int(graph)][int(index.row())]
        data = (task.text, task.time, task.date, task.uid)
        dlg = CompleteTaskDialog(data)
        dlg.exec()
        self.clear_columns()
        self.fill_task_list()


class AddTaskWidget(Ui_AddTaskWidget):
    time: Time
    date: Date
    text: Text

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.retranslateUi(self)
        self.calendar_widget.setMinimumDate(QDate(*map(int, str(datetime.datetime.today())[:10].split("-"))))
        self.done_button.clicked.connect(self.get_data)

    def get_data(self):
        self.time = self.time_edit.time().toString("HH:mm")
        self.date = self.calendar_widget.selectedDate().toString("dd-MM-yyyy")
        self.text = self.text_edit.toPlainText()
        self.add_task()

    def add_task(self):
        try:
            if self.text.lstrip(" ") != "":
                DBWriter.add_task(date=self.date, time=self.time, text=self.text)
            else:
                pass
        except NotOriginalTask as N:
            e = NotOriginalTaskDialog(N)
            e.exec()
        finally:
            self.close()


class NotOriginalTaskDialog(Ui_NotOriginalTaskDialog):
    def __init__(self, data):
        super(NotOriginalTaskDialog, self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)
        self.label_2.setText(str(data))
        self.pushButton.clicked.connect(self.close)


class CompleteTaskDialog(Ui_CompleteTaskDialog):
    def __init__(self, task: list):
        super(Ui_CompleteTaskDialog, self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)
        self.time_l.setText(f"{task[0]}")
        self.text_l.setText(f"{task[1]}  {task[2]}")
        self.uid = task[3]
        self.status = DBReader.get_status(self.uid)
        self.complete.clicked.connect(lambda: self.complete_())
        self.cancel.clicked.connect(self.close)

    def complete_(self):
        print(self.uid)
        DBWriter.make_complete(self.uid)
        self.close()


def run_app():
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    app.exec()
    TaskProcessor.app_is_running = False


if __name__ == "__main__":
    t1 = threading.Thread(target=TaskProcessor.check_date, args=())
    t2 = threading.Thread(target=run_app, args=())
    t1.start()
    t2.start()
