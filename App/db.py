import sqlite3

# Importamos la clase que nos permite crear los registros

'''
    @LD-OH==================================================
        Esta clase nos permite instanciar un modulo gestor
        de base de datos utilizando sqlite3
    ========================================================
'''

class DB_Control():
    # Metodo constructor
    def __init__(self, _db, _tabla):
        self.db = _db
        self.tabla = _tabla
        self.cnx = None
        self.cursor = None

        self.abrir_cnx()

    # Metodo para abrir conexion y crear cursor
    def abrir_cnx(self):
        self.cnx = sqlite3.connect(self.db)
        self.cursor = self.cnx.cursor()
        print("Conexion exitosa con la base de datos")


    # Metodo para cerrar la conexion
    def cerrar_cnx(self):
        self.cnx.close()
        print("se ha cerrado la conexion")

    # Metodo para crear base de datos
    def crear_tabla(self):
        try:
            self.cursor.execute(f'CREATE TABLE {self.tabla} (nombre VARCHAR(30), edad INTEGER, correo VARCHAR(30), ciudad VARCHAR(30), usuario VARCHAR(15), clave VARCHAR(15))')
            print("Tabla Creada con exito")
        
        except:
            print("Ya existe la tabla en la base de datos")
    
    # Leer informacion de la base, podemos seleccionar las columnas llenando data con las columnas deseadas
    # data = "nombre, edad, correo"
    def lectura(self, datos = "*"):
        self.cursor.execute(f"SELECT {datos} FROM {self.tabla}")

        data = self.cursor.fetchall()

        if(len(data)>0):
            return data
        else:
            return False
    
    # Registrando informacion en la base de datos
    def registrar(self, info):
   
        self.cursor.execute(f'INSERT INTO {self.tabla} VALUES("{info.nombre}", "{info.edad}", "{info.correo}", "{info.ciudad}", "{info.usuario}","{info.clave}")')
    
        # Se confirma el cambio
        self.cnx.commit()
        print("Nuevo registro agregado!!")

    
    # Creamos una funcion debusqueda
    def busqueda(self, columna, parametro):
        self.cursor.execute(f'SELECT*FROM {self.tabla} WHERE {columna} = "{parametro}"')
        data  = self.cursor.fetchall()

        if(len(data)>0):
            return True, data
        else:
            return False, None

    # Modificacion de elementos en la base
    def modificar(self, columna, parametro, mcolumna, ndato):
        self.cursor.execute(f'UPDATE {self.tabla} SET {mcolumna} = "{ndato}" WHERE {columna} = "{parametro}"')

        self.cnx.commit()
