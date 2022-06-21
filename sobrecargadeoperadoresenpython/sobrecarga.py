from operator import truediv


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
    
    def __or__(self, b):
        if(self.costo > b.costo):
            return Producto(self.name, self.costo)
        else: 
            return Producto(b.name, b.costo)
    
    def __float__(self):
        return self.costo
    
    def __iadd__(self, b):
        self.costo =self.costo + float(b)
        return self
    
    def __gt__(self, b):
        if self.costo > b.costo:
            return True
        else:
            return False

print ("------")
manzana = Producto('Manzana Roja', 10500.1)
pera = Producto('pera pequeña', 3500.3)
print(manzana)
print(pera)
print ("------")
canasta = manzana + pera
print(canasta)
print ("------")
costoso = manzana | pera
print(costoso)
print ("------")
total = 5*float(manzana)
print(total)
print ("------")
pera += 2134.2
print(pera)
print ("------")
comparacion = pera < manzana
print(comparacion)
print ("------")