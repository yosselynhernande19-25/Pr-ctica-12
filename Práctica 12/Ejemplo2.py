from time import sleep
def conte_hacia_atras(n):
    if n <= 0:
        print("¡Despegueee!")
    else:
        print(n)
        sleep(2)
        conte_hacia_atras(n-1)
        
# Ejemplo de uso
conte_hacia_atras(10)