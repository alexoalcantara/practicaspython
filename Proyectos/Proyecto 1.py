n = input("Escriba su nombre por favor: ")
while True:
    edad = input("Ingrese su edad en años: ")
    try:
        edad = int(edad)
        if edad > 0:
            break
        elif edad == 0:
            print ("La edad no puede ser igual a 0 años, por favor introduce otro valor")
    except ValueError:
        print("Por favor introoduce valores númericos, no olvides rellenar cada espacio")
a = float(input("Indique su altura en metros: "))
altura = a
m = float (input("Indique su masa en kilogramos (peso): "))
masa = m
IMC = m / a**2
if(edad < 18):
        print("usted es menor de edady su IMC es equivalente a: ")
else:
        print("usted es mayor de edad y su IMC es equivalente a: ")
        IMC = m / a**2
        print("IMC: " + str(IMC) )
if IMC >= 0 and IMC <= 15.99 :
        print ("Delgadez severa")
elif IMC >= 16.00 and IMC <= 16.99 :
        print ("Delgadez moderada")
elif IMC >= 17.00 and IMC <= 18.49:
        print ("Delgadez leve")
elif IMC >= 18.50 and IMC <= 24.99 :
        print ("Normal")
elif IMC >= 25.00 and IMC <= 29.99:
        print ("Sobrepeso")
elif IMC >= 30.00 and IMC <= 34.99:
        print ("obesidad leve")
elif IMC >= 35.00 and IMC <= 39.00:
        print ("obesidad media")
elif IMC >= 40.00:
        print ("obesidad morbida")
print("Ahora usted ya conoce su IMC, hasta luego")        