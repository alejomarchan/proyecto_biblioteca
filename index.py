import os
import re
import database as db

#Declaración de funciones de validación

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

def valida_isbn(isbn_par):
    """
    Funcion que recibe el por parámetro el código del libro (isbn_par)
    y valida si es correcto o no.
    Retorna False si la validación es correcta
    Retorne True si no pasa la validación
    """
    
    isbn_par = isbn_par.replace("-", "").replace(" ", "").upper();
    chars = list(re.sub("[- ]|^ISBN(?:-1[03])?:?", "", isbn_par))
    last = chars.pop()
    if len(chars) == 9:
        # Compute the ISBN-10 check digit
        val = sum((x + 2) * int(y) for x,y in enumerate(reversed(chars)))
        check = 11 - (val % 11)
        if check == 10:
            check = "X"
        elif check == 11:
            check = "0"
    else:
        # Compute the ISBN-13 check digit
        val = sum((x % 2 * 2 + 1) * int(y) for x,y in enumerate(chars))
        check = 10 - (val % 10)
        if check == 10:
            check = "0"
   
    if (str(check) == last):
            return True
    else:
        print("Dígito ISBN de comprobación inválido. Reingrese el valor")
        return False

    

    if regex.search(isbn_par):
        isbn_par = isbn_par.replace("-", "").replace(" ", "").upper();
        # Remove non ISBN digits, then split into a list
        chars = list(re.sub("[- ]|^ISBN(?:-1[03])?:?", "", isbn_par))
		# Remove the final ISBN digit from `chars`, and assign it to `last`
        last = chars.pop()

        if len(chars) == 9:
			# Compute the ISBN-10 check digit
            val = sum((x + 2) * int(y) for x,y in enumerate(reversed(chars)))
            check = 11 - (val % 11)
            if check == 10:
                check = "X"
            elif check == 11:
                check = "0"
        else:
			# Compute the ISBN-13 check digit
            val = sum((x % 2 * 2 + 1) * int(y) for x,y in enumerate(chars))
            check = 10 - (val % 10)
            if check == 10:
                check = "0"

        if (str(check) == last):
            return False
        else:
            print("Dígito ISBN de comprobación inválido. Reingrese el valor")
            return True
    else:
        print("ISBN Inválido")
        return True

def valida_cadena(cadena):
    if len(cadena.replace(" ", ""))>0:
        return True
    else:
        print("La cadena que ingresaste está vacía.")
        return False

#Definición de funciones de interacción        

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

#Definición de funciones del Menú

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
        5: "Eliminar Libro",
        6: "Volver al Menú Principal"
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
                libros_disponibles()
            if ele_conv == 2:
                libros_prestados()
            if ele_conv == 3:
                libros_ingreso()
            if ele_conv == 4:
                libros_actualiza()
            if ele_conv == 5:
                libros_baja()
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


#Definición de funciones de cada proceso

#Libros
def libros_disponibles():
    bbl = conn.tablas_bbl
    sql = 'select isbn, titulo, autor from '+bbl['db']+'.'+bbl['libros']+' where estado =%s and activo=%s'
    lista = [1,1]
    param = tuple(i for i in lista)
    conn.sql_query(sql,param)
    fet = conn.sql_fetchall()
    print ("{:^45}".format('Libros Disponibles'))
    print ("{:^20} {:<50} {:^10}".format('ISBN','TITULO','AUTOR'))
    for i in fet:
        print ("{:<20} {:<50} {:<10}".format(i[0], i[1], i[2]))
    input("\nPresione cualquier tecla para continuar...")
    menu_libros()

def libros_prestados():
    bbl = conn.tablas_bbl
    sql = 'select isbn, titulo, autor from '+bbl['db']+'.'+bbl['libros']+' where estado =%s'
    lista = [0]
    param = tuple(i for i in lista)
    conn.sql_query(sql,param)
    fet = conn.sql_fetchall()
    print ("{:^45}".format('Libros En Préstamo'))
    print ("{:^20} {:<50} {:^10}".format('ISBN','TITULO','AUTOR'))
    for i in fet:
        print ("{:<20} {:<50} {:<10}".format(i[0], i[1], i[2]))
    input("\nPresione cualquier tecla para continuar...")
    menu_libros()

