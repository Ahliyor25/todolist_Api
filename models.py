import datetime
from peewee import *

db = SqliteDatabase('db1.db')

class BaseModel(Model):
    class Meta:
        database = db

class Tasks(BaseModel):
    id = AutoField()
    title = CharField()
    description = CharField()
    done = BooleanField()

       # Tasks.create_table()
        #first = Tasks(title='Buy groceries' , description ='Milk, Cheese, Pizza, Fruit, Tylenol', done=False).save()

       # second = Tasks(title='Learn python ' , description ='Need to find a good Python tutorial on the web', done=False).save()
