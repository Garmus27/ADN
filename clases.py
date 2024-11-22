import random


class ADN:
    def __init__(self):
        self.bases = ['A', 'T', 'C', 'G']
        self.matriz = []

    def crearADN(self):
        self.matriz = []
        for _ in range(6):
            fila = ''.join(random.choices(self.bases, k=6))
            self.matriz.append(fila)
        return self.matriz
    
    def mostrar_matriz(self, matriz):
        for fila in matriz:
            print("  ".join(fila))
        print()
        
        
        
class Detector:
    def __init__(self, adn):
        self.__base_nitrogenada = None
        self.__tipo_mutacion = None
        self.__encontrado = False
        self.adn = adn
        self.base_map = {
            'A': 'Adenina',
            'T': 'Timina',
            'C': 'Citosina',
            'G': 'Guanina'}

    def deteccion_horizontal(self):
        for fila in self.adn:
            if self.__detectar_mutacion(fila):
                self.__tipo_mutacion = "RADIACION"
                return

    def deteccion_vertical(self):
        for col in range(6):
            columna = ''.join([self.adn[fila][col] for fila in range(6)])
            if self.__detectar_mutacion(columna):
                self.__tipo_mutacion = "RADIACION"
                return

    def deteccion_diagonal(self):
        for start in range(-5, 6):
            diagonal1 = ''.join([self.adn[i][i-start] for i in range(6) if 0 <= i-start < 6])
            diagonal2 = ''.join([self.adn[i][5-i+start] for i in range(6) if 0 <= 5-i+start < 6])
            if self.__detectar_mutacion(diagonal1) or self.__detectar_mutacion(diagonal2):
                self.__tipo_mutacion = "VIRUS"
                return

    def detectar_mutaciones(self):
        self.deteccion_horizontal()
        if not self.__encontrado:
            self.deteccion_vertical()
        if not self.__encontrado:
            self.deteccion_diagonal()
        return self.__encontrado

    def mostrar(self):
        if self.__encontrado:
            return f"Este ADN ha sido mutado\nTipo de mutación: {self.__tipo_mutacion}\nBase nitrogenada mutada: {self.base_map[self.__base_nitrogenada]}"
        else:
            return "No se han encontrado mutaciones"

    def __detectar_mutacion(self, secuencia):
        for base in ['A', 'T', 'C', 'G']:
            if base * 4 in secuencia:
                self.__base_nitrogenada = base
                self.__encontrado = True
                return True
        return False

        
        
class Mutador:
    def __init__(self, base_nitrogenada, horientacion, coordenada_inicial):
        self.base_nitrogenada = base_nitrogenada
        self.horientacion = horientacion
        self.coordenada_inicial = coordenada_inicial

    def crear_mutante(self):
        pass
    



class Radiacion(Mutador):
    def __init__(self, base_nitrogenada, horientacion, coordenada_inicial):
        super().__init__(base_nitrogenada, horientacion, coordenada_inicial)

    def crear_mutante(self, matriz):
        while True:
            try:
                base_nitrogenada = input("Ingrese la base nitrogenada (A, T, C, G): ").upper()
                if base_nitrogenada not in ['A', 'T', 'C', 'G']:
                    raise ValueError("Base nitrogenada no válida")

                fila, columna = map(int, input("Ingrese la coordenada inicial (fila, columna) separada por una coma: ").split(","))
                if not (0 <= fila < 6 and 0 <= columna < 6):
                    raise ValueError("Coordenada fuera de rango")

                orientacion = input("Ingrese la orientación de la mutación (H para horizontal, V para vertical): ").upper()
                if orientacion not in ['H', 'V']:
                    raise ValueError("Orientación no válida")

                if orientacion == 'H' and columna + 3 >= 6:
                    raise ValueError("Mutación horizontal excede el rango de la matriz")
                if orientacion == 'V' and fila + 3 >= 6:
                    raise ValueError("Mutación vertical excede el rango de la matriz")

                break
            except ValueError as e:
                print(f"Error: {e}. Por favor, intente nuevamente.")

        self.base_nitrogenada = base_nitrogenada
        self.horientacion = orientacion
        self.coordenada_inicial = (fila, columna)

        if self.horientacion == 'H':
            for i in range(4):
                matriz[fila] = matriz[fila][:columna + i] + self.base_nitrogenada + matriz[fila][columna + i + 1:]
        else:
            for i in range(4):
                matriz[fila + i] = matriz[fila + i][:columna] + self.base_nitrogenada + matriz[fila + i][columna + 1:]

        return matriz
    

class Virus(Mutador):
    def __init__(self, base_nitrogenada, horientacion, coordenada_inicial):
        super().__init__(base_nitrogenada, horientacion, coordenada_inicial)

    def crear_mutante(self, matriz):
        while True:
            try:
                base_nitrogenada = input("Ingrese la base nitrogenada (A, T, C, G): ").upper()
                if base_nitrogenada not in ['A', 'T', 'C', 'G']:
                    raise ValueError("Base nitrogenada no válida")

                fila, columna = map(int, input("Ingrese la coordenada inicial (fila, columna) separada por una coma: ").split(","))
                if not (0 <= fila < 6 and 0 <= columna < 6):
                    raise ValueError("Coordenada fuera de rango")

                orientacion = input("Ingrese la orientación de la mutación (A para ascendente, D para descendente): ").upper()
                if orientacion not in ['A', 'D']:
                    raise ValueError("Orientación no válida para un virus")

                if orientacion == 'A':
                    if fila - 3 >= 0 and columna + 3 < 6:  
                        direccion = 'SD'
                    elif fila - 3 >= 0 and columna - 3 >= 0:  
                        direccion = 'SI'
                    else:
                        raise ValueError("Mutación ascendente excede el rango de la matriz")
                else:
                    if fila + 3 < 6 and columna + 3 < 6:  
                        direccion = 'ID'
                    elif fila + 3 < 6 and columna - 3 >= 0:  
                        direccion = 'II'
                    else:
                        raise ValueError("Mutación descendente excede el rango de la matriz")

                break
            except ValueError as e:
                print(f"Error: {e}. Por favor, intente nuevamente.")

        self.base_nitrogenada = base_nitrogenada
        self.horientacion = orientacion
        self.coordenada_inicial = (fila, columna)

        if direccion == 'SD':
            for i in range(4):
                matriz[fila - i] = matriz[fila - i][:columna + i] + self.base_nitrogenada + matriz[fila - i][columna + i + 1:]
        elif direccion == 'ID':
            for i in range(4):
                matriz[fila + i] = matriz[fila + i][:columna + i] + self.base_nitrogenada + matriz[fila + i][columna + i + 1:]
        elif direccion == 'SI':
            for i in range(4):
                matriz[fila - i] = matriz[fila - i][:columna - i] + self.base_nitrogenada + matriz[fila - i][columna - i + 1:]
        elif direccion == 'II':
            for i in range(4):
                matriz[fila + i] = matriz[fila + i][:columna - i] + self.base_nitrogenada + matriz[fila + i][columna - i + 1:]

        return matriz
    
    
    
class Sanador:
    def __init__(self, adn):
        self.adn = adn
        self.mutaciones_detectadas = False

    def sanar_mutantes(self):
        detector = Detector(self.adn)
        self.mutaciones_detectadas = detector.detectar_mutaciones()
        
        if self.mutaciones_detectadas:
            nueva_matriz = []
            bases = ['A', 'T', 'C', 'G']
            for _ in range(6):
                fila = ''.join(random.choices(bases, k=6))
                nueva_matriz.append(fila)
            return nueva_matriz
        else:
            return self.adn       