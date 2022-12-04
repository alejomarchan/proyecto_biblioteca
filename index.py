import os
import re
import database as db
import time

#Declaración de funciones de validación

def despliega_menu(menu):
    """
    Toma como parámetro el diccionario (menu) y hace un print de sus elementos
    para que sean visulizadas las opciones correspondientes
    """
    for key, values in menu.items():
        print("({}) \"{}\"".format(key, values))

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
    match = re.search(r'^(\d{9})(\d|X)$', isbn_par)
    last = chars.pop()
    try:
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
    except Exception as e:
        print("No es un ISBN {}".format(e))
        return False
   
    if (str(check) == last):
            return True
    else:
        print("Dígito ISBN de comprobación inválido. Reingrese el valor")
        return False

def valida_cadena(cadena):
    if len(cadena.replace(" ", ""))>0:
        return False
    else:
        print("La cadena que ingresaste está vacía.")
        return True

def valida_dni_prestamo(dni, existencia):
    """
    Toma como parámetro la seleccion del usuario (elemento) y valida si es numérico
    """
    if existencia == "existe":
        sql_existe = "SELECT estado, COUNT(*) from {}.usuarios where dni=%s GROUP BY estado;".format(database)
        param = (dni,)
        conn.sql_query(sql_existe,param)
        fet = conn.sql_fetchall()
        row = len(fet)
        if row > 0:
            if fet[0]==0:
                print("Usuario Inactivo. No puede solicitar préstamos")
                return False
            else:
                return True
        else:
            print("No existe como Usuario este DNI")
            return False
    elif existencia=="prestamos":
        sql_existe = "SELECT COUNT(*) from {}.prestamos where dni=%s and devuelto = 0;".format(database)
        param = (dni,)
        conn.sql_query(sql_existe,param)
        fet = conn.sql_fetchall()
        row = int(fet[0][0])
        if row !=0:
            print("Usuario con préstamos activo. DEVUELVE EL ANTERIOR")
            return True
        else:
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
        1: "Menú disponibilidad",
        2: "Menú Libros",
        3: "Menú Socios",
        4: "Menú Préstamos",
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
                menu_disponibilidad()
            if ele_conv == 2:
                os.system('cls')
                menu_libros()
            if ele_conv == 3:
                os.system('cls')
                menu_socios()
            if ele_conv == 4:
                os.system('cls')
                menu_prestamo()
            else:
                exit


#Menú Disponibilidad
def menu_disponibilidad():
    sql = 'SELECT li.isbn, li.titulo, li.autor, coalesce(CONCAT("Prestado a ", us.nombre," DNI " , cast(us.dni AS char)), "Disponible") AS "Nombre" from ' + database + '.'+bbl['libros']+' li left JOIN ' + database + '.'+bbl['prestamos']+' pr ON (li.isbn=pr.ISBN AND pr.devuelto=0) LEFT JOIN ' + database + '.' + bbl['socios']+' us ON (us.dni=pr.dni) WHERE li.isbn = %s'
    isbn = input("Ingrese ISBN: ")
    param = (isbn,)
    conn.sql_query(sql,param)
    fet = conn.sql_fetchall()
    print ("{:^45}".format('Libros Disponibles'))
    print ("{:^20} {:^30} {:^20} {:^30}".format('ISBN','TITULO','AUTOR', 'DISPONIBILIDAD'))
    for i in fet:
        print ("{:^20} {:<30} {:^20} {:^30}".format(i[0], i[1], i[2], i[3]))
    input("\nPresione cualquier tecla para continuar...")
    menu_general()


#Menú Libros
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
    
