class Punto():
    #Metodo que define como crear un punto
     def __init__(self,numero1,numero2):
         self.numero1=numero1
         self.numero2=numero2

p= Punto(2,8)
print(p.numero1)
print(p.numero2)

class Vuelo():
    def __init__(self,numero,capacidad):
        self.capacidad=capacidad
        self.numero=numero
        self.pasajero=[]

    def agregar_pasajero(self, nombre):
        if not self.asientos_disponibles():
            return False
        self.pasajero.append(nombre)
        return True

    def asientos_disponibles(self):
        return self.capacidad - len (self.pasajero)

vuelo147 = Vuelo(147,2)
print(vuelo147.capacidad)
print(vuelo147.numero)
vuelo147.agregar_pasajero("juan carlos")
print(vuelo147.pasajero)
vuelo147.agregar_pasajero("juan3 carlos")
print(vuelo147.pasajero)
vuelo147.agregar_pasajero("juan4 carlos")
print(vuelo147.pasajero)
print(vuelo147.asientos_disponibles())

cuadrado = lambda x: x*x
print(cuadrado(5))

personas = [
    {"nombre": "harry", "casa":"xGryffindor"},
    {"nombre": "cho", "casa":"Ravebclaw"}
]

def f(unaPersona):
    return unaPersona["nombre"]

personas.sort(key=lambda unaPersona: unaPersona["casa"])
#personas.sort(key=f)

print(personas)

ejemploDiccionario = { 
   "clase":{ 
      "estudiante":{ 
         "nombre":"Marcos",
         "examenes":{ 
            "matematica":70,
            "geografia":80
         }
      }
   }
}
print(ejemploDiccionario['clase']['estudiante']['examenes']['matematica'])
