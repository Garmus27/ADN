import random
from typing import List, Optional

class ADN:
    """Pensamos conveniente crear una clase ADN, para seguir con el concepto de que en python todo es un objeto
    """
    def __init__(self):
        self.bases: List[str] = ['A', 'T', 'C', 'G']
        self.matriz: List[str] = []

    def crearADN(self) -> List[str]:
        self.matriz = []
        for _ in range(6):
            fila = ''.join(random.choices(self.bases, k=6))
            self.matriz.append(fila)
        return self.matriz
        """El metodo crear adn, crea una matriz que representa una secunecua de ADN
        """

    def mostrar_matriz(self, matriz: List[str]) -> None: 
        for fila in matriz:
            print("  ".join(fila))
        print()
        """ metodo para mostrar la matriz
        """

class Detector:
    def __init__(self, adn: List[str]):
        self.__base_nitrogenada: Optional[str] = None
        self.__tipo_mutacion: Optional[str] = None
        self.__encontrado: bool = False
        self.adn: List[str] = adn
        self.base_map: dict = {
            'A': 'Adenina',
            'T': 'Timina',
            'C': 'Citosina',
            'G': 'Guanina'}
       
        
    """metodo deteccion horizontal detecta si hay alguna mutacion horizontal, si la encuentra actualiza el atributo tipo_mutacion a RADIACION"
    """
    def deteccion_horizontal(self) -> None:
        for fila in self.adn:
            if self.__detectar_mutacion(fila):
                self.__tipo_mutacion = "RADIACION"
                return    
            
    """metodo deteccion vertical detecta si hay alguna mutacion vertical, si la encuentra actualiza el atributo tipo_mutacion a RADIACION"
    """
    def deteccion_vertical(self) -> None:
        for col in range(6):
            columna = ''.join([self.adn[fila][col] for fila in range(6)])
            if self.__detectar_mutacion(columna):
                self.__tipo_mutacion = "RADIACION"
                return
            
            
    """metodo deteccion diagonal detecta si hay alguna mutacion diagonal, si la encuentra actualiza el atributo tipo_mutacion a VIRUS"
        """
    def deteccion_diagonal(self) -> None:
        for start in range(-5, 6):
            diagonal1 = ''.join([self.adn[i][i-start] for i in range(6) if 0 <= i-start < 6])
            diagonal2 = ''.join([self.adn[i][5-i+start] for i in range(6) if 0 <= 5-i+start < 6])
            if self.__detectar_mutacion(diagonal1) or self.__detectar_mutacion(diagonal2):
                self.__tipo_mutacion = "VIRUS"
                return

        """creamos el metodo que ejecutara todas las detecciones
        """
    def detectar_mutaciones(self) -> bool:
        self.deteccion_horizontal()
        if not self.__encontrado:
            self.deteccion_vertical()
        if not self.__encontrado:
            self.deteccion_diagonal()
        return self.__encontrado


        """este metodo mostrar da mas legibilidad e informacion al usuario cuando se ha encontrado una mutacion, nos dice el tipo de mutacion, usando un map"
        """
    def mostrar(self) -> str:
        if self.__encontrado:
            base_mutada = ', '.join([f"{base}: {nombre}" for base, nombre in self.base_map.items() if base == self.__base_nitrogenada])
            return f"Este ADN ha sido mutado\nTipo de mutación: {self.__tipo_mutacion}\nBase nitrogenada mutada: {base_mutada}"
        else:
            return "No se han encontrado mutaciones"

    """metodo privado detectar_mutacion se encarga de ver en una sola secuencia si hay un patron de 4 cadenas repetidas aledañas, y es utilizado en los metodos de deteccion
    se penso conveniente separarlo por una cuestion de modularizacion, para poder ser reutilizado"""
    def __detectar_mutacion(self, secuencia: str) -> bool:
        for base in ['A', 'T', 'C', 'G']:
            if base * 4 in secuencia:
                self.__base_nitrogenada = base
                self.__encontrado = True
                return True
        return False

class Mutador:
    """creacion de la clase mutador con los atributos requeridos y el metodo crear mutante vacio """
    def __init__(self, base_nitrogenada: Optional[str], horientacion: Optional[str], coordenada_inicial: Optional[tuple]):
        self.base_nitrogenada: Optional[str] = base_nitrogenada
        self.horientacion: Optional[str] = horientacion
        self.coordenada_inicial: Optional[tuple] = coordenada_inicial

    def crear_mutante(self):
        pass

