# 1. Luis decidió tener un rato de diversión luego de una larga jornada de estudio. Decidió 
# entonces, jugar GAME OF THRONES. Luis actualmente tiene 1000 puntos. Si hoy llega al 
# Pozo del Dragón sumará 19 puntos más. Si logra llegar al Medidor de Feudos sumará los 
# 19 puntos del Pozo más 40 puntos adicionales. Si logra alcanzar Hielo y Fuego obtendrá 
# 19 puntos del Pozo del Dragón, más 40 puntos del Medidor de Feudos, más 10 puntos 
# por participar en el juego. 

print("Niveles")
print("1.Pozo del Dragón , 2. Medidor de Feudos, 3.Hielo y Fuego")

nivel = int(input("Digite el numero del nivel alcanzado:"))
puntos = 1000
pososDelDragon = + 19
medidorFeudos =  pososDelDragon + 40
hieloYfuego =  medidorFeudos + 10

if nivel == 1 :
    print("Puntos obtenidos", puntos + pososDelDragon)
if nivel == 2 : 
     print("Puntos obtenidos", puntos + medidorFeudos)    
if nivel == 3 : 
     print("Puntos obtenidos", puntos + hieloYfuego) 
else :
     nivel > 3 or nivel <= 0
     print("Ingrese un numeo correcto")
    





  

    
