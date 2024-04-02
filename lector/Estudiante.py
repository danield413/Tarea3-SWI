'''
    Clase Estudiante
    Clase que representa un estudiante con sus atributos id, nombre y apellido
'''
class Estudiante:

    '''
        Constructor de la clase Estudiante
        :param id: str
        :param nombre: str
        :param apellido: str
    '''
    def __init__(self, id: str, nombre: str, apellido: str):
        self.__id = id
        self.__nombre = nombre
        self.__apellido = apellido


    '''Getters de la clase Estudiante'''
    def getId(self) -> str:
        return self.__id
    
    def getNombre(self) -> str:
        return self.__nombre
    
    def getApellido(self) -> str:
        return self.__apellido

    '''
        Método obtenerObjeto
        Método que retorna un diccionario con los atributos de la clase Estudiante
        :return dict
    '''
    def obtenerObjeto(self) -> dict:
        return {
            "id": self.__id,
            "nombre": self.__nombre,
            "apellido": self.__apellido
        }

    def __str__(self) -> str:
        return f'{self.id}, {self.nombre}, {self.apellido}'