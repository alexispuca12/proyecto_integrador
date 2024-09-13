from basedato.db import db
from modelo.cursos import Cursos
from modelo.estudiantes import Estudiantes
from controlador.curso_controlador import CursoControlador
from controlador.estudiante_controlador import EstudianteControlador

def main():
    db.connect()
    db.create_tables([Cursos, Estudiantes])
    #CursoControlador.crear("Programacion IV", "ess programar", "12/14/2019", "330/11/2019", "83 horas")
    #EstudianteControlador.crear("Alexisss", 3, 3192391332, "lol2@gmail.com", 137753, "2/39/13482")
    EstudianteControlador.eliminar(1)

if __name__ == '__main__':
    main()