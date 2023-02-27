# Install peewee
from peewee import *

from os import path

connection = path.dirname(path.realpath(__file__))

db = SqliteDatabase(path.join(connection, "Mariao.db"))


# creating my first table


class User(Model):
    name = CharField()
    email = CharField(unique=True)
    password = CharField()

    class Meta:
        database = db


User.create_table(fail_silently=True)


class Student(Model):
    name = CharField()
    age = CharField()
    id = CharField()
    stream = CharField()
    gender = CharField()

    class Meta:
        database = db


Student.create_table(fail_silently=True)



class People(Model):
    name = CharField()
    phonenumber = CharField()
    email = CharField()
    country = CharField()
    gender = CharField()
    religion = CharField()
    password = CharField()

    class Meta:
        database = db


People.create_table(fail_silently=True)