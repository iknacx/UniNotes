#| Solemne 2 | Grupo 9
#| Integrantes: 
#| * Estefano Muñoz
#| * Lucas Bastidas
#| * Ignacio Ibarra        

import os
from matplotlib import pyplot as plt
import pandas as pd

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
        Usamos el metodo describe() para describir el dataframe con las siguientes columnas:
        * Salario
        * Experiencia
        * Contratacion
        """
        des = self.df[["Salario", "Experiencia", "Contratacion"]].describe()
        print(des)

    def datos_pregunta2(self):
        df = self.df.loc[(self.df["Pais Residencia"] == "United States") & ((self.df["Experiencia"] == 2) | (self.df["Experiencia"] == 5))]

        datos = df.groupby(["Contratacion", "Experiencia"])["Salario"].sum().reset_index()
        datos["Conteo"] = df.groupby(["Contratacion", "Experiencia"]).size().reset_index(drop=True)
        
        datos["Media"] = datos[["Salario", "Conteo"]].apply(lambda s: round(s[0] / s[1], 2), axis=1)
        return datos


    def grafico_pregunta2(self, datos: pd.DataFrame):
        pivot = datos.pivot_table(index="Contratacion", columns="Experiencia", values="Media", fill_value=0)

        labels = pivot.index
        exp_2 = pivot[2]
        exp_5 = pivot[5]

        posiciones = range(len(labels))
        ancho = 0.35

        fig, ax = plt.subplots()
        ax.bar(posiciones, exp_2, ancho, label="2 años")
        ax.bar([p + ancho for p in posiciones], exp_5, ancho, label="5 años")

        ax.set_title("Media de salario de residentes en Estados Unidos de 2 y 5 años de experiencia")
        ax.set_ylabel("Media")
        ax.set_xticks([p + ancho / 2 for p in posiciones])
        ax.set_xticklabels(labels)
        ax.legend()

        plt.show()

    
    def grafico_pregunta3(self):
        df = self.df.loc[(self.df["Contratacion"] >= 2017) & (self.df["Pais Origen"] != "SIN DATOS")][["Pais Origen", "Hijos"]]
        df = df.groupby('Pais Origen')['Hijos'].sum().reset_index()

        

        df = df.sort_values("Hijos", ascending=False).reset_index(drop=True)
        df = df[:6]
        
        total = df["Hijos"].sum()
        df["Porcentaje"] = df["Hijos"].apply(lambda n: round((n * 100) / total, 2))

        print(df)
        
        plt.pie(df["Porcentaje"], labels = df["Pais Origen"], autopct="%1.2f%%", pctdistance=0.8)
        plt.title("Porcentaje de hijos por trabajadora respecto al Pais de Origen")
        plt.show()

        return df

        guardar_dataframe(df)


def guardar_dataframe(df):
    with open("DF_P3.txt", "w", encoding="utf-8") as f: 
        f.write(df.to_csv(index=False))
        f.write("\n\nInterpretación del gráfico:\n")
        f.write("En este grafico, podemos ver que los paises Brasil, Estados Unidos y Perú, son la mayoría\n")
        f.write("Comparado con Chile, Italia y Costa Rica, que son la minoría\n")
        f.write("El país con mas hijos es Brasil con 45.84%\n")

def limpiar_pantalla():
    """
    Esta función limpia la pantalla mandando un comando a la terminal
    Revisa si esta corriendo el programa en windows o linux
    """

    # Si os.name es 'nt', significa que estamos en windows y el comando para limpiar pantalla es 'cls'
    if os.name == 'nt':
        os.system("cls")
    # Sino, se ejecuta el comando 'clear', este es el comando para limpiar pantalla en linux y macOS
    else:
        os.system("clear")

prog = Programa("9_RRHHEmpresas_Nine.csv")
listo = False
# Creamos un bucle "while" para mostrar las opciones disponibles para el usuario.
while not listo:
    limpiar_pantalla()
        

    prog.mostrar_menu()
    opcion = input("Elige [1, 2, 3, 4]: ")
    print("\n")
    
    if opcion == "1":
        prog.analisis_archivo()

    elif opcion == "2":
        datos = prog.datos_pregunta2()
        prog.grafico_pregunta2(datos)

    elif opcion == "3":
        prog.grafico_pregunta3()

    elif opcion == "4":
        print("Programa finalizado.")
        listo = True


    # Hacemos una pausa por cada opción que elija el usuario
    # para despues volver al menú o salir
    continuar = False
    while not continuar and not listo:
        input("\nPresione [Enter] para continuar.. ")
        continuar = True