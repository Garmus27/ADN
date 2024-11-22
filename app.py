import random
from clases import ADN,Detector,Radiacion,Virus,Sanador

def main():
    adn = ADN()
    secuencia_de_adn = adn.crearADN()
    print("ADN inicial:")
    adn.mostrar_matriz(secuencia_de_adn)

    while True:
        print("\nOpciones:")
        print("1. Detectar mutaciones")
        print("2. Mutar ADN")
        print("3. Sanar ADN")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("-------------------------------------------------------------")
            detector = Detector(secuencia_de_adn)
            detector.detectar_mutaciones()
            print(detector.mostrar())

        elif opcion == "2":
            while True:                
                print("-------------------------------------------------------------")
                tipo_mutacion = input("Ingrese el tipo de mutación \n1. Radiacion \n2. Virus\n ")
                if tipo_mutacion == "1":
                    mutador = Radiacion(None, None, None)
                    secuencia_de_adn = mutador.crear_mutante(secuencia_de_adn)
                    break
                elif tipo_mutacion == "2":
                    mutador = Virus(None, None, None)
                    secuencia_de_adn = mutador.crear_mutante(secuencia_de_adn)
                    break
                else:
                    print("opcion no valida")

            print("ADN mutado:")
            adn.mostrar_matriz(secuencia_de_adn)

        elif opcion == "3":
            print("-------------------------------------------------------------")
            sanador = Sanador(secuencia_de_adn)
            secuencia_de_adn = sanador.sanar_mutantes()
            print("ADN después de sanar:")
            adn.mostrar_matriz(secuencia_de_adn)
            
        elif opcion == "4":
            print("\nTerminando el programa ......")
            print("...................\n")
            print("Nos vemos en segundo año si dios y la rosa de guadalupe, con ventilador de fondo, asi lo quieren\n4")
            break
            
if __name__ == "__main__":
    main()
    