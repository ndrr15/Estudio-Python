class Producto:
    def __init__(self, name, costo):
        self.name = name
        self.costo = costo
        
    def __str__(self) :
        return 'Producto: '+ self.name + ' cuesta: $'+ str(self.costo)
    
    def __add__(self, b):
        tempN = self.name + ', '+b.name
        tempoC = self.costo + b.costo
        return Producto(tempN, tempoC)

manzana = Producto('Manzana Roja', 10500)
pera = Producto('pera pequeña', 3500)
# print(manzana)
# print(pera)

canasta = manzana + pera
print(canasta)