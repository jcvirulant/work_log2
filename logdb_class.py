from collections import OrderedDict
import datetime
import sys
import os

from peewee import *

db = SqliteDatabase("log.db")


class Log(Model):
    class Meta:
        database = db


class Employee(Log):
    first_name = CharField()
    last_name = CharField()


class Task(Log):
    employee = ForeignKeyField(Employee, related_name='tasks')
    task_name = CharField(max=50)
    duration = DateTimeField("%h:%m")
    date = DateTimeField()
    notes = TextField()
    timestamp = DateTimeField(default=datetime.datetime.now)
    date = DateTimeField(formats='%Y-%m-%d')


if __name__ == '__main__':
    db.connect
    db.create_tables([Log], safe=True)
