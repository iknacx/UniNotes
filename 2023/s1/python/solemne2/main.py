#| Solemne 2 | Grupo 9
#| Integrantes:
#| * Estefano Muñoz
#| * Lucas Bastidas
#| * Ignacio Ibarra

from funciones import guardar_dataframe, limpiar_pantalla
from programa import Programa

# Inicializar la clase Programa
prog = Programa("9_RRHHEmpresas_Nine.csv")
listo = False
# Creamos un bucle "while" para mostrar las opciones disponibles para el usuario.
while not listo:
    # Antes de mostrar el menú limpiamos la pantalla
    limpiar_pantalla()

    # Mostramos el menú y pedimos al usuario que elija una opción
    prog.mostrar_menu()
    opcion = int(input("Elige [1, 2, 3, 4]: "))
    print("\n")

    # Revisamos cada opción que pudo elegir el usuario y realizamos la acción de cada opción
    if opcion == 1:
        prog.analisis_archivo()

    elif opcion == 2:
        datos = prog.datos_pregunta2()
        prog.grafico_pregunta2(datos)

    elif opcion == 3:
        datos = prog.grafico_pregunta3()
        guardar_dataframe(datos)

    elif opcion == 4:
        print("Programa finalizado.")
        listo = True
    else:
        # Si el usuario ingresó una opción que no corresponde, le avisamos que se equivocó
        print("* Opcion Invalida *")


    # Hacemos una pausa por cada opción que elija el usuario
    # para despues volver al menú o salir
    continuar = False
    while not continuar and not listo:
        input("\nPresione [Enter] para continuar.. ")
        continuar = True
