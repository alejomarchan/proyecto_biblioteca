import mariadb
import json
import time

class ConDatabase:
    def __init__(self):
        with open('./conf/conf_general.json', 'r') as conf_file:
            config = json.load(conf_file)
        self.conn_params= {
            "user" : config["CONFIG"]["USER"],
            "password" : config["CONFIG"]["PASS"],
            "host" : config["CONFIG"]["HOST"],
            "port" : config["CONFIG"]["PORT"]
        }
        self.tablas_bbl= {
            "db" : config["BD"]["BD"],
            "socios" : config["BD"]["PARTNER"],
            "libros" : config["BD"]["BOOKS"],
            "prestamos" : config["BD"]["LOANS"]
        }
        fd = open('./conf/ddl_biblioteca_export.sql', 'r')
        sqlFile = fd.read()
        fd.close()

        # all SQL commands (split on ';')
        self.sqlCommands = sqlFile.split(';')

        #global conn
        #Configuracion de la conexión a Base de Datos
        self.conn = None
        try:
            print("Se va iniciar la conexión a la Base de Datos...")
            self.conn = mariadb.connect(**self.conn_params)
            print("Se estableció Conexión!")
            self.cur = self.conn.cursor()
        except mariadb.DatabaseError as err:
            print("Hubo un error en la conexión --> : {}".format(err))
        else:
            print("Connection established")

    def buscarDatabase(self,nombre):
        """Funcion que busca si la base de datos nombre existe en Mysql
                    Parameters
                    ----------
                    nombre : str
                        Es el nombre es el esquema de la Base de Datos que queremos
                        revisar si existe en Mariadb
                    Return
                    ----------
                        True si la Base de Datos existe
                        False si la Base de Datos no existe
                    """
        print("Ingresando en BuscarDatabase buscando {}".format(nombre))
        self.cur.execute("show databases;")
        buscur = self.sql_fetchall()
        while True:
            try:
                for row in buscur:
                    if nombre.lower() in row:
                        return True
                return False
            except StopIteration:
                return False
                break

    def createDatabase(self,nombre):
        """Funcion que crea la base de datos en Mysql
            Parameters
            ----------
            nombre : str
                Es el nombre que se le asigna a la base de datos cuando es creada"""
        #exis = False
        sql = "CREATE DATABASE {}".format(nombre)
        #buscarDatabase(db,nombre)
        #if not buscarDatabase(nombre):
        if not self.buscarDatabase(nombre):
            self.cur.execute(sql)
            print("Base de datos {} Creada con exito".format(nombre))
            self.cur.execute("use {}".format(nombre))
            for sql_tables in self.sqlCommands:
            # This will skip and report errors
            # For example, if the tables do not yet exist, this will skip over
            # the DROP TABLE commands
                try:
                    print(sql_tables)
                    self.cur.execute(sql_tables)
                except mariadb.Error as e:
                    print("Command skipped por error: {}. Query".format(e,sql_tables))

    def dropDatabase(self,nombre):
        sql = 'drop database if exists ' + nombre
        try:
            self.cur.execute(sql)
        except mariadb.Error as e:
             print("Error en Drop: {}.".format(nombre))
        
      
    def close(self):
        if self.conn:
            print("Cerrando sesión")
            self.conn.close()

    def ret_fetchall(self):
        for i in self.cur.fetchall():
            print("Pasando")
            print(i)

    def sql_fetchall(self):
        return self.cur.fetchall()

    def sql_query(self, consulta, parametros):
        try:
            self.cur.execute(consulta,parametros)
            return self.cur
        except mariadb.Error as e:
            print(f"Error en ejecución: {e}")
    
    def sql_commit(self):
        self.conn.commit()

    def timer(self, t):  
        while t:
            mins, secs = divmod(t, 60)
            timer = 'Saliendo del sistema en {:02d} seg'.format(secs)
            print(timer, end="\r")
            time.sleep(1)
            t -= 1