import json

def registrar_usuario():
    nombre = input("Ingrese nombre: ")
    contraseña = input("Ingrese contraseña: ")

    with open("usuarios.json", "r") as archivo:
        base_datos = json.load(archivo)

    if nombre in base_datos:
        print("El usuario ya existe. Ingrese otro nombre de usuario")
        return

    base_datos[nombre] = contraseña

    with open("usuarios.json", "w") as archivo:
        json.dump(base_datos, archivo)

    print("¡Usuario registrado exitosamente!")

def mostrar_usuarios():
    with open("usuarios.json", "r") as archivo:
        base_datos = json.load(archivo)

    print("Lista de usuarios:")
    for nombre, contraseña in base_datos.items():
        print(f"{nombre} : {contraseña}")

def hacer_login():
    nombre = input("Ingrese su nombre de usuario: ")
    contraseña = input("Ingrese su contraseña: ")

    with open("usuarios.json", "r") as archivo:
        base_datos = json.load(archivo)

    if nombre not in base_datos:
        print("El usuario no existe")
        return

    if contraseña != base_datos[nombre]:
        print("La contraseña es incorrecta")
        return

    # Si el usuario y contraseña son correctos:
    print(f"Bienvenido {nombre}!")

while True:
    print("1) Registrar un nuevo usuario")
    print("2) Mostrar la lista de usuarios registrados")
    print("3) Hacer login")
    print("4) Salir")

    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        registrar_usuario()
    elif opcion == "2":
        mostrar_usuarios()
    elif opcion == "3":
        hacer_login()
    elif opcion == "4":
        break
    else:
        print("Opción inválida.")
