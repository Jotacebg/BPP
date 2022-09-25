import pdb
pdb.set_trace()

def maximo_list():
    lista = [[2, 4, 1], [1,2,3,4,5,6,7,8], [100,250,43]]

    # Obtiene el valor máximo de cada sublista
    # Recorre las sublistas que se encuentran en el a lista para encontrar el valor mas alto.
    maximos = [max(i) for i in lista]

    print(maximos)


def es_primo(num):
    """Funcion que determina si un número es primo"""
    for n in range(2, num):
        if num % n == 0:
            return False
        
        return True

def es_primo_filter():
    
    lista = [3, 4, 8, 5, 5, 22, 13]
    # Utilizamos filter con la funcion para calcular si es un número primo y le pasamos la lista
    # Muestra todos los números primos de la lista.
    primo = list(filter(es_primo, lista))

    print(primo)
    
if __name__ == '__main__':
    maximo_list()
    es_primo_filter()