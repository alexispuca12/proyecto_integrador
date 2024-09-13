from servicio.curso_servicio import CursoServicio

class CursoControlador():

    def crear(nombre, descripcion, fecha_de_inicio, fecha_de_fin, horas):
        return CursoServicio.crear_curso(nombre, descripcion, fecha_de_inicio, fecha_de_fin, horas)
    
    def mostrar( ):
        return CursoServicio.mostrar_cursos()