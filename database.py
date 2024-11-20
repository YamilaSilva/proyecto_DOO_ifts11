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
    
#clase str2dic
schema = 'Nombre,Apellido,Edad,Mail'
row = 'Yamila,Silva,29,yamilaksilva1@gmail.com'

class SchemaError(Exception):
    def __init__(self, message):
        self.message = message
        super(). __init_ (message)


class Str2Dic():
    def __init__(self, schema, separator=','):
        if len(schema) == 0:
            raise SchemaError("El schema esta vacío")
        self.schema = schema.split(separator)
        self.separator = separator
    def convert(self, row):
        tmp = row.split(self.separator)
        if len(tmp) == len(self.schema):
            i = 0
            d = {}
            while i < len(tmp):
                d[self.schema[i]] = tmp[i]
                i += 1
            return d
        else:
            raise SchemaError("Los campos de la fila no concuerdan con el schema")
        

o = Str2Dic(schema)
try:
    d = o.convert(row)
    print(d)
except SchemaError as e:
    print("Falló algo en el schema", e)