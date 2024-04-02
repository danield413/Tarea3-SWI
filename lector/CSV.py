
import csv

'''
    Clase CSV
    Clase que lee un archivo CSV
'''
class CSV:

    '''
        Constructor de la clase CSV
        :param ruta: str
    '''
    def __init__(self, ruta: str):
        self.__ruta = ruta

    '''Getter de la clase CSV'''
    def getRuta(self):
        return self.__ruta

    '''
        Método leer
        Método que lee un archivo CSV y retorna una lista con la información del archivo
        :return list | None
    '''    
    def leer(self) -> list | None:

        try:
            info = []   
            with open(self.__ruta, newline='', encoding="utf-8") as archivo:
                lector = csv.DictReader(archivo)
                for linea in lector:
                    info.append(linea)
            return info   
        except FileNotFoundError:
            return None

    def __str__(self) -> str:
        return f'{self.__ruta}'
            