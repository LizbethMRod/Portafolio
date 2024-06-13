print("cerradura: La suma de dos numeros reales siempre da como resultado otro numero real")
print("a + b pertenece R")
print("El siguiente programa realiza la propiedad de cerradura")
print() #linea en blanco para dejar un espacio 
num1 = float(input("Ingrese el primer numero"))
num2 = float(input("Ingrese el segundo numero"))
#calcula la suma de los dos numeros 
multi = num1 * num2
#verifica si la suma es un numero entero 
if multi.is_integer():
    resulted = "entero"
else:
    resulted = "racional"

#Muestra el resultado de la suma y su tipo 
print() #linea para dejar espacio 
print("El resultado de la multiplicacion es:" , multi )
print("El resultado es un numero", resulted)
    