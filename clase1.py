import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re
import csv

class Error(Exception):
        pass

class NumerodeMesesIncorrecto(Error):
        pass

# Función que intenta abrir y leer el fichero csv Finanzas
# Se muestran los datos del csv
def leer_csv():
        try:
        #Se intenta abrir el fichero csv
                with open('finanzas2020[1].csv', newline='') as File:  
                        reader = csv.reader(File)
                        for row in reader:
                                print(row)
                
        except IOError as err:
                print("No encuentro el fichero o no se puede leer. Error: ", err)
        else:
                print("Se ha leído el fichero correctamente.") 

# Función que crea un DataFrame y comprobamos que los datos son correctos
# Comprobamos que hay doce columnas.
# Devuelve un dataframe de enteros
def crearDataFrame():
        try:
                #Leemos el fichero finanzas.csv y creamos un dataframe
                df = pd.read_csv("finanzas2020[1].csv", sep="\t")
                #Activamos la opcion para poder ver todas las filas
                pd.options.display.max_rows = 100
                
                #Se comprueba que se tienen 12 columnas
                col = df.columns
                if int(len(col)) != 12:
                        raise NumerodeMesesIncorrecto
                
                #Con regex buscamos con una expresión regular palabras o cualquier cadena de string
                palabras = re.compile(r'[a-zA-Z]{2,6}', re.I)
                # Recorremos todo el Dataframe
                for column in df:
                        for i in range(len(df[column])):
                                try:
                                        #Si se encuentra la expresion regular la cambia por un cero
                                        if palabras.findall(df.loc[i,column]):
                                                df.loc[i,column] = 0
                                        else:
                                                #Si se trata de un numero pero que es string entre comillas, se eliminan las comillas.
                                                df.loc[i,column] = df[column][i].replace("\'","")
                                                
                                except:
                                        #Si se trata de un string sin comillas o un entero continua con el siguiente dato
                                        continue

                #Convertimos todos los datos a enteros
                for column in df:
                        df[column] = df[column].astype(int)
                
                
                return df
        
        except NumerodeMesesIncorrecto:
                print("No hay doce meses en el fichero")
                
                
# Función que calcula el mes que más gasto del año tiene
def maxgasto():
        df = crearDataFrame()
        maxgasto = None
        maxmes = None
        for mes in df:
                gastos = df.loc[df[mes] < 0,mes].sum()
                if (maxgasto is None or gastos < maxgasto):
                        maxgasto = gastos
                        maxmes = mes
        
        print(f"El mes de más gasto es {maxmes} el cuál se gastó {maxgasto} €")
        
# Función que calcula el mes que más se ha ahorrado.
def maxahorrado():
        df = crearDataFrame()
        ahorros = 0
        aux = None
        maxmes = None
        for mes in df:
                ingresos = df.loc[df[mes] > 0,mes].sum()
                gastos = df.loc[df[mes] < 0,mes].sum()
                
                ahorros = ingresos + gastos
                print(f"{ingresos} + {gastos} = {ahorros}")
                if (aux is None or ahorros > aux):
                        aux = ahorros
                        maxmes = mes

                
        print(f"El mes de más ahorro es {maxmes} en el que se consiguió ahorrar {aux} €.")
        
# Función que calcula la media de gasto en el año
def gasto_total_media():
        df = crearDataFrame()
        media = 0
        
        for mes in df:
                gastos = df.loc[df[mes] < 0,mes].sum()
                media += gastos
        
        print(f"El total de gastos en el año es: {media} €")                 
        media = round(media/int(len(df.columns)),2)   
        print(f"La media de gastos del año es: {media} €")
        
# Función que calcula el total de ingresos de todo el año
# Devuelve una lista con los ingresos de cada mes
def total_ing():
        df = crearDataFrame()
        total = 0
        lista_ing = []
        for mes in df:
                ingresos = df.loc[df[mes] > 0,mes].sum()
                lista_ing.append(ingresos)
                total += ingresos
                
                          

        print(f"El total de ingresos en el año es: {total} €")
        
        return lista_ing
        
# Función que muestra una gráfica con la evolucion de los ingresos a lo largo del año
def gra_ingresos():
        df = crearDataFrame()       
        x = ['Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre']
        y = total_ing()
            
        values = range(len(x))
        plt.figure(figsize=(12,6))
        plt.plot(x,y,marker="o")
        plt.xticks(values,x)
        plt.xlabel('Meses del año')
        plt.ylabel('Ingresos')
        plt.title('Evolucion de los ingresos a lo largo del 2020')
        plt.show()
        
# Función que comprueba que se introduce un número entero
def pedirNumeroEntero():
    correcto=False
    num=0
    while(not correcto):
        try:
            num = int(input("Elige una opción: "))
            correcto=True
        except ValueError:
            print('Error, introduce un numero entero')
     
    return num
 
 
# Menú para seleccionar la distintas opciones
salir = False
opcion = 0
while not salir:
 
    print ("1. Leer el fichero CSV")
    print ("2. Calcular el mes de mas gasto")
    print ("3. Calcular el mes de mas ahorro")
    print ("4. Calcular el total de gasto en el año y la media")
    print ("5. Ingresos totales del año")
    print ("6. Mostrar gráfica de la evolución de los ingresos")
    print ("7. Salir")
 
    opcion = pedirNumeroEntero()
 
    if opcion == 1:
        leer_csv()   
    elif opcion == 2:
        maxgasto()
    elif opcion == 3:
        maxahorrado()
    elif opcion == 4:
        gasto_total_media()
    elif opcion == 5:
        total_ing()
    elif opcion == 6:
        gra_ingresos()    
    elif opcion == 7:
        salir = True
    else:
        print ("Introduce un numero entre 1 y 7")
 
print ("Fin")