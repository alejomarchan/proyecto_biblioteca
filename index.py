import os
import database as db

def despliega_menu(menu):
    """
    Toma como parámetro el diccionario (menu) y hace un print de sus elementos
    para que sean visulizadas las opciones correspondientes
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
    Toma como parámetros el diccionario (menu) y la seleccion del usuario (elemento)
    y devuelve como resultado True si el elemento pertenece a la clave del menú
    """
    if elemento in diccionario:
        os.system('cls')
        return True
    else:
        os.system('cls')
        return False

def solicita_eleccion():
    """
    Devuelve como resultado el input del usuario
    """
    eleccion = input("Ingrese su eleccion: ")
    return eleccion

def imprime_respuesta(flag):
    """
    Funcion que devuelve al usuario los comentarios de su elección si es errónea
    Toma como parámetro una cadena (flag) y dependiendo, del error, genera el print
    """
    if flag == 'no_numero':
        print("No elegiste un número. Ingrese valor numérico!!!")
    elif flag == 'no_eleccion':
        print("Tu elección no existe en este listado. Ingrese valor correspondiente")
    else:
        print("No tenemos respuesta para esto :D")



def menu_general():
    """
    El menú general es invocado al inicio del programa.
    El mismo despliega los items principales a mostrar al usuario para su elección
    """
    print("***** Menú General *****")
    menu = {
        1: "Menú Libros",
        2: "Menú Usuarios",
        3: "Menú Préstamos",
        0: "Salir"
    }
    #Pasa por parámetro el diccionario con los elementos del respectivo Menú
    despliega_menu(menu)

    eleccion = input("Ingrese su eleccion: ")

    if not valida_numero(eleccion):
        os.system('cls')
        imprime_respuesta('no_numero')
        menu_general()
    else:
        ele_conv = int(eleccion)
        if not valida_eleccion(menu,ele_conv):
            print("Eleccion errónea. Ingrese valor correspondiente")
            menu_general()
        else:
            #print("Eleccion correcta {}".format(ele_conv))
            if ele_conv == 1:
                os.system('cls')
                menu_libros()
            if ele_conv == 2:
                os.system('cls')
                menu_usuarios()
            if ele_conv == 3:
                os.system('cls')
                menu_prestamo()
            else:
                exit

def menu_libros():
    print("***** Menú Libros *****")
    menu = {
        1: "Libros Disponibles",
        2: "Libros En Préstamo",
        3: "Ingreso Nuevo Libro",
        4: "Actualizar Libro",
        5: "Baja Libro",
        6: "Volver al Menú Principañ"
    }
    despliega_menu(menu)
    eleccion = solicita_eleccion()
    if not valida_numero(eleccion):
        os.system('cls')
        imprime_respuesta('no_numero')
        menu_libros()
    else:
        ele_conv = int(eleccion)
        if not valida_eleccion(menu,ele_conv):
            imprime_respuesta('no_eleccion')
            menu_libros()
        else:
            #print("Eleccion correcta {}".format(ele_conv))
            if ele_conv == 1:
                print("libros disponibles")
            if ele_conv == 2:
                print("libros en préstamo")
            if ele_conv == 3:
                print("Ingreso Nuevo libro")
            if ele_conv == 4:
                print("Actualizar libro")
            if ele_conv == 5:
                print("Dar Baja de libro")
            if ele_conv == 6:
                menu_general()
            else:
                exit
    
def menu_usuarios():
    print("***** Menú Usuarios *****")
    menu = {
        1: "Alta Cliente",
        2: "Consulta Cliente",
        3: "Actualizar Cliente",
        4: "Eliminar Cliente",
        5: "Volver al Menú Principal"
    }
    despliega_menu(menu)
    eleccion = solicita_eleccion()
    if not valida_numero(eleccion):
        os.system('cls')
        imprime_respuesta('no_numero')
        menu_usuarios()
    else:
        ele_conv = int(eleccion)
        if not valida_eleccion(menu,ele_conv):
            imprime_respuesta('no_eleccion')
            menu_usuarios()
        else:
            #print("Eleccion correcta {}".format(ele_conv))
            if ele_conv == 1:
                pass
            if ele_conv == 2:
                pass
            if ele_conv == 3:
                pass
            if ele_conv == 4:
                pass
            if ele_conv == 5:
                menu_general()
            else:
                exit

def menu_prestamo():
    print("***** Menú Préstamos *****")
    menu = {
        1: "Prestar Libro",
        2: "Registrar Devolución",
        3: "Volver al Menú Principal"
    }
    despliega_menu(menu)
    eleccion = solicita_eleccion()
    if not valida_numero(eleccion):
        os.system('cls')
        imprime_respuesta('no_numero')
        menu_prestamo()
    else:
        ele_conv = int(eleccion)
        if not valida_eleccion(menu,ele_conv):
            imprime_respuesta('no_eleccion')
            menu_prestamo()
        else:
            #print("Eleccion correcta {}".format(ele_conv))
            if ele_conv == 1:
                pass
            if ele_conv == 2:
                pass
            if ele_conv == 3:
                menu_general()
            else:
                exit


if __name__ == "__main__":
    conn = db.ConDatabase()
    #menu_general()
    bbl = conn.tablas_bbl
    print(bbl['db'])
    sql='select * from '+bbl['db']+'.'+bbl['usuarios']
    lista = [] #['Alejandro',95783601]
    param = tuple(i for i in lista)
    salida = conn.sql_query(sql,param)
    fet = conn.sql_fetchall()
    for i in fet:
        print(i[0],i[1],i[2],i[3],i[4],i[5])


    conn.close()