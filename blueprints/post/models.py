import datetime as dt
from peewee import *
from blueprints.user.models import User


db = SqliteDatabase('database.db')


class Post(Model):
    user = ForeignKeyField(User, backref='posts')
    text = TextField()
    date = DateTimeField(default=dt.datetime.now)

    class Meta:
        database = db

    @property
    def post_date(self):
        return self.date.strftime('%Y-%m-%d %H:%M:%S')
