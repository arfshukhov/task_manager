from models import *
import hashlib as hl
from exceptions import NotOriginalTask


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
    def get_days_task(cls, day):
        return [task for task in Task.select().where(Task.date == day)]


class DBWriter:
    @classmethod
    def add_task(cls,text, time, date):
        md5_hash = Hasher.make_hash(text, time, date)
        ids = [id_ for id_ in Task.select().where(Task.uid == md5_hash)]
        if len(ids) == 0:
            Task()


