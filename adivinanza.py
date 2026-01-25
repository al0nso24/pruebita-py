import random

secreto = random.randint(1, 10)
num = int(input("Escribe un número: "))
intentos = 1

while num != secreto: #Mientras el número (usuario) no sea igual al número secreto.
    num = int(input("Sigue intentando: "))
    intentos+=1
    
print("Adivinaste :D")
print(f"Logrado en {intentos} intentos")

if intentos > 100: #Si supera los 100 intentos.
    print("Que mala suerte tienes :v")