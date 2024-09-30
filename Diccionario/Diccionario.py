# Función para crear el diccionario inicial de una persona
def crear_diccionario():
    info = {}
    info["nombre"] = input("Nombre: ")
    info["edad"] = int(input("Edad: "))
    info["ciudad"] = input("Ciudad: ")
    info["profesion"] = input("Profesión: ")
    return info


# Modificar valor en un campo existente
def modificar_valor(diccionario, campo):
    if campo in diccionario:
        diccionario[campo] = input(f"Nuevo valor para '{campo}': ")
        print(f"'{campo}' actualizado.")
    else:
        print(f"'{campo}' no existe.")


# Agregar un nuevo campo-valor
def agregar_campo(diccionario):
    while True:
        campo = input("Nuevo campo (o escribe 'salir' para terminar): ")
        if campo.lower() == 'salir':
            break
        diccionario[campo] = input(f"Valor para '{campo}': ")
        print(f"'{campo}' agregado.")


# Verificar si un campo existe
def verificar_campo(diccionario):
    campo = input("Campo a verificar: ")
    if campo in diccionario:
        print(f"'{campo}' existe: {diccionario[campo]}")
    else:
        if input(f"¿Agregar '{campo}'? (sí/no): ").lower() == 'sí':
            diccionario[campo] = input(f"Valor para '{campo}': ")
            print(f"'{campo}' agregado.")


# Eliminar un campo
def eliminar_campo(diccionario):
    campo = input("Campo a eliminar: ")
    diccionario.pop(campo, None)
    print(f"'{campo}' eliminado.")


# Menú de interacción
def menu_interactivo():
    registros = []  # Lista para almacenar registros de múltiples personas

    while True:
        print()  # Salto de línea antes de agregar un nuevo registro
        diccionario = crear_diccionario()  # Crear un nuevo registro
        registros.append(diccionario)  # Agregar el registro a la lista

        while True:
            print("\nRegistros:", registros)
            print(
                "1. Modificar valor\n2. Agregar más campos\n3. Verificar campo\n4. Eliminar campo\n5. Agregar otro registro\n6. Salir")
            opcion = input("Opción: ")

            if opcion == '1':
                modificar_valor(diccionario, input("Campo a modificar: "))
            elif opcion == '2':
                agregar_campo(diccionario)
            elif opcion == '3':
                verificar_campo(diccionario)
            elif opcion == '4':
                eliminar_campo(diccionario)
            elif opcion == '5':
                break  # Salir del bucle interno para agregar otro registro
            elif opcion == '6':
                print("Saliendo... Registros finales:", registros)
                return  # Salir del programa
            else:
                print("Opción no válida.")


# Ejecutar el menú interactivo
menu_interactivo()