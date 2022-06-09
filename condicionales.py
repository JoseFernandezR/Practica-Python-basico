calificacion = input("Introduce tu calificacion de la AZ-900: ")
calificacion = int(calificacion)

# Comparamos la calificacion para saber si es menor a 700
if calificacion < 700 :
    print("Veess, por no estudiar... ") # Si es menor a 700 imprime esto
elif calificacion == 700 :
    print("Panzazoooo...")
elif calificacion > 1000:
    print("Mientes, no puedes sacar mas de 1000")
else : # Si no se cumple el if anterior pasa a esta linea
    print("Felicidades, pasa por tu certificado") # Se ejecuta si ningun if se cumple

#Verificador de mayoria de edad
edad = input("Cual es tu edad: ")
edad = int(edad)

if edad >=18 and edad <= 100 :
    print("Bienvenid@ al mamitas")
elif edad > 100 :
    print("Si vienes acompañad@ de tus abuelitos, si te podemos fiar")
elif edad < 0 :
    print("Ni que fueras viajer@ del tiempo")
else :
    print("No puedes llevarte esos cigarros")

# En Python no hay SWITCH CASES 