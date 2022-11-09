import mariadb

class ConDatabase:
    def __init__(self):
        conn_params= {
            "user" : "root",
            "password" : "admin",
            "host" : "127.0.0.1",
            "port" : 3308
        }
        #global conn
        #Configuracion de la conexión a Base de Datos
        MYSQL_HOST = 'localhost'
        MYSQL_USER = 'root'
        MYSQL_PASSWORD = '1234'
        MYSQL_DB = 'abl_telefonica'
        self.conn = None
        try:
            print("Se va iniciar la conexión a la Base de Datos...")
            self.conn = mariadb.connect(**conn_params)
            print("Se estableció Conexión!")
        except mariadb.DatabaseError as err:
            print("Hubo un error en la conexión --> : {}".format(err))
        else:
            print("Connection established")

    def connection(self):
        return self.conn
      
    def close(self):
        if self.conn:
            print("Cerrando sesión")
            self.conn.close()