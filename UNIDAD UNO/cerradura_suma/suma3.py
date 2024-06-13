#Pedirle al usuario que ingrese dos numeros flotantes 
print("Ingrese dos números flotantes:")
num1 = float(input("Ingrese el primer numero"))
num2 = float(input("Ingrese el segundo numero"))
#comparar los numeros 
if num1 > num2: 
    print("El primer numero es mayor que el segundo numero ")
elif num1 < num2:
    print("El segundo numero es mayor que el primer numero ")
    format((num2,num1))
else:
    print("Ambos numeros son iguales")