#| Importamos la libreria "pandas" como "pd" que nos ayuda a leer archivos csv
import pandas as pd
#| Importamos la libreria "matplotlib" de la que sacamos "pyplot" como "plt", esta nos ayuda a generar graficos
from matplotlib import pyplot as plt

#| Leemos el archivo csv como un "dataframe" de pandas
df = pd.read_csv("gamesales.csv")

#| Esta función lo que hace es devolver un diccionario ({genero: venta}) ordenado de mayor a menor
#| Nos sirve para sacar el punto 1 y 2
def lista_ventas_genero(anyo, region):
    #| "d" es el diccionario que luego se devolverá al rellenarle los datos y ordenarlo
    d = {}
    #| Iteramos el rango de 0 a el número de filas del dataframe
    for i in range(len(df.index)):
        #| Comprobamos si el año de la fila es el correcto
        if df["Year"][i] == anyo:
            #| Actualizamos el diccionario guardando el genero con su respectiva venta global
            d.update({ df["Genre"][i]: df[region][i] })

    #| Devolvemos el diccionario ordenado de mayor a menor
    #|
    #| Usamos "lambda" (funcion anonima) en el parametro "key" para indicarle a la función que ordene
    #| el diccionario tomando en cuenta el valor y no la llave: ({llave: valor})
    #|                                                              ^      ^
    #|                                                            x[0]   x[1]
    #| Finalmente especificamos el argumento "reverse" para indicar que queremos que ordene de manera descendiente
    #| ya que la función "sorted" ordena de manera ascendiente por defecto
    return dict(sorted(d.items(), key=lambda x: x[1], reverse=True))

#| Esta función nos sirve para calcular el porcentaje de inversión de cada genero
def inversion_publicidad_por_genero():
    #| Sumamos todos los valores de la columna "Global_Sales" para despues sacar el promedio
    prom = sum(df["Global_Sales"])

    #| d es el diccionario que devolveremos
    d = {}

    #| Iteramos por el rango de 0 al número de filas
    for i in range(len(df.index)):
        #| Guardamos el genero de la fila i
        genero = df["Genre"][i]
        
        #| Si el genero no está guardado en el diccionario..
        if not genero in d.keys():
            #| Actualizamos el diccionario agregando el genero con su respectivo valor 
            d.update({ genero: 0.0 })
        
        #| Le sumamos la venta global del genero al valor del genero en el diccionario
        d[genero] += df["Global_Sales"][i]

    #| Iteramos por las llaves ({llave: valor}) del diccionario
    for k in d.keys():
        #| Actualizamos el valor del diccionaro en la llave k con el porcentaje promedio redondeado con 2 decimales
        d[k] = round((d[k] * 100) / prom, 2)
    
    #| Devolvemos el diccionario
    return d


#| Obtenemos la respuesta del primer punto del problema
resultado = lista_ventas_genero(2017, "Global_Sales")
#| Le asignamos un tamaño a la figura para que no se sobrepongan las cosas
plt.figure(figsize=(15, 8))
#| Le colocamos el titulo a la figura
plt.title("Videojuegos a nivel Global el año 2017")
#| Colocamos un texto para mostrar que significan las xs
plt.xlabel("Genero")
# Realizamos lo mismo para las ys
plt.ylabel("Venta")

# Obtenemos la lista de barras de la figura para luego cambiarle el color a la más alta
barras = plt.bar(resultado.keys(), resultado.values())
barras[0].set_color('orange')

# Guardamos la figura como imagen
plt.savefig("punto1.png")
# Finalmente cerramos la figura
plt.close()

# Obtenemos la respuesta del segundo punto del problema
resultado = lista_ventas_genero(2020, "EU_Sales")
# Le asignamos un tamaño a la figura para que no se sobrepongan las cosas
plt.figure(figsize=(15, 8))
# Le colocamos el titulo a la figura
plt.title("Videojuegos en Europa el año 2020")

# Le colocamos nombre a las x e y
plt.xlabel("Genero")
plt.ylabel("Venta")

# Le cambiamos el color a la 5ta barra 
barras = plt.bar(resultado.keys(), resultado.values())
barras[4].set_color('orange')

# Guardamos y cerramos la figura
plt.savefig("punto2.png")
plt.close()

# Obtenemos la respuesta del tercer punto del problema
resultado = inversion_publicidad_por_genero()
# Le asignamos un tamaño a la figura para que no se sobrepongan las cosas
plt.figure(figsize=(10, 5))

# Le colocamos titulo
plt.title("Porcentaje de inversión")

# Para este punto creamos un grafico de torta ya que trata de porcentajes
plt.pie(resultado.values(), labels=resultado.keys())

# Arreglamos los nombres para mostrarlos de forma "Genero - Porcentaje%"
# para esto usamos una lista de comprensión el cual crea una lista segun el format especificado
nombres = [f"{k} - {v}%" for k, v in resultado.items()]

# Agregamos una simbología con los nombres arreglados y la mostramos a la izquierda
plt.legend(nombres, bbox_to_anchor=(1.1, 1.0))

# Guardamos y cerramos la figura
plt.savefig("punto3.png")
plt.close()

print("Graficos generados: punto1.png, punto2.png, punto3.png")