class NoEsPositivo(Exception):
    pass
       
def cuadrado_num(num):
    if num < 0:
        raise NoEsPositivo("No es un número positivo")
    else:
        return num * num
       
def cubo_num(num):
    if num < 0:
        raise NoEsPositivo("No es un número positivo")
    else:
       return num * num * num

def es_par(num):
    if num < 0:
        raise NoEsPositivo("No es un número positivo")
    else:
        if num & 1 == 0:
           return True
        else:
            return False
        
def es_primo(num):
    if num < 0:
        raise NoEsPositivo("No es un número positivo")
    else:
        for n in range(2, num):
            if num % n == 0:
                print("No es primo", n, "es divisor")
                return False
        print("Es primo")
        return True
    