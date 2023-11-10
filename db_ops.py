import datetime

from data_types import *

from models import *
import hashlib as hl
from exceptions import NotOriginalTask

WEEK = {
    "monday": 1,
    "tuesday": 2,
    "wednesday": 3,
    "thursday": 4,
    "friday": 5,
    "saturday": 6,
    "sunday": 7
}


class WeekProcessor:
    @classmethod
    def get_week_days(cls) -> list:
        today = datetime.date.today()
        dates = [(today + datetime.timedelta(days=i)).strftime("%Y-%m-%d")
                 for i in range(0 - today.weekday(), 7 - today.weekday())]
        return dates

    @classmethod
    def get_week_tasks(cls) -> List[List[Task]]:
        days = cls.get_week_days()
        tasks: List[List[Task]] = []
        for i in days:
            tasks_by_day = [task for task in DBReader.get_actual_task(i)]
            tasks.append(tasks_by_day)
        return tasks


class Hasher:
    @classmethod
    def make_hash(cls, text, time, date):
        md5_hash = hl.new('md5')
        token = "|".join([text, time, date])
        md5_hash.update(token.encode())
        hex_hash = md5_hash.hexdigest()
        return str(hex_hash)

    @classmethod
    def check_hash(cls, text, time, date):
        h = cls.make_hash(text, time, date)
        tasks = [t for t in Task.select().where(Task.uid == h)]
        if len(tasks) == 0:
            return True
        else:
            return False


class DBReader:
    @classmethod
    def __match_for_active(cls, task):
        try:
            return TaskStatus.select().where(TaskStatus.uid == task.uid).get() in ("active", "failed")
        except Exception:
            db.rollback()

    @classmethod
    def __match_for_failed(cls, task):
        try:
            return TaskStatus.select().where(TaskStatus.uid == task.uid).get() == "failed"
        except Exception:
            db.rollback()

    @classmethod
    def get_days_task(cls, day):
        return [task for task in Task.select().where(Task.date == day)]

    @classmethod
    def get_actual_task(cls, day):
        return list(filter(cls.__match_for_active, cls.get_days_task(day)))

    @classmethod
    def get_failed(cls, day):
        return list(filter(cls.__match_for_failed, cls.get_days_task(day)))


class DBWriter:
    @classmethod
    def add_task(cls, text: Text, time: Time, date: Date):
        md5_hash = Hasher.make_hash(text, time, date)
        ids = [id_ for id_ in Task.select().where(Task.uid == md5_hash)]
        if len(ids) == 0:
            try:
                Task(text=text, time=time, date=date, uid=md5_hash).save()
                TaskStatus(uid=md5_hash, status="active").save()
            except:
                db.rollback()
        else:
            raise NotOriginalTask((text, time, date))

    @classmethod
    def make_failed(cls, uid) -> DBOperationResult:
        query = (TaskStatus
                 .update({TaskStatus.status: "failed"})
                 .where(TaskStatus.uid == uid))
        query.execute()
