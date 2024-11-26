from str2dic import Str2Dic

class importarCSV:
    def importar_csv(self, nombre_coleccion, path):
        coleccion = self.obtener_coleccion(nombre_coleccion)
        if not coleccion:
            raise ValueError(f"La colección '{nombre_coleccion}' no existe.")
        
        try:
            with open("csv_files/bdatos.csv", 'r') as f:
                schema = f.readline().replace("\n", "")
                parser = Str2Dic(schema)
                col = self.obtener_coleccion(self)  

        except FileNotFoundError:
            raise FileNotFoundError(f"El archivo '{path}' no fue encontrado. Verifica la ruta.")
f = open("csv_files/bdatos.csv", "rt")

schema = f.readline().replace("\n", "")
parser= Str2Dic(schema)

print(schema)

while True:
    row = f.readline().replace("\n", "")
    if not row:
        break
    print(row)


