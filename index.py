import os
import database as db

def despliega_menu(menu):
    """
    Toma como parámetro el diccionario menu y hace un print de sus elementos
    """
    for key, values in menu.items():
        print("({}) para \"{}\"".format(key, values))

def valida_numero(elemento):
    """
    Toma como parámetro la seleccion del usuario (elemento) y valida si es numérico
    """
    if elemento.isnumeric():
        return True
    else:
        os.system('cls')
        return False

def valida_eleccion(diccionario, elemento):
    """
    Toma como parámetros el diccionario del menú y la seleccion del usuario
    y devuelve como resultado True si el elemento pertenece a la clave del menú
    """
    print(type(elemento))
    if elemento in diccionario:
        return True
    else:
        os.system('cls')
        return False


def menu_general():
    """
    El menú general es invocado al inicio del programa.
    El mismo despliega los items principales a mostrar al administrador para su elección
    """
    
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
                menu_libros()
            if ele_conv == 2:
                menu_usuarios()
            if ele_conv == 3:
                menu_prestamo()
            else:
                exit

def menu_libros():
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
        os.system('cls')
        print("Eleccion errónea. Ingrese valor numérico correspondiente")
        menu_libros()
    else:
        ele_conv = int(eleccion)
        if not valida_eleccion(menu,ele_conv):
            print("Eleccion errónea. Ingrese valor correspondiente")
            menu_libros()
        else:
            print("Eleccion correcta {}".format(ele_conv))
            if ele_conv == 1:
                pass
            if ele_conv == 2:
                pass
            if ele_conv == 3:
                pass
            if ele_conv == 4:
                pass
            if ele_conv == 5:
                pass
            else:
                exit
    
def menu_usuarios():
    os.system('cls')
    menu = {
        1: "Alta Cliente",
        2: "Consulta Cliente",
        3: "Actualizar Cliente",
        4: "Eliminar Cliente"
    }
    despliega_menu(menu)
    eleccion = input("Ingrese su eleccion:")
    eleccion = input("Ingrese su eleccion:")
    if not valida_numero(eleccion):
        os.system('cls')
        print("Eleccion errónea. Ingrese valor numérico correspondiente")
        menu_usuarios()
    else:
        ele_conv = int(eleccion)
        if not valida_eleccion(menu,ele_conv):
            print("Eleccion errónea. Ingrese valor correspondiente")
            menu_usuarios()
        else:
            print("Eleccion correcta {}".format(ele_conv))
            if ele_conv == 1:
                pass
            if ele_conv == 2:
                pass
            if ele_conv == 3:
                pass
            if ele_conv == 4:
                pass
            else:
                exit

def menu_prestamo():
    os.system('cls')
    menu = {
        1: "Prestar Libro",
        2: "Registrar Devolución"
    }
    despliega_menu(menu)
    eleccion = input("Ingrese su eleccion:")
    if not valida_numero(eleccion):
        os.system('cls')
        print("Eleccion errónea. Ingrese valor numérico correspondiente")
        menu_prestamo()
    else:
        ele_conv = int(eleccion)
        if not valida_eleccion(menu,ele_conv):
            print("Eleccion errónea. Ingrese valor correspondiente")
            menu_prestamo()
        else:
            print("Eleccion correcta {}".format(ele_conv))
            if ele_conv == 1:
                pass
            if ele_conv == 2:
                pass
            else:
                exit


if __name__ == "__main__":
    conn = db.ConDatabase()
    menu_general()
    #ql='select * from biblioteca.usuarios'
    #lista = [] #['Alejandro',95783601]
    #param = tuple(i for i in lista)
    #salida = conn.sql_query(sql,param)
    #conn.ret_fetchall()
    conn.close()