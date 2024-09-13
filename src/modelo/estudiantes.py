from peewee import Model, AutoField, CharField, IntegerField, DateField, ForeignKeyField
from basedato.db import db
from modelo.cursos import Cursos

class Estudiantes(Model):
    id = AutoField( )
    nombre = CharField()
    dni = IntegerField()
    correo_electronico = CharField()
    Numero_de_telefono = IntegerField()
    fecha_de_nacimiento = DateField()
    cursos_id = ForeignKeyField(Cursos)

    class Meta:
        database = db
        table_name = "estudiantes"