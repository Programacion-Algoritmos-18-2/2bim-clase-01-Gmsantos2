"""
    creación de clases
"""

class Persona(object): #clase persona
    """
    """
    
    def __init__(self, n, n1,n2,n3): #init con tods sus valores inicializados
        """
        """
        self.nombre = n
        self.nota1 = float(n1)
        self.nota2 = float(n2)
        self.nota3 = float(n3)
    
    #METODOS AGREGAR Y OBTENER
    def agregar_nombre(self, n):
        """
        """
        self.nombre = n

    def obtener_nombre(self):
        """
        """
        return self.nombre

    
    def agregar_n1(self, n1):
        """
        """
        self.nota1 = n1

    def obtener_n1(self):
        """
        """
        return self.nota1
    
    def agregar_n2(self, n2):
        """
        """
        self.nota2 = n2

    def obtener_n2(self):
        """
        """
        return self.nota2

    def agregar_n3(self, n3):
        """
        """
        self.nota3 = n3

    def obtener_n3(self):
        """
        """
        return self.nota3

    #metodo para retornar el promedio
    def promedio (self):
        sum = self.nota1 + self.nota2 + self.nota3
        self.prom = sum / 3
        return self.prom #retorna el promedio
    
    def __str__(self): #metodo to string
        """
        """
        return "%s|%.2f\n" % (self.obtener_nombre(), self.promedio()) #retorna una cadena (print)
