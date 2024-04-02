
from lector.CSV import CSV
from lector.Estudiante import Estudiante

'''
    Clase Convertidor
    Clase que genera un archivo JSON a partir de un archivo CSV
'''
class Convertidor:
    '''
        Constructor de la clase Convertidor
        :param archivo: CSV
    '''
    def __init__(self, archivo: CSV):
        self.archivo = archivo

    '''
        Método generar
        Método que genera una lista de objetos Estudiante a partir de un archivo CSV
        :return list | None
    '''
    def __generarEstructuraJSON(self) -> list | None:
        informacion = self.archivo.leer()
        
        if informacion is not None:
            infoJSON = []
            for estudiante in informacion:
                id = estudiante.get("id")
                nombre = estudiante.get("nombre")
                apellido = estudiante.get("apellido")
                estudiante = Estudiante(id, nombre, apellido)
                infoJSON.append(estudiante.obtenerObjeto())
            return infoJSON
        else:
            return None
        
    '''
        Método convertir
        Método que convierte un archivo CSV a un archivo JSON
        :return str | None
    '''
    def convertir(self) -> str | None:
        info = self.__generarEstructuraJSON()

        if info is None:
            print("No se pudo leer el archivo, no existe o no se encuentra en la ruta especificada")
            return None
        
        newData = str(info).replace("'", '"')

        print(newData)

        with open(f'{self.archivo.getRuta().replace(".csv", ".json")}', 'w', encoding="utf-8") as archivo:
            archivo.write(str(newData))

        return newData
