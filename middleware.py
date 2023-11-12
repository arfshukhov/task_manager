import datetime
from time import sleep

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


class TaskProcessor:
    app_is_running = True

    @classmethod
    def check_date(cls):
        time_ = 0
        while time_ <= 86400:
            tasks = DBReader.get_days_task(datetime.date.today().strftime("%d-%m-%Y"))
            for i in tasks:
                t = datetime.datetime.today().time().strftime("%H:%M")
                if datetime.datetime.strptime(i.time, "%H:%M") < datetime.datetime.strptime(t, "%H:%M"):
                    if DBReader.get_status_by_uid(i.uid) != "completed":
                        DBWriter.make_failed(i.uid)
            if not cls.app_is_running:
                break
            time_ += 30
            sleep(30)


class WeekProcessor:
    @classmethod
    def __get_week_days(cls) -> list:
        today = datetime.date.today()
        dates = [(today + datetime.timedelta(days=i)).strftime("%d-%m-%Y")
                 for i in range(0 - today.weekday(), 7 - today.weekday())]
        return dates

    @classmethod
    def get_week_tasks(cls) -> Week:
        days = cls.__get_week_days()
        #print(cls.__get_week_days())
        tasks: Week = []
        for i in days:
            tasks_by_day = [task for task in DBReader.get_actual_task(i)]
            tasks_by_day.sort(key=lambda x: datetime.datetime.strptime(x.time, "%H:%M"))
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
    def get_status_by_uid(cls, uid):
        return TaskStatus.select().where(TaskStatus.uid == uid).get().status

    @classmethod
    def __match_for_active(cls, task):
        try:
            return TaskStatus.select().where(TaskStatus.uid == task.uid).get().status in ("active", "failed")
        except Exception:
            print("__match_for_active err")
            db.rollback()

    @classmethod
    def __match_for_failed(cls, task):
        try:
            return TaskStatus.select().where(TaskStatus.uid == task.uid).get().status == "failed"
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

    @classmethod
    def get_status(cls, uid):
        return TaskStatus.select().where(TaskStatus.uid == uid).get().status


class DBWriter:
    @classmethod
    def add_task(cls, text: Text, time: Time, date: Date):
        md5_hash = Hasher.make_hash(text, time, date)
        ids = [id_ for id_ in Task.select().where(Task.uid == md5_hash)]
        if len(ids) == 0:
            try:
                Task(text=text, time=time, date=date, uid=md5_hash).save()
                TaskStatus(uid=md5_hash, status="active").save()
            except Exception as e:
                db.rollback()
        else:
            raise NotOriginalTask((text, time, date))

    @classmethod
    def make_failed(cls, uid) -> DBOperationResult:
        query = (TaskStatus
                 .update({TaskStatus.status: "failed"})
                 .where(TaskStatus.uid == uid)).execute()

    @classmethod
    def make_complete(cls, uid):
        query = (TaskStatus
                 .update({TaskStatus.status: "completed"})
                 .where(TaskStatus.uid == uid)).execute()
