#clase str2dic
schema = 'Nombre,Apellido,Edad,Mail'
linea = 'Yamila,Silva,29,yamilaksilva1@gmail.com'

class SchemaError(Exception):
    def __init__(self, message):
        self.message = message
        super(). __init_ (message)


class Str2Dic():
    def __init__(self, schema: str, separator=';'):
        if len(schema) == 0:
            raise SchemaError("El schema esta vacío")
        self.schema = schema.split(separator)
        self.separator = separator
    def convert(self, row):
        linea = row.split(self.separator)
        if len(linea) == len(self.schema):
            i = 0
            d = {}
            while i < len(linea):
                d[self.schema[i]] = linea[i]
                i += 1
            return d
        else:
            raise SchemaError("Los campos de la fila no concuerdan con el schema")
        

# o = Str2Dic(schema)
# try:
#     d = o.convert(linea)
#     print(d)
# except SchemaError as e:
#     print("Falló algo en el schema", e)