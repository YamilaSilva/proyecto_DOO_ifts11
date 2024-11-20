
#line0 = "nombre, email, telefono, edad"
#keys = line0.split(",")
#split separa el texto por cada vez que encuentra la ","

#line1 = "yamila, yamilaksilva1@gmail.com, 1122334455, 29"
#values = line1.split(",")
#if len(keys) == len(values):
#    print(keys)
#    print(values)
#    d = {}



class Str2doc(object):
    def __init__(self, keysStr, separator = ","):
        self.separator = separator
        self.keys = keysStr.split(separator)
    def convert(self, line):
        values = line.split(self.separator)
        if len(values) == len(self.keys):
            d = {}
            i = 0
            while i < len(values):
                key = self.keys[i]
                val = values[i]
                d[key] = val
                i = i + 1
            return d



s2d = Str2doc("nombre, email, telefono, edad")
print(s2d.keys)
print(s2d.convert("yamila, yamilaksilva1@gmail.com, 1122334455, 29"))
