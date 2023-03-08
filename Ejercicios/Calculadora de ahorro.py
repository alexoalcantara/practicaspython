print("Hola")
print("Por favor introduce la siguiente información: ")
na_ = input
na_ = int(input("Número de años a ahorrar: "))
m = int(input("Perioricidad de sus aportaciones: "))
R = float(input("Monto: "))
J = float(input("Tasa de interés (expresada en porcentaje): "))/100

#Cálculos
i = J/m
print(type(i))
n = na_*m
M = R*((1+i)**n-1)/i

numUno = 1
numDos = 2

num_uno = 1
num_dos = 2

print(f"Si ahorras {R} pesos durante {m} al año, al final de {na_} años estarás recibiendo un total de {M:.2f} pesos")