def menu_socios():
    print("***** Menú socios *****")
    menu = {
        1: "Consulta Socios",
        2: "Alta Socio",
        3: "Actualizar Socio",
        4: "Eliminar Socio",
        5: "Volver al Menú Principal"
    }
    despliega_menu(menu)
    eleccion = solicita_eleccion()
    if not valida_numero(eleccion):
        os.system('cls')
        imprime_respuesta('no_numero')
        menu_socios()
    else:
        ele_conv = int(eleccion)
        if not valida_eleccion(menu,ele_conv):
            imprime_respuesta('no_eleccion')
            menu_socios()
        else:
            #print("Eleccion correcta {}".format(ele_conv))            
            if ele_conv == 1:
                menu_socios_disponibles()
            if ele_conv == 2:
                socios_ingreso()
            if ele_conv == 3:
                usuario_actualiza()
            if ele_conv == 4:
                usuario_baja()
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
                libros_prestamos()
            if ele_conv == 2:
                libros_devolucion()
            if ele_conv == 3:
                menu_general()
            else:
                exit


#Definición de funciones de cada proceso
#Libros
def libros_disponibles():
    bbl = conn.tablas_bbl
    sql = 'select isbn, titulo, autor from ' + database + '.'+bbl['libros']+' where estado =%s and activo=%s'
    print(sql)
    lista = [1,1]
    param = tuple(i for i in lista)
    conn.sql_query(sql,param)
    fet = conn.sql_fetchall()
    print ("{:^45}".format('Libros Disponibles'))
    print ("{:^20} {:<50} {:^10}".format('ISBN','TITULO','AUTOR'))
    for i in fet:
        print ("{:<20} {:<50} {:<10}".format(i[0], i[1], i[2]))
    input("\nPresione cualquier tecla para continuar...")
    os.system('cls')
    menu_libros()

def libros_prestados():
    bbl = conn.tablas_bbl
    sql = 'select isbn, titulo, autor from ' + database + '.'+bbl['libros']+' where estado =%s'
    lista = [0]
    param = tuple(i for i in lista)
    conn.sql_query(sql,param)
    fet = conn.sql_fetchall()
    print ("{:^45}".format('Libros En Préstamo'))
    print ("{:^20} {:<50} {:^10}".format('ISBN','TITULO','AUTOR'))
    for i in fet:
        print ("{:<20} {:<50} {:<10}".format(i[0], i[1], i[2]))
    input("\nPresione cualquier tecla para continuar...")
    os.system('cls')
    menu_libros()

def libros_ingreso():
    bbl = conn.tablas_bbl
    sql = 'insert into ' + database + '.'+bbl['libros']+' (isbn,titulo,autor,estado,activo) values (%s,%s,%s,1,1)'
    flag_isbn = True
    flag_titulo = True
    flag_autor = True
    while flag_isbn:
        isbn = input('Ingrese ISBN: ')
        if valida_isbn(isbn):
            isbn.upper()
            isbn = isbn.replace("-", "").replace(" ", "").replace("ISBN","").upper();
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
    sql = 'select isbn, titulo, autor, estado, activo from ' + database + '.'+bbl['libros']+' order by isbn;'
    sql_update = 'update ' + database + '.'+bbl['libros']+' set titulo=%s, autor=%s, estado=%s, activo=%s where isbn=%s;'
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
        sql = 'select isbn, titulo, autor, estado, activo from ' + database + '.'+bbl['libros']+' order by isbn;'
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
        estado_act = input("Modificar Estado. Actual en {}: Presione 1 para Activo, 0 para Inactivo: ".format(estado_old) or estado_old)
        activo_act = input("Modificar Activo. Actual en {}: Presione 1 para Activo, 0 para Inactivo: ".format(activo_old) or activo_old)
        param = (titulo_act, autor_act, estado_act,activo_act,isbn_act)
        conn.sql_query(sql_update,param)
        conn.sql_commit()

    menu_libros()

def libros_baja():
    bbl = conn.tablas_bbl
    sql = 'select isbn, titulo, autor, estado, activo from ' + database + '.'+bbl['libros']+' where activo = 1 order by isbn;'
    sql_update = 'update ' + database + '.'+bbl['libros']+' set activo=0 where isbn=%s;'
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

