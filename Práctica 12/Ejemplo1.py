def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)
    
# Ejemplo de uso
resultado = factorial(5)
print(resultado) # Salida: 120