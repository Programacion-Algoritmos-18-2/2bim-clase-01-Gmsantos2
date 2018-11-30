#Ejeplo de excepciones

try:
	n1 = input("Ingrese un numero:\n")
	n1 = int(n1)
	n2 = input("Ingrese un numero 2:\n")
	n2 = int(n2)
	operacion = n1 / n2
	print("El valor de la operacion es: %d"%(operacion))
except NameError as e:
	print("Existe un error: %s" % (e))

except ValueError as e:
	print("Existe un error(%s): %s" % (e.__class__ , e ))

except ZeroDivisionError as e:
	print("Existe un error(%s): %s" % (e.__class__ , e ))

#except Exception as e:
#	print("Existe un error(%s): %s" % (e.__class__ , e ))

