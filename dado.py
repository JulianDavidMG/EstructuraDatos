import random

def lanzar_dado():
    resultado = random.randint(1, 6)
    
    print("Lanzando el dado....")
    print(f"el resultado es: {resultado}")
    
lanzar_dado()