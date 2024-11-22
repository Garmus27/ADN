import random
from clases import ADN, Detector, Radiacion, Virus, Sanador

def main() -> None:
    adn = ADN()
    secuencia_de_adn = adn.crearADN()
    print("ADN inicial:")
    adn.mostrar_matriz(secuencia_de_adn)

    while True:
        
        """ Se crea el menu"""
        print("\nOpciones:")
        print("1. Detectar mutaciones")
        print("2. Mutar ADN")
        print("3. Sanar ADN")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        """ si se elije la opcion uno se llama a la clase detector a que realize su magia y finalize mostrando la informacion correspondiente tanto si se encontro un mutante o si no se encontro"""
        if opcion == "1":
            print("-------------------------------------------------------------")
            detector = Detector(secuencia_de_adn)
            detector.detectar_mutaciones()
            print(detector.mostrar())
  
        
        elif opcion == "2":
            """ si se elige la opcion dos primero se pregunta que tipo de mutacion se quiere realizar"""
            while True:
                print("-------------------------------------------------------------")
                tipo_mutacion = input("Ingrese el tipo de mutación \n1. Radiación \n2. Virus\n ")
                """ dependiendo de la opcion se llama a la clase Radiacion o Virus y se crea la mutacion"""
                if tipo_mutacion == "1":
                    mutador = Radiacion(None, None, None)
                    secuencia_de_adn = mutador.crear_mutante(secuencia_de_adn)
                    break
                elif tipo_mutacion == "2":
                    mutador = Virus(None, None, None)
                    secuencia_de_adn = mutador.crear_mutante(secuencia_de_adn)
                    break
                else:
                    print("Opción no válida")

            """mostramos la nueva secuencia de adn mutada"""
            print("ADN mutado:")
            adn.mostrar_matriz(secuencia_de_adn)

        
        elif opcion == "3":
            """ si se elige la opcion 3 se llama a la clase sanar para crear una secuencia de adn sana sin covid"""
            print("-------------------------------------------------------------")
            sanador = Sanador(secuencia_de_adn)
            secuencia_de_adn = sanador.sanar_mutantes()
            print("ADN después de sanar:")
            adn.mostrar_matriz(secuencia_de_adn)

        elif opcion == "4":
            
            """ cerramos el programa con un mensaje amigable y esperanzador"""
            
            print("\nTerminando el programa ......")
            print("...................\n")
            print("Nos vemos en segundo año si dios y la rosa de Guadalupe, con ventilador de fondo, así lo quieren\n")
            break

if __name__ == "__main__":
    main()
