from modelo.cursos import Cursos


class CursoServicio:

    @staticmethod
    def crear_curso(nombre, descripcion, fecha_de_inicio, fecha_de_fin, horas):
        curso = Cursos.create(nombre=nombre, descripcion=descripcion, fecha_de_inicio=fecha_de_inicio, fecha_de_fin=fecha_de_fin, horas=horas )
        return curso
    
    @staticmethod
    def mostrar_cursos( ):
        return list(Cursos.select())