#socios
def menu_socios_disponibles():
    print("***** Menú socios *****")
    menu = {
        1: "Consulta Listado de Socios",
        2: "Consulta Socio por DNI",
        3: "Volver al Menú Anterior",
        4: "Volver al Menú Principal"
    }
    despliega_menu(menu)
    eleccion = solicita_eleccion()
    if not valida_numero(eleccion):
        os.system('cls')
        imprime_respuesta('no_numero')
        menu_socios()
    else:
        ele_conv = int(eleccion)
        if not valida_eleccion(menu,ele_conv):
            imprime_respuesta('no_eleccion')
            menu_socios()
        else:
            #print("Eleccion correcta {}".format(ele_conv))            
            if ele_conv == 1:
                socios_disponibles()
            if ele_conv == 2:
                socios_disponibles_dni()
            if ele_conv == 3:
                menu_socios()
            if ele_conv == 4:
                menu_general()
            else:
                exit

def socios_disponibles():
    bbl = conn.tablas_bbl
    sql = 'select dni, nombre, telefono, direccion, fecha_alta from ' + database + '.'+bbl['socios']+' where estado =%s;'
    lista = [1]
    param = tuple(i for i in lista)
    conn.sql_query(sql,param)
    fet = conn.sql_fetchall()
    print ("{:^45}".format('Socios Disponibles'))
    print ("{:^20} {:<20} {:^20} {:^20} {:^20}".format('DNI','NOMBRE','TELEFONO', 'DIRECCION', 'FECHA_ALTA'))
    for i in fet:
        print ("{:^20} {:<20} {:^20} {:^20} {:^20}".format(i[0], i[1], i[2], i[3], str(i[4])))
    input("\nPresione cualquier tecla para continuar...")
    os.system('cls')
    menu_socios()

def socios_disponibles_dni():
    bbl = conn.tablas_bbl
    sql = 'SELECT us.dni, us.nombre, us.direccion, li.titulo, pr.fecha_prestamo FROM ' + database + '.'+bbl['socios']+' us LEFT JOIN ' + database + '.'+bbl['prestamos']+ ' pr ON (us.dni=pr.dni AND pr.devuelto=0) left JOIN ' + database + '.'+bbl['libros']+' li ON (li.isbn=pr.ISBN) WHERE us.dni=%s;'
    flag_dni = True
    while flag_dni:
        dni = input('Ingrese DNI: ')
        flag_dni = valida_cadena(dni)
    lista = [dni]
    param = tuple(i for i in lista)
    conn.sql_query(sql,param)
    fet = conn.sql_fetchall()
    print ("{:^45}".format('Socios Disponibles'))
    for i in fet:
        print ("{:^15} {:<15} {:^15} {:^20}".format('DNI','NOMBRE', 'DIRECCION' ,'LIBROS'))
        print("{:^15} {:<15} {:^15} {:^20}".format(i[0], i[1], i[2],str(i[3] or "Sin Préstamos Activos")))
    input("\nPresione cualquier tecla para continuar...")
    os.system('cls')
    menu_socios()    

def socios_ingreso():
    bbl = conn.tablas_bbl
    sql = 'insert into ' + database + '.'+bbl['socios']+' (dni,nombre,telefono,direccion,fecha_alta, estado) values (%s,%s,%s,%s,%s,1);'
    flag_dni = True
    flag_nombre = True
    flag_telefono = True
    flag_direccion = True
    fecha_alta = time.strftime('%Y-%m-%d')
    while flag_dni:
        dni = input('Ingrese DNI: ')
        flag_dni = valida_cadena(dni)
    while flag_nombre:
        nombre = input('Ingrese Nombre: ')
        flag_nombre = valida_cadena(nombre)
    while flag_telefono:
        telefono = input('Ingrese telefono: ')
        flag_telefono = valida_cadena(telefono)
    while flag_direccion:
        direccion = input('Ingrese Dirección: ')
        flag_direccion = valida_cadena(direccion)
    
    lista = [dni, nombre, telefono, direccion, fecha_alta]
    param = tuple(i for i in lista)
    conn.sql_query(sql,param)
    conn.sql_commit()
    menu_socios()

