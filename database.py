import csv_files
from str2dic import *



#clase documento
class Documento:
    def __init__ (self, id, contenido=None):
        self.id = id
        self.contenido = contenido if contenido is not None else {}
    
    def obtener_valor(self, clave):
        return self.contenido.get(clave, None)
    
    def modificar_valor(self, clave, valor):
        self.contenido[clave] = valor

    def __str__(self):
        return f"Documento(id={self.id}, contenido={self.contenido})"
    
#clase coleccion
class Coleccion:
    def __init__(self, nombre):
        self.nombre = nombre
        self.documentos = {}

    def añadir_documento(self, documento):
        self.documentos[documento.id] = documento

    def eliminar_documento(self, id_documento):
        if id_documento in self.documentos:
            del self.documentos[id_documento]
    
    def buscar_documento(self, id_documento):
        return self.documentos.get(id_documento, None)

    def __str__(self):
        return f"Coleccion {self.nombre} con {len(self.documentos)} documentos"

    def listar_documentos(self):
        total = []
        for i in self.documentos:
            total.append(self.documentos[i])
        return total
          

class DB:
    def __init__(self, nombre=None):
        self.colecciones = {}
        self.nombre = nombre
        

    def crear_coleccion(self, nombre_coleccion):
        if nombre_coleccion not in self.colecciones:
            self.colecciones[nombre_coleccion] = Coleccion(nombre_coleccion)

    def eliminar_coleccion(self, nombre_coleccion):
        if nombre_coleccion in self.colecciones:
            del self.colecciones[nombre_coleccion]

    def obtener_coleccion(self, nombre_coleccion):
        return self.colecciones.get(nombre_coleccion, None)

    def __srt__(self):
        return f"DB (nombre={self.nombre}, con {len(self.colecciones)} colecciones"

    def importar_csv(self, nombre_coleccion, path):
        coleccion = self.obtener_coleccion(nombre_coleccion)
        if not coleccion:
            raise ValueError(f"La colección '{nombre_coleccion}' no existe.")
        f = open("csv_files/bdatos.csv", "rt")
        try:
            with open(path, 'r') as f:
                schema = f.readline().replace("\n", "")
                parser = Str2Dic(schema)
                col = self.obtener_coleccion(self)  

        except FileNotFoundError:
            raise FileNotFoundError(f"El archivo '{path}' no fue encontrado. Verifica la ruta.")
        # for idx, row in enumerate(f, start=1):
        #         contenido = parser.convert(row.strip())
        #         documento = Documento(id=idx, contenido=contenido)
        #         coleccion.añadir_documento(documento)        
       
