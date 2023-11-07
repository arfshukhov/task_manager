import datetime
import sys

from data_types import *

from models import *

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

    def get_data(self):
        # self.time = self.calendar_widget.
        ...

if __name__ == "__main__":
    print(str(datetime.datetime.today())[:10])
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec())