def usuario_actualiza():
    bbl = conn.tablas_bbl
    sql = 'select dni, nombre, telefono, direccion, estado from ' + database + '.'+bbl['socios']+' order by dni;'
    sql_update = 'update ' + database + '.'+bbl['socios']+' set nombre=%s, telefono=%s, direccion=%s, fecha_actualizacion=%s, estado=%s where dni=%s;'
    fecha_modificacion = time.strftime('%Y-%m-%d')
    param = tuple()
    conn.sql_query(sql,param)
    fet = conn.sql_fetchall()
    print ("{:^45}".format('socios a modificar'))
    print ("{:^20} {:<20} {:<20} {:^20} {:^20}".format('DNI','NOMBRE','TELEFONO', 'DIRECCION', 'ACTIVO'))
    socios_ingresados = []
    for i in fet:
        socios_ingresados.append(i[0])
        print ("{:<20} {:<20} {:<20} {:^20} {:^20}".format(i[0], i[1], i[2], i[3], i[4]))
    dni_act = int(input("\nSeleccione el DNI a modificar: "))
    if dni_act in socios_ingresados:
        sql = 'select nombre, telefono, direccion, estado from ' + database + '.'+bbl['socios']+' where dni=%s order by dni;'
        param = (dni_act,)
        conn.sql_query(sql,param)
        fet = conn.sql_fetchall()
        for i in fet:
            nombre_old = i[0]
            telefono_old = i[1]
            direccion_old = i[2]
            estado_old = i[3]
        print("Modifique el valor o solamente presione Enter si no desea cambiar ese campo\n")
        nombre_act = input("Modificar Nombre: {}: ".format(nombre_old)) or nombre_old
        telefono_act = input("Modificar Telefono: {}: ".format(telefono_old)) or telefono_old
        direccion_act = input("Modificar Direccion: {}:".format(direccion_old)) or direccion_old
        estado_act = input("Modificar Activo--> 1 para Activo, 0 para Inactivo: ".format(estado_old)) or estado_old
        param = (nombre_act, telefono_act, direccion_act,fecha_modificacion,estado_act,dni_act)
        conn.sql_query(sql_update,param)
        conn.sql_commit()
    menu_socios()
    
def usuario_baja():
    bbl = conn.tablas_bbl
    sql = 'select dni, nombre, telefono, direccion, estado from ' + database + '.'+bbl['socios']+' order by dni;'
    sql_update = 'update ' + database + '.'+bbl['socios']+' set estado=0 where dni=%s;'
    param = tuple()
    conn.sql_query(sql,param)
    fet = conn.sql_fetchall()
    print ("{:^45}".format('socios Activos'))
    print ("{:^20} {:<20} {:<20} {:^20} {:^20}".format('DNI','NOMBRE','TELEFONO', 'DIRECCION', 'ESTADO'))
    dni_ingresados = []
    for i in fet:
        dni_ingresados.append(i[0])
        print ("{:<20} {:<45} {:<25} {:^5} {:^5}".format(i[0], i[1], i[2], i[3], i[4]))
    dni_act = input("\nSeleccione el DNI a dar de baja: ")
    param = (dni_act,)
    conn.sql_query(sql_update,param)
    conn.sql_commit()
    menu_socios()

