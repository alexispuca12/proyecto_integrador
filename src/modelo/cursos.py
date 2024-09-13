from peewee import Model, AutoField, CharField, DateField, TimeField
from basedato.db import db

class Cursos(Model):
    id = AutoField( )
    descripcion = CharField
    nombre = CharField(unique=True)
    fecha_de_inicio = DateField()
    fecha_de_fin = DateField()
    horas = TimeField

    class Meta:
        database = db
        table_name = "cursos"