import datetime
import sys


from db_ops import *


from design import *
from PySide6.QtWidgets import QApplication, QMainWindow

SCREEN_SIZE = [1280, 640]


class MainWindow(Ui_TaskManager):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.retranslateUi(self)
        self.add_task_button.clicked.connect(self.show_add_task_dialog)

    def show_add_task_dialog(self):
        dlg = AddTaskWidget()
        dlg.exec()


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
            DBWriter.add_task(date=self.date, time=self.time, text=self.text)
        except NotOriginalTask as N:
            e = NotOriginalTaskDialog(N)
            e.exec()


class NotOriginalTaskDialog(Ui_NotOriginalTaskDialog):
    def __init__(self, data):
        super(NotOriginalTaskDialog, self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)
        self.label_2.setText(str(data))
        self.pushButton.clicked.connect(lambda: self.close())


if __name__ == "__main__":
    today = datetime.date.today()
    dates = [(today + datetime.timedelta(days=i)).strftime("%Y-%m-%d")for i in range(0 - today.weekday(), 7 - today.weekday())]
    print(dates)
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec())

