from collections import deque


cola_notificaciones = deque()

class Notificacion:
    def __init__(self, hora, app, mensaje):
        self.hora = hora
        self.app = app
        self.mensaje = mensaje

#a) Función para eliminar todas las notificaciones de Facebook de la cola
def eliminar_notificaciones_facebook():
    global cola_notificaciones
    cola_notificaciones = deque([notificacion for notificacion in cola_notificaciones if notificacion.app != 'Facebook'])

#b) Función para mostrar las notificaciones de Twitter con la palabra 'Python'
def mostrar_notificaciones_python():
    for notificacion in cola_notificaciones:
        if notificacion.app == 'Twitter' and 'Python' in notificacion.mensaje:
            print(f'Hora: {notificacion.hora}, Mensaje: {notificacion.mensaje}')

#c) Función para contar las notificaciones producidas entre las 11:43 y las 15:57 utilizando una pila
def contar_notificaciones_pila():
    pila_temporal = []
    contador = 0

    for notificacion in cola_notificaciones:
        if '11:43' <= notificacion.hora <= '15:57':
            pila_temporal.append(notificacion)
            contador += 1
    return contador

cola_notificaciones.append(Notificacion('10:30', 'Facebook', 'Notificación 1'))
cola_notificaciones.append(Notificacion('11:50', 'Twitter', 'Notificación 2'))
cola_notificaciones.append(Notificacion('12:15', 'Twitter', 'Notificación 3'))
cola_notificaciones.append(Notificacion('14:30', 'Facebook', 'Notificación 4'))
cola_notificaciones.append(Notificacion('15:00', 'Twitter', 'Notificación con Python'))
cola_notificaciones.append(Notificacion('16:00', 'Facebook', 'Notificación 5'))

contador_notificaciones = contar_notificaciones_pila()
print(f'Cantidad de notificaciones entre las 11:43 y las 15:57: {contador_notificaciones}')