def libros_ingreso():
    bbl = conn.tablas_bbl
    sql = 'insert into ' +bbl['db']+'.'+bbl['libros']+' (isbn,titulo,autor,estado,activo) values (%s,%s,%s,1,1)'
    flag_isbn = True
    flag_titulo = True
    flag_autor = True
    while flag_isbn:
        isbn = input('Ingrese ISBN: ')
        if valida_isbn(isbn):
            flag_isbn = False
        else:
            flag_isbn = True
    while flag_titulo:
        titulo = input('Ingrese titulo del libro: ')
        flag_titulo = valida_cadena(titulo)
    while flag_autor:
        autor = input('Ingrese autor del libro: ')
        flag_autor = valida_cadena(autor)
    
    lista = [isbn, titulo, autor]
    param = tuple(i for i in lista)
    conn.sql_query(sql,param)
    conn.sql_commit()
    menu_libros()
    
def libros_actualiza():
    bbl = conn.tablas_bbl
    sql = 'select isbn, titulo, autor, estado, activo from '+bbl['db']+'.'+bbl['libros']+' order by isbn'
    sql_update = 'update '+bbl['db']+'.'+bbl['libros']+' set titulo=%s, autor=%s, estado=%s, activo=%s where isbn=%s;'
    param = tuple()
    conn.sql_query(sql,param)
    fet = conn.sql_fetchall()
    print ("{:^45}".format('Libros En Préstamo'))
    print ("{:^20} {:<45} {:<25} {:^5} {:^5}".format('ISBN','TITULO','AUTOR', 'ESTADO', 'ACTIVO'))
    isbn_ingresados = []
    for i in fet:
        isbn_ingresados.append(i[0])
        print ("{:<20} {:<45} {:<25} {:^5} {:^5}".format(i[0], i[1], i[2], i[3], i[4]))
    isbn_act = input("\nSeleccione el ISBN a modificar: ")
    if isbn_act in isbn_ingresados:
        sql = 'select isbn, titulo, autor, estado, activo from '+bbl['db']+'.'+bbl['libros']+' order by isbn'
        param = tuple(i for i in isbn_act)
        conn.sql_query(sql,param)
        fet = conn.sql_fetchall()
        for i in fet:
            titulo_old = i[1]
            autor_old = i[2]
            estado_old = i[3]
            activo_old = i[4]
        print("Modifique el valor o solamente presione Enter si no desea cambiar ese campo")
        titulo_act = input("\nModificar Titulo: {}: ".format(titulo_old) or titulo_old)
        autor_act = input("Modificar autor: {}: ".format(autor_old) or autor_old)
        estado_act = input("Modificar Estado--> 1 para Activo, 0 para Inactivo: ".format(estado_old) or estado_old)
        activo_act = input("Modificar Activo--> 1 para Activo, 0 para Inactivo: ".format(activo_old) or activo_old)
        param = (titulo_act, autor_act, estado_act,activo_act,isbn_act)
        conn.sql_query(sql_update,param)
        conn.sql_commit()

    menu_libros()

def libros_baja():
    bbl = conn.tablas_bbl
    sql = 'select isbn, titulo, autor, estado, activo from '+bbl['db']+'.'+bbl['libros']+' where activo = 1 order by isbn'
    sql_update = 'update '+bbl['db']+'.'+bbl['libros']+' set activo=0 where isbn=%s;'
    param = tuple()
    conn.sql_query(sql,param)
    fet = conn.sql_fetchall()
    print ("{:^45}".format('Libros Activos'))
    print ("{:^20} {:<45} {:<25} {:^5} {:^5}".format('ISBN','TITULO','AUTOR', 'ESTADO', 'ACTIVO'))
    isbn_ingresados = []
    for i in fet:
        isbn_ingresados.append(i[0])
        print ("{:<20} {:<45} {:<25} {:^5} {:^5}".format(i[0], i[1], i[2], i[3], i[4]))
    isbn_act = input("\nSeleccione el ISBN a dar de baja: ")
    param = (isbn_act,)
    conn.sql_query(sql_update,param)
    conn.sql_commit()

    menu_libros()



if __name__ == "__main__":
    conn = db.ConDatabase()
    menu_general()
    #print(bbl['db'])
    #sql='select * from '+bbl['db']+'.'+bbl['usuarios']
    #lista = [] #['Alejandro',95783601]
    #param = tuple(i for i in lista)
    #salida = conn.sql_query(sql,param)
    #fet = conn.sql_fetchall()
    #print(len(fet[0]))
    #for i in fet:
    #    print(i[0],i[1],i[2],i[3],i[4],i[5])

    #isbn="978-3-16-148410-0"
    #valida_isbn(isbn)

    conn.close()