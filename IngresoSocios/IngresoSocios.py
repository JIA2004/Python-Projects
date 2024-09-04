import random
import re

# Manejo del archivo usando 'with' para asegurar que se cierra correctamente
try:
    with open('mensaje.txt', 'r') as mensaje:
        opciones = ["A", "B", "C", "D", "E"]
        cont = 0
        users = {}

        def imprimirArchivo(archivo):
            archivo.seek(0)  # Reiniciar el puntero del archivo al inicio
            for line in archivo:
                print(line)

        def new_user():
            try:
                num = int(input("Ingrese la cantidad de usuarios que desea registrar: "))
            except ValueError:
                print("Error: Debe ingresar un número entero.")
                return

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

                users[codigo] = {
                    'Nombre': nombre,
                    'Apellido': apellido,
                    'Teléfono': tel,
                    'Correo': mail,
                }
                print()

        def show_user(id):
            if id not in users:
                print("Usuario no encontrado.")
                return
            
            print("\nInformación del Usuario")
            print("-----------------------")
            print(f"ID: {id}")
            for key, value in users[id].items():
                print(f"{key}: {value}")
            print()

        def edit_user(id):
            if id not in users:
                print("Usuario no encontrado.")
                return
            
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

        def delete_user(id):
            if id not in users:
                print("Usuario no encontrado.")
                return
            del users[id]
            print("Usuario eliminado con éxito.")

        def list_users(dict):
            if not dict:
                print("No hay usuarios registrados.")
                return

            print("\nUsuarios Registrados")
            print("--------------------")
            for key, value in dict.items():
                print(f"ID: {key}")
                for k, v in value.items():
                    print(f"{k}: {v}")
                print()

        # Imprimir el menú inicial
        imprimirArchivo(mensaje)
        print()

        while True:
            opcion = input("Ingrese su opción: ").upper()

            if opcion == "":
                print("¡Hasta luego!")
                break

            if opcion not in opciones:
                print(f"'{opcion}' no es una opción válida.")
                continue

            if opcion == "A":
                new_user()
                if users:
                    cont += 1
                print("¡Todos los usuarios fueron cargados con éxito!")

            elif opcion == "B" and cont >= 1:
                list_users(users)

            elif opcion == "C" and cont >= 1:
                list_users(users)
                cod = input("Ingrese el ID del usuario que desea editar: ")
                edit_user(cod)

            elif opcion == "D" and cont >= 1:
                id = input("Ingrese el ID del usuario: ")
                show_user(id)

            elif opcion == "E" and cont >= 1:
                id = input("Ingrese el ID del usuario: ")
                delete_user(id)

            elif cont <= 0:
                print("\nNo hay ningún usuario registrado en el sistema.")

            # Volver a imprimir el menú después de cada operación
            imprimirArchivo(mensaje)
            print()

except FileNotFoundError:
    print("Error: El archivo 'mensaje.txt' no se encuentra.")
except Exception as e:
    print(f"Error inesperado: {e}")