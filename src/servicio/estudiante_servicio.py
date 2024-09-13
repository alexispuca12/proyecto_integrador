from modelo.estudiantes import Estudiantes
from modelo.cursos import Cursos


class EstudianteServicio:

    @staticmethod
    def crear_estudiante(nombre, cursos_id, dni, correo_electronico, Numero_de_telefono, fecha_de_nacimiento):
        Curso = Cursos.get(Cursos.id == cursos_id)
        estudiante = Estudiantes.create(nombre=nombre, cursos_id=Curso, dni=dni, correo_electronico=correo_electronico, Numero_de_telefono=Numero_de_telefono, fecha_de_nacimiento=fecha_de_nacimiento)
        return estudiante
    
    @staticmethod
    def mostrar_estudiantes( ):
        return list(Estudiantes.select())
    
    @staticmethod
    def eliminar_estudiante(id):
        Estudiante = Estudiantes.get(Estudiantes.id == id)
        Estudiantes.delete_instance()
        return Estudiante