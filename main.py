from peewee import *

db = PostgresqlDatabase('countries', user='base2', password='',
                        host='localhost', port=5432)

class BaseModel(Model):
    class Meta:
        database = db

class Country(BaseModel):
    name = CharField()
    capital = CharField()

# db.connect()
# db.drop_tables([Country])
# db.create_tables([Country])

