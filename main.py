import datetime
import sys


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
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.retranslateUi(self)





if __name__ == "__main__":
   # print(datetime.datetime.strptime(str(datetime.datetime.now()), "%Y/%m/%d"))
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec())
