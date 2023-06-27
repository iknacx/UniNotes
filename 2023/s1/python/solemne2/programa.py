import pandas as pd
from matplotlib import pyplot as plt

class Programa:
    """
    Esta clase contiene todas las funciones del programa
    """
    def __init__(self, nombre_archivo) -> None:
        """
        Inicializamos la clase aceptando el nombre del archivo csv como parametro 
        """

        # Guardamos el dataframe en la clase
        self.df = pd.read_csv(nombre_archivo)

        # Rellenar las filas vacías en la columna "Pais Origen" con "SIN DATOS"
        self.df["Pais Origen"] = self.df["Pais Origen"].fillna("SIN DATOS")

        # Eliminar todas las filas vacías
        self.df = self.df.dropna()

        # Usamos los metodos de str del dataframe para reemplazar cada '$' con un caracter vacío para borrarlo
        self.df["Salario"] = self.df["Salario"].str.replace('$', '').astype(float)

    def mostrar_menu(self):
        """
        Esta función muestra el menú principal del programa
        """

        print("** Menu Principal **")
        print("[1] Análisis del Archivo de Datos (9_RRHHEmpresas_Nine.csv)")
        print("[2] Analítica de datos 1")
        print("[3] Analítica de datos 2")
        print("[4] Salir")

    def analisis_archivo(self):
        """
        Usamos el metodo describe(), y describimos la salida del metodo en las siguientes 2 columnas:
        * Salario
        * Experiencia
        """
        print(self.df.describe())
        print("Interpretación de columna \"Salario\":")
        print("* La media del salario es: 3093.31")
        print("* El salario minimo fue de: 1005.37")
        print("* El salario maximo fue de: 4998.89")
        print("* La derivación estandar fue de: 1120.68")

        print("Interpretación de columna \"Experiencia\":")
        print("* La media de experiencia es: 4.81")
        print("* El minimo de experiencia fue que no habia experiencia")
        print("* El maximo de experiencia fue de 10 años")
        print("* La derivación estandar fue de: 3.07")

    def datos_pregunta2(self):
        """
        Prepara los datos para luego graficarlos en la función "grafico_pregunta2"
        """
        # Este es el filtro que selecciona solo los residentes de estados unidos, y con 2 y 5 años de experiencia
        df = self.df.loc[(self.df["Pais Residencia"] == "United States") & ((self.df["Experiencia"] == 2) | (self.df["Experiencia"] == 5))]

        # Aqui los agrupamos por el año de contratación y experiencia y luego sumamos el salario de cada uno
        datos = df.groupby(["Contratacion", "Experiencia"])["Salario"].sum().reset_index()
        # Agregamos una columna llamada "Conteo" la cual guardará cuantas personas hay en cada fila
        datos["Conteo"] = df.groupby(["Contratacion", "Experiencia"]).size().reset_index(drop=True)
        # Luego sacamos la media tomando el salario y la cantidad de personas
        # Usamos apply con una funcion anonima que toma "x" el cual contiene el salario y la cantidad de personas de cada fila
        # Y realizamos una división, luego la redondeamos a 2
        # El parametro axis=1 es para especificar que el calculo se haga en filas, no en columnas
        datos["Media"] = datos[["Salario", "Conteo"]].apply(lambda s: round(s[0] / s[1], 2), axis=1)
        # Devolvemos los datos calculados a la otra función para graficar
        return datos


    def grafico_pregunta2(self, datos: pd.DataFrame):
        """
        Esta función grafica los datos recibidos de la función "datos_pregunta2"
        """

        # Recreamos el dataframe usando el año de contratación como fila, y la experiencia como columna
        # Y rellenamos la tabla con los valores de Media
        # Esto sirve para que en caso de que sea nulo el valor, se rellene con 0s
        pivot = datos.pivot_table(index="Contratacion", columns="Experiencia", values="Media", fill_value=0)

        # pivot.index son los años de contratación
        labels = pivot.index

        # pivot[n] accede a los valores de la Media, siendo n la Experiencia (2 y 5)
        exp_2 = pivot[2]
        exp_5 = pivot[5]


        posiciones = range(len(labels))
        ancho = 0.35



        # Obtenemos el subgrafico para poder graficar más de una cosa a la vez
        _, ax = plt.subplots()
        # Añadimos las barras de 2 años de experiencia al grafico
        ax.bar(posiciones, exp_2, ancho, label="2 años")
        # Luego las de 5 años de experiencia
        # Usamos una lista de comprensión para sumarle el "ancho" a cada posición para ajustarla y que se puedan mostrar las 2 barras
        ax.bar([p + ancho for p in posiciones], exp_5, ancho, label="5 años")

        # Le colocamos titulo
        ax.set_title("Media de salario de residentes en Estados Unidos de 2 y 5 años de experiencia")
        # El nombre de la coordenada y
        ax.set_ylabel("Media")
        # Movemos las barras a medio "ancho" para que no queden pegadas
        ax.set_xticks([p + ancho / 2 for p in posiciones])
        # le damos nombre a cada barra
        ax.set_xticklabels(labels)
        # Mostramos la simbología
        ax.legend()


        print("Interpretación del grafico:")
        print("Podemos concluir que la media las residentes con 2 años de experiencia superan en la mayoria de años a las de 5 años")
        print("Tambien podemos concluir que en el 2018 no hubo nadie de 5 años de experiencia")

        # Desplegamos el grafico
        plt.show()


    def grafico_pregunta3(self):
        """
        Resuelve el punto 3
        Muestra un gráfico de torta el cual muestra los porcentajes de Hijos en cada Pais de Origen
        """

        # Aplicamos el filtro para seleccionar la contratación mayor o igual a 2017, que no sea el pais de origen "SIN DATOS"
        # Y seleccionamos las columnas País de Origen e Hijos
        df = self.df.loc[(self.df["Contratacion"] >= 2017) & (self.df["Pais Origen"] != "SIN DATOS")][["Pais Origen", "Hijos"]]

        # Agrupamos las filas en País de origen y le sumamos la columna hijos
        df = df.groupby('Pais Origen')['Hijos'].sum().reset_index()

        # Ordenamos los valores de la columna Hijos
        # Usamos el parametro ascending=False para que pueda ser de mayor a menor
        df = df.sort_values("Hijos", ascending=False).reset_index(drop=True)
        # Sacamos solo los 6 primeros Paises
        df = df[:6]

        # Obtenemos el total de hijos para luego sacar el porcentaje
        total = df["Hijos"].sum()

        # Usamos apply en la columna de Hijos, usando una función anónima la cual saca el porcentaje de cada valor de la columna
        df["Porcentaje"] = df["Hijos"].apply(lambda n: round((n * 100) / total, 2))

        # Mostramos el dataframe
        print(df)

        # Generamos el grafico de torta, con el porcentaje y con los paises como etiqueta
        # Usamos autopct para mostrar el %, y pctdistance para mover el texto del porcentaje para que se vea mejor
        plt.pie(df["Porcentaje"], labels = df["Pais Origen"], autopct="%1.2f%%", pctdistance=0.8)
        # Le asignamos un titulo
        plt.title("Porcentaje de hijos por trabajadora respecto al Pais de Origen")

        # Mostramos el grafico
        plt.show()
        # Retornamos el dataframe para luego guardarlo en el archivo
        return df
