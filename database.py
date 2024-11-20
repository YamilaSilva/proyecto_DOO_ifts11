from .str2dic import Str2Dic



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



class DB:
	def __init__(self):
		self.colecciones = {}

	def crear_coleccion(self, nombre_coleccion):
		if nombre_coleccion not in self.colecciones:
			self.colecciones[nombre_coleccion] = Coleccion(nombre_coleccion)

	def eliminar_coleccion(self, nombre_coleccion):
		if nombre_coleccion in self.colecciones:
			del self.colecciones[nombre_coleccion]

	def obtener_coleccion(self, nombre_coleccion):
		return self.colecciones.get(nombre_coleccion, None)

	def __srt__(self):
		return f"DB con {len(self.colecciones)} colecciones"
    
