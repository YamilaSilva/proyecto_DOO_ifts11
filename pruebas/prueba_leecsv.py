from main import Str2Dic

f = open("csv_files/bdatos.csv", "rt")

schema = f.readline().replace("\n", "")
parser= Str2Dic(schema)

print(schema)

while True:
    row = f.readline().replace("\n", "")
    if not row:
        break
    print(row)


