import os
import database as db

def despliega_menu(menu):
    for key, values in menu.items():
        print("({}) para \"{}\"".format(key, values))

def valida_numero(elemento):
    if elemento.isnumeric():
        return True
    else:
        os.system('cls')
        return False

def valida_eleccion(diccionario, elemento):
    print(type(elemento))
    if elemento in diccionario:
        return True
    else:
        os.system('cls')
        return False


def menu_general():
    os.system('cls')
    menu = {
        1: "Menú Libros",
        2: "Menú Usuarios",
        3: "Menú Préstamos",
        0: "Salir"
    }
    despliega_menu(menu)

    eleccion = input("Ingrese su eleccion: ")

    if not valida_numero(eleccion):
        os.system('cls')
        print("Eleccion errónea. Ingrese valor numérico correspondiente")
        menu_general()
    else:
        ele_conv = int(eleccion)
        if not valida_eleccion(menu,ele_conv):
            print("Eleccion errónea. Ingrese valor correspondiente")
            menu_general()
        else:
            print("Eleccion correcta {}".format(ele_conv))
            if ele_conv == 1:
                sub_menu_libros()
            if ele_conv == 2:
                sub_menu_usuarios()
            if ele_conv == 3:
                sub_menu_prestamo()
            else:
                exit

def sub_menu_libros():
    os.system('cls')
    menu = {
        1: "Libros Disponibles",
        2: "Libros En Préstamo",
        3: "Nuevo Libro",
        4: "Actualizar Libro",
        5: "Baja Libro"
    }
    despliega_menu(menu)
    eleccion = input("Ingrese su eleccion: ")
    if not valida_numero(eleccion):
        print("Eleccion errónea. Ingrese valor numérico correspondiente")
        sub_menu_libros()
    
def sub_menu_usuarios():
    os.system('cls')
    menu = {
        1: "Alta Cliente",
        2: "Consulta Cliente",
        3: "Actualizar Cliente",
        4: "Eliminar Cliente"
    }
    despliega_menu(menu)
    eleccion = input("Ingrese su eleccion:")
    if not valida_numero(eleccion):
        print("Eleccion errónea. Ingrese valor numérico correspondiente")
        sub_menu_libros()

def sub_menu_prestamo():
    os.system('cls')
    menu = {
        1: "Prestar Libro",
        2: "Registrar Devolución"
    }
    despliega_menu(menu)
    eleccion = input("Ingrese su eleccion:")
    if not valida_numero(eleccion):
        print("Eleccion errónea. Ingrese valor numérico correspondiente")
        sub_menu_libros()


if __name__ == "__main__":
    conn = db.ConDatabase()
    menu_general()
    conn.close()