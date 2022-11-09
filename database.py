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
        self.conn = None
        try:
            print("Se va iniciar la conexión a la Base de Datos...")
            self.conn = mariadb.connect(**conn_params)
            print("Se estableció Conexión!")
            self.cur = self.conn.cursor()
        except mariadb.DatabaseError as err:
            print("Hubo un error en la conexión --> : {}".format(err))
        else:
            print("Connection established")
      
    def close(self):
        if self.conn:
            print("Cerrando sesión")
            self.conn.close()

    def sql_query(self, consulta):
        try:
            print(self.cur)
            salida = self.cur.execute(consulta)
            return salida
        except mariadb.Error as e:
            print(f"Error: {e}")