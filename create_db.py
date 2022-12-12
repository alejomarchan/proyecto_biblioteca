import database as db
import os

def creaDB():
    os.system('cls')
    print('Ingrese Nombre de Base de Datos a crear. Por default es {}'.format(database))
    new_database=str(input("Si solamente presionas enter queda {} como database: ".format(database)) or database)
    print("Se crea".format(new_database))
    conn.createDatabase(new_database)
    database=new_database

conn = db.ConDatabase()
database = conn.tablas_bbl['db']
bbl = conn.tablas_bbl

if not conn.buscarDatabase(database):
    creaDB()
    input("\nPresione cualquier tecla para continuar...")
else:
    os.system('cls')
    flag_db = True
    print('La Base de datos {} ya existe.'.format(database))
    respuestas = ['s','n']
    while flag_db:
        resp = str(input('Desea recrearla de todas formas? s/N ')).lower()
        if resp in respuestas:
            if resp=='s':
                print("Base de datos dropeada")
                conn.dropDatabase(database)
                creaDB()
                print("Base de datos {} recreada".format(database))
                input("\nPresione cualquier tecla para continuar...")
            else:
                t=3
                conn.timer(t)
                exit
            
            flag_db = False
        else:
            print("Elección errónea, escoja s para sí o n para no")