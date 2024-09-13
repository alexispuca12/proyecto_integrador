from servicio.estudiante_servicio import EstudianteServicio

class EstudianteControlador():

    def crear(nombre, cursos_id, dni, correo_electronico, Numero_de_telefono, fecha_de_nacimiento):
        return EstudianteServicio.crear_estudiante(nombre, cursos_id, dni, correo_electronico, Numero_de_telefono, fecha_de_nacimiento)
    
    def mostrar():
        return EstudianteServicio.mostrar_estudiantes()
    
    def eliminar(id):
        return EstudianteServicio.eliminar_estudiante(id)