#Préstamos
def libros_prestamos():
    intentos = 3
    bbl = conn.tablas_bbl
    #Querys de actualización
    sql_insert_prest = 'insert into ' + database + '.'+bbl['prestamos']+' (id_prestamo, dni, ISBN,fecha_prestamo, devuelto) values (%d, %d, %s, %s,%d);'
    sql_update_prest_libro = 'update ' + database + '.'+bbl['libros']+' set estado =0 where isbn=%s;'
    fecha = time.strftime('%Y-%m-%d')
    #Querys de consulta de los libros y el id
    sql_libros = 'select isbn, titulo from ' + database + '.'+bbl['libros']+' where estado =%s and activo=%s;'
    sql_max = 'select nvl(max(id_prestamo),0) + 1 from ' + database + '.'+bbl['prestamos']
    param = tuple()
    conn.sql_query(sql_max,param)
    fet = conn.sql_fetchall()
    id_prestamos = fet[0][0]
    lista = [1,1]
    param = tuple(i for i in lista)
    conn.sql_query(sql_libros,param)
    fet = conn.sql_fetchall()
    libros_disponibles = []
    flag_dni = True
    cont_flag = 0
    while flag_dni:
        dni = input("Ingrese dni: ")
        for i in fet:
            libros_disponibles.append(i[0])
        if valida_dni_prestamo(dni, "existe"):
            print("Usuario existe en la Base de Datos")
            if valida_dni_prestamo(dni, "prestamos"):
                print("Usuario con Préstamos activo, no se puede")
            else:
                print("Puede pedir cualquier libro disponible")
                flag_dni = False
        cont_flag = cont_flag+1
        if cont_flag>2 and flag_dni:
            print("Cantidad de intentos erróneos con el dni: ")
            menu_prestamo()
        if cont_flag>0 and flag_dni>0:
            print("Le quedan {} intentos".format(intentos-cont_flag))
    flag_isbn = True
    cont_flag = 0
    while flag_isbn:
        isbn = input("Ingrese ISBN del libro a solicitar: ")
        flag_isbn = False
        if isbn not in libros_disponibles:
            print("Libro no existe")
            flag_isbn = False
        cont_flag = cont_flag+1
        if cont_flag>2 and flag_isbn:
            print("Cantidad de intentos erróneos con el ISBN")
            menu_prestamo()
        if cont_flag>0 and flag_isbn>0:
            print("Le quedan {} intentos".format(intentos-cont_flag))
            menu_prestamo()
    param = (id_prestamos, dni, isbn, fecha,0)
    conn.sql_query(sql_insert_prest,param)
    param = (isbn,)
    conn.sql_query(sql_update_prest_libro,param)
    conn.sql_commit()
    print("exitoso")
    menu_prestamo()

def libros_devolucion():
    intentos = 3
    bbl = conn.tablas_bbl
    #Querys de actualización
    fecha = time.strftime('%Y-%m-%d')
    sql_update_prest_libro = 'UPDATE ' + database + '.'+bbl['libros']+ ' a JOIN ' + database + '.'+bbl['prestamos'] + ' b ON (a.isbn = b.isbn) SET a.estado=1, b.devuelto = 1,  b.fecha_devolucion = %s WHERE b.dni = %d AND b.devuelto = 0;'
    sql_libros = 'select dni from ' + database + '.'+bbl['prestamos']+' where devuelto=0;'
    param = tuple()
    conn.sql_query(sql_libros,param)
    libros_dni_prestados = []
    fet = conn.sql_fetchall()
    for i in fet:
            libros_dni_prestados.append(i[0])
    
    print(libros_dni_prestados)
    cont_flag = 0
    flag_isbn = True
    while flag_isbn:
        dni = int(input("Ingrese DNI del usuario: "))
        if not valida_dni_prestamo(dni, "existe"):
            print("El usuario ingresado no existe")
        else:
            flag_isbn = False
            if dni not in libros_dni_prestados:
                print("Este usuario no tiene préstamos. Reingrese DNI")
                flag_isbn = True
            cont_flag = cont_flag+1
        if cont_flag>2 and flag_isbn:
            print("Cantidad de intentos erróneos con el DNI")
            menu_prestamo()
        if cont_flag>0 and flag_isbn>0:
            print("Le quedan {} intentos".format(intentos-cont_flag))
            flag_isbn = True
    param = (fecha, dni)
    conn.sql_query(sql_update_prest_libro,param)
    conn.sql_commit()
    menu_prestamo()

if __name__ == "__main__":
    database='biblioteca'
    conn = db.ConDatabase()
    if not conn.buscarDatabase(database):
        os.system('cls')
        print('Ingrese Nombre de Base de Datos a crear. Por default es {}'.format(database))
        new_database=str(input("Si solamente presionas enter queda {} como database: ".format(database)) or database)
        print("No Existe la base de datos {} y se crea".format(new_database))
        conn.createDatabase(new_database)
        database=new_database
        input("\nPresione cualquier tecla para continuar...")
    bbl = conn.tablas_bbl
    os.system('cls')
    menu_general()
    conn.close()