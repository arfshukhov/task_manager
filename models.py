# import datetime

from peewee import *

db = SqliteDatabase("database.db")


class Task(Model):
    text = TextField(null=False)
    time = TimeField(formats="%H:%M")
    date = DateField(formats="%Y-%m-%d")
    uid = TextField(null=False)

    class Meta:
        database = db
        db_table = "Task"
