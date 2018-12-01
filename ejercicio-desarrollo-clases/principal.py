from paqueteArchivo.miarchivo import MiArchivo, MiArchivoEscribir #importacion de los paquetec con sus respectivas clases
from paqueteModelo.mimodelo import Persona

m = MiArchivo() # objeto para leer el archivo
m2 = MiArchivoEscribir() # objeto para escribir el archivo

lista = m.obtener_informacion() #lista le mandamos  la informacion de el metodo obtener informacion
lista = [l.split("|") for l in lista] #manejo de split para cojer un elemento  donde termina en |

lista = lista[1:] #lista queda inicializada desde la posicion 1
for d in lista: #for para recorrer la lista
    
    p = Persona(d[0], d[1],d[2],d[3]) #al objeto le mandamos los parametos de a lista  en tal posicion
    print(p) #presenta el objeto p 
    m2.agregar_informacion(p) #agrega 

m.cerrar_archivo() #metodo para cerrar el archivo  (close())
m2.cerrar_archivo() #cerrar el archivo que escribimos (close())