class Radiacion(Mutador):
    def __init__(self, base_nitrogenada: Optional[str], horientacion: Optional[str], coordenada_inicial: Optional[tuple]):
        super().__init__(base_nitrogenada, horientacion, coordenada_inicial)

    def crear_mutante(self, matriz: List[str]) -> List[str]:
        while True:
            try:
                """comienzo del menu, pidiendo la base nitrogenada con la que se creara la mutacion"""
                """ se valida mayusculas y minusculas, y el try captura el error si se ingresa una opcion no valida"""
                base_nitrogenada = input("Ingrese la base nitrogenada (A, T, C, G): ").upper()
                if base_nitrogenada not in ['A', 'T', 'C', 'G']:
                    raise ValueError("Base nitrogenada no válida")

                """ Siguiente punto se pide que se ingrese la coordenada donde iniciara la mutacion y se valida que la coordenada no exeda los limites de la matriz"""
                fila, columna = map(int, input("Ingrese la coordenada inicial (fila, columna) separada por una coma: ").split(","))
                if not (0 <= fila < 6 and 0 <= columna < 6):
                    raise ValueError("Coordenada fuera de rango")
                
                """se pide que se ingrese la horientacion y se valida mayusculas y minusculas, y que la opcion sea una opcion valida"""
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

        """se actualizan los valores de la la clase radiacion """
        self.base_nitrogenada = base_nitrogenada
        self.horientacion = orientacion
        self.coordenada_inicial = (fila, columna)
        
        """se procede a crear la mutacion horizontal o vertical dependiendo de la opcion ingresada"""
        if self.horientacion == 'H':
            for i in range(4):
                matriz[fila] = matriz[fila][:columna + i] + self.base_nitrogenada + matriz[fila][columna + i + 1:]
        else:
            for i in range(4):
                matriz[fila + i] = matriz[fila + i][:columna] + self.base_nitrogenada + matriz[fila + i][columna + 1:]

        return matriz

class Virus(Mutador):
    def __init__(self, base_nitrogenada: Optional[str], horientacion: Optional[str], coordenada_inicial: Optional[tuple]):
        super().__init__(base_nitrogenada, horientacion, coordenada_inicial)
        
    """se crea la clase virus """
    def crear_mutante(self, matriz: List[str]) -> List[str]:
        while True:
            try:
                """ se procede a comenzar con el menu de igual manera que en la clase Radiacion"""
                base_nitrogenada = input("Ingrese la base nitrogenada (A, T, C, G): ").upper()
                if base_nitrogenada not in ['A', 'T', 'C', 'G']:
                    raise ValueError("Base nitrogenada no válida")

                fila, columna = map(int, input("Ingrese la coordenada inicial (fila, columna) separada por una coma: ").split(","))
                if not (0 <= fila < 6 and 0 <= columna < 6):
                    raise ValueError("Coordenada fuera de rango")

                """aqui encontramos diferenciac con la clase anterior, la horientacion puede ser ascendente o descendente"""
                orientacion = input("Ingrese la orientación de la mutación (A para ascendente, D para descendente): ").upper()
                if orientacion not in ['A', 'D']:
                    raise ValueError("Orientación no válida")

                """en esta parte se verifica que la mutacion sea creada hacia donde no exeda el limite de la matriz"""
                """ por ejemplo si el comienzo de la matriz es 2,1 se creara hacia abajo y hacia la derecha porque si fuera hacia la izquierda se crearia fuera de los limites de la matriz"""
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

        """ se procede a actualizar los valores de los atribtuos de la clase virus"""
        self.base_nitrogenada = base_nitrogenada
        self.horientacion = orientacion
        self.coordenada_inicial = (fila, columna)
        
        """ se crea la mutacion  segun los valores ingresados"""
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

    """ aqui la clase sanador utiliza la funcion mutaciones detectadas de la clase detector para verificar """
    def sanar_mutantes(self):
        detector = Detector(self.adn)
        self.mutaciones_detectadas = detector.detectar_mutaciones()
        
        """ este metodo revisa que la nueva cadena de adn no posea mutaciones y si encuentra una mutacion, cambia las cadenas repetidas por unas aleatorias eliminando la mutacion"""
        if self.mutaciones_detectadas:
            nueva_matriz = []
            bases = ['A', 'T', 'C', 'G']
            for _ in range(6):
                fila = ''.join(random.choices(bases, k=6))
                nueva_matriz.append(fila)
            return nueva_matriz
        else:
            return self.adn       