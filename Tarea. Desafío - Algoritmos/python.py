import json
import datetime
import os

if not os.path.isfile("tareas_pendientes.json"):
    with open("tareas_pendientes.json", "w") as archivo:
        json.dump([], archivo)

if not os.path.isfile("tareas_completadas.json"):
    with open("tareas_completadas.json", "w") as archivo:
        json.dump([], archivo)

def cargar_tareas(nombre_archivo):
    try:
        with open(nombre_archivo, 'r') as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return []

def guardar_tareas(tareas, nombre_archivo):
    with open(nombre_archivo, 'w') as archivo:
        json.dump(tareas, archivo, indent=4)

def agregar_tarea(tareas):
    titulo = input("Ingrese el título de la tarea: ")
    descripcion = input("Ingrese la descripción de la tarea: ")
    fecha_vencimiento = input("Ingrese la fecha de vencimiento (yyyy-mm-dd): ")

    tarea = {
        "titulo": titulo,
        "descripcion": descripcion,
        "completada": False,
        "fecha_vencimiento": fecha_vencimiento
    }
    tareas.append(tarea)
    print("Tarea agregada con éxito.")

def listar_tareas(tareas):
    for idx, tarea in enumerate(tareas, start=1):
        print(f"Tarea {idx}:")
        print(f"Título: {tarea['titulo']}")
        print(f"Descripción: {tarea['descripcion']}")
        print(f"Fecha de vencimiento: {tarea['fecha_vencimiento']}")
        print(f"Estado: {'Completada' if tarea['completada'] else 'Pendiente'}")
        print("-" * 20)

def marcar_completada(tareas):
    listar_tareas(tareas)
    try:
        indice = int(input("Ingrese el número de la tarea que desea marcar como completada: ")) - 1
        if 0 <= indice < len(tareas):
            tareas[indice]['completada'] = True
            print("Tarea marcada como completada.")
        else:
            print("Número de tarea inválido.")
    except ValueError:
        print("Entrada inválida. Debe ingresar un número válido.")

def tareas_por_vencer(tareas):
    hoy = datetime.date.today()
    print("Tareas próximas a vencerse:")
    for tarea in tareas:
        if not tarea['completada']:
            fecha_vencimiento = datetime.datetime.strptime(tarea['fecha_vencimiento'], "%Y-%m-%d").date()
            dias_restantes = (fecha_vencimiento - hoy).days
            if dias_restantes <= 3:
                print(f"Título: {tarea['titulo']}")
                print(f"Fecha de vencimiento: {tarea['fecha_vencimiento']}")
                print(f"Días restantes: {dias_restantes} días")
                print("-" * 20)

def main():
    tareas_pendientes = cargar_tareas("tareas_pendientes.json")
    tareas_completadas = cargar_tareas("tareas_completadas.json")

    while True:
        print("\n¡Bienvenido a la lista de tareas!")
        print("1. Agregar tarea")
        print("2. Listar tareas pendientes")
        print("3. Marcar tarea como completada")
        print("4. Mostrar tareas próximas a vencerse")
        print("5. Salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            agregar_tarea(tareas_pendientes)
        elif opcion == '2':
            listar_tareas(tareas_pendientes)
        elif opcion == '3':
            marcar_completada(tareas_pendientes)
        elif opcion == '4':
            tareas_por_vencer(tareas_pendientes)
        elif opcion == '5':
            guardar_tareas(tareas_pendientes, "tareas_pendientes.json")
            guardar_tareas(tareas_completadas, "tareas_completadas.json")
            print("Gracias por usar la lista de tareas. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()
    
