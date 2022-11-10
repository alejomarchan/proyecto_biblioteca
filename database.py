import mariadb
import json

class ConDatabase:
    def __init__(self):
        with open('./conf/conf_general.json', 'r') as conf_file:
            config = json.load(conf_file)
        conn_params= {
            "user" : config["CONFIG"]["USER"],
            "password" : config["CONFIG"]["PASS"],
            "host" : config["CONFIG"]["HOST"],
            "port" : config["CONFIG"]["PORT"]
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

    def ret_fetchall(self):
        for i in self.cur.fetchall():
            print("Pasando")
            print(i)

    def sql_query(self, consulta, parametros):
        try:
            self.cur.execute(consulta,parametros)
            return self.cur
        except mariadb.Error as e:
            print(f"Error: {e}")