import os

def guardar_dataframe(df):
    """
    Guarda el dataframe en el archivo "DF_P3.txt"
    Usamos encoding="utf-8" para aceptar caracteres con tilde y ñ
    """
    with open("DF_P3.txt", "w", encoding="utf-8") as f: 
        # Usamos el parametro index=False para no mostrar el indice de cada fila en el archivo
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

