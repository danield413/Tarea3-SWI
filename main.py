
from lector.CSV import CSV
from lector.Convertidor import Convertidor

#* ------------------ Pruebas -------------------

#* Prueba 1
archivoCSV = CSV("./archivos/estudiantes.csv")
convertidor = Convertidor( archivoCSV )

convertidor.convertir()

print("\n")

#* Prueba 2
archivoCSV = CSV("./archivos/xyz.csv")
convertidor = Convertidor( archivoCSV )

convertidor.convertir()
