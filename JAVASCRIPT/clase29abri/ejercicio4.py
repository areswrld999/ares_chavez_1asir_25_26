import pandas as pd

# Tus listas
Nombres= ["Ana","Luis","Pedro"]
Edades = [25,30,35]

# Crear un diccionario
datos = {"Nombres": Nombres, "Edades": Edades}

# Convertir a DataFrame
df = pd.DataFrame(datos)

# Exportar a Excel
df.to_excel("datos.xlsx", index=False)
print("Archivo Excel generado con éxito")