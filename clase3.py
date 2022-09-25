class NoEsPositivo(Exception):
    """Clase usada para la excepción cuando un número es negativo"""
    pass
       
def cuadrado_num(num):
    """Función devuelve el cuadrado de un número"""
    if num < 0:
        raise NoEsPositivo("No es un número positivo")
    else:
        return num * num
       
def cubo_num(num):
    """Función que devuelve el cubo de un número"""
    if num < 0:
        raise NoEsPositivo("No es un número positivo")
    else:
       return num * num * num

def es_par(num):
    """Función que determina si un número es par"""
    if num < 0:
        raise NoEsPositivo("No es un número positivo")
    else:
        if num & 1 == 0:
           return True
        else:
            return False
        
def es_primo(num):
    """Funcion que determina si un número es primo"""
    if num < 0:
        raise NoEsPositivo("No es un número positivo")
    else:
        for n in range(2, num):
            if num % n == 0:
                print("No es primo", n, "es divisor")
                return False
        print("Es primo")
        return True
    