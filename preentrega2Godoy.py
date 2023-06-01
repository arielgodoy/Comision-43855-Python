class Persona:    
    nombre = ''
    rut = ''     
    #Constructor de la Clase Persona (Nombre y rut obligatorio)    
    def __init__(self, nombre,rut):
        self.nombre = nombre
        self.rut = rut   
    #ToString()
    def __str__(self):
        return f'Nombre: {self.nombre},RUT: {self.rut}'   
    
    #setters clase Persona    
    def setNombre(self, Nombre):
        self.Nombre = Nombre
    def setRut(self, rut):
        self.rut = rut
        
    
    #getters  clase Persona   
    def getNonbre(self):
        return self.Nonbre
    def getRut(self):
        return self.rut
    
    #Metodo nombre y Rut de la Clase Persona    
    def NombreyRut (self):        
        return self.nombre + ', ' + self.rut

#Clase Cliente hereda de la Clase persona
class Cliente(Persona):
    fechaingreso =''   
    direccion =''
    def __init__(self, nombre,rut, direccion,fechaingreso):
        # Call the constructor of the parent class
        super().__init__(nombre,rut)
        self.direccion = direccion
        self.fechaingreso =fechaingreso
    #ToString()
    def __str__(self):
        return super().__str__() + f"Direccion: {self.direccion},Fecha de Ingreso: {self.fechaingreso}"       
    
    #setters clase Cliente    
    def setfechaingreso(self, fechaingreso):
        self.fechaingreso = fechaingreso
    def setdireccion(self, direccion):
        self.direccion = direccion       
    
    #getters clase Cliente          
    def getfechaingreso(self):
        return self.fechaingreso
    def getdireccion(self):
        return self.direccion



personaactiva = Persona("Ariel Godoy","11.111.111-1")
print(str(personaactiva))
personaactiva.setRut('13.135.401-0')
print(str(personaactiva))
clienteactivo=Cliente("Ariel Godoy","11.111.111-1","Avda. Los Heroes #12345","2023-05-31")

clienteactivo.setRut('22.222.222-2')
print(str(clienteactivo))






