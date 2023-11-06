class NotOriginalTask(Exception):
    def __init__(self, arg: tuple):
        if arg:
            self.arg = arg
        else:
            self.arg = None

    def __str__(self):
        if self.arg:
            return f"U are crearing not original task: {str(self.arg)}"
        else:
            return "U are crearing not original task."


