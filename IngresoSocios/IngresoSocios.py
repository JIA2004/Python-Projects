import random
import re

mensaje = open('mensaje.txt','r')

def imprimirArchivo(archivo):
    for line in mensaje:
        print(line)


opciones = ["A", "B", "C", "D", "E"]
imprimirArchivo(mensaje)
print()
opcion = input("Ingrese su opción: ")
cont = 0
users = {}

def new_user():
    num = int(input("Ingrese la cantidad de usuarios que desea registrar: "))
    lista = []

    for i in range(num):
        nombre = input("Por favor, ingrese su nombre: ")
        while len(nombre) < 5 or len(nombre) > 50:
            print("Nombre inválido (debe tener entre 5 y 50 caracteres).")
            nombre = input("Por favor, ingrese su nombre: ")

        apellido = input("Por favor, ingrese su apellido: ")
        while len(apellido) < 5 or len(apellido) > 50:
            print("Apellido inválido (debe tener entre 5 y 50 caracteres).")
            apellido = input("Por favor, ingrese su apellido: ")

        tel = input("Ingrese su número de teléfono (10 dígitos mínimo): ")
        while len(tel) < 10:
            print("Número de teléfono inválido.")
            tel = input("Ingrese su número de teléfono: ")

        mail = input("Ingrese su correo electrónico: ")
        while len(mail) < 5 or len(mail) > 50 or not re.match(r"[^@]+@[^@]+\.[^@]+", mail):
            print("Correo inválido. Por favor, ingrese un correo electrónico válido.")
            mail = input("Ingrese nuevamente su correo electrónico: ")

        print("\nUsuario cargado en el sistema con éxito.")
        codigo = "".join([str(random.randint(1, 9)) for _ in range(7)])
        lista.append(codigo)

        users[codigo] = {
            'Nombre': nombre,
            'Apellido': apellido,
            'Teléfono': tel,
            'Correo': mail,
        }
        print()

def show_user(id):
    print("\nInformación del Usuario")
    print("-----------------------")
    print(f"ID: {id}")
    for key, value in users[id].items():
        print(f"{key}: {value}")
    print()

def edit_user(id):
    if id in users:
        print("\nInformación del usuario seleccionado:")
        print("-------------------------------")
        for key, value in users[id].items():
            print(f"{key}: {value}")
        campo = input("¿Qué campo desea editar (Nombre, Apellido, Teléfono, Correo)?: ").capitalize()
        if campo in users[id]:
            nuevo_valor = input(f"Ingrese el nuevo valor para {campo}: ")
            users[id][campo] = nuevo_valor
            print("\n¡Información actualizada con éxito!")
        else:
            print("Campo inválido.")
    else:
        print("Usuario no encontrado.")

def delete_user(id):
    del(users[id])
    print("Usuario eliminado con éxito.")

def list_users(dict):
    print("\nUsuarios Registrados")
    print("--------------------")
    for key, value in dict.items():
        print(f"ID: {key}")
        for k, v in value.items():
            print(f"{k}: {v}")
        print()

while True:
    while opcion.upper() not in opciones:
        print()
        print(f"'{opcion}' no es una opción válida.")
        imprimirArchivo(mensaje)
        print()
        opcion = input("Ingrese su opción: ")

    while opcion.upper() == "A":
        new_user()
        print("¡Todos los usuarios fueron cargados con éxito!")
        cont += 1
        print()
        imprimirArchivo(mensaje)
        print()
        opcion = input("Ingrese su opción: ")

    while cont <= 0 and (opcion.upper() in ["B", "C", "D", "E"]):
        print("\nNo hay ningún usuario registrado en el sistema.")
        imprimirArchivo(mensaje)
        print()
        opcion = input("Ingrese su opción: ")

    while opcion.upper() == "B" and cont >= 1:
        list_users(users)
        print()
        imprimirArchivo(mensaje)
        print()
        opcion = input("Ingrese su opción: ")

    while opcion.upper() == "C" and cont >= 1:
        list_users(users)
        cod = input("Ingrese el ID del usuario que desea editar: ")
        edit_user(cod)
        print()
        imprimirArchivo(mensaje)
        print()
        opcion = input("Ingrese su opción: ")

    while opcion.upper() == "D" and cont >= 1:
        id = input("\nIngrese el ID del usuario: ")
        if id in users:
            show_user(id)
            imprimirArchivo(mensaje)
            print()
            opcion = input("Ingrese su opción: ")
        else:
            print("El ID no coincide con un usuario registrado.")

    while opcion.upper() == "E" and cont >= 1:
        id = input("\nIngrese el ID del usuario: ")
        if id in users:
            delete_user(id)
            imprimirArchivo(mensaje)
            print()
            opcion = input("Ingrese su opción: ")

    if opcion == '':
        print("¡Hasta luego!")
        break
