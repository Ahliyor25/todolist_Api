import datetime
from peewee import *

db = SqliteDatabase('db.db')

class BaseModel(Model):
    class Meta:
        database = db

class tasks(BaseModel):
    id = AutoField()
    title = CharField()
    description = CharField
    done = BooleanField()

#first = tasks(id=1,title='Buy groceries' , description ='Milk, Cheese, Pizza, Fruit, Tylenol', done=False)

#second = tasks(id=2,title='Learn python ' , description ='Need to find a good Python tutorial on the web', done=False)
#tasks.create_table()