
#pip install pandas
#pip install openpyxl

import pandas as pd
nombre_planilla=input("Ingrese el nombre de la planilla ")
ventas=pd.read_excel(nombre_planilla,sheet_name="Ventas")
#print(ventas.head(7))
#print(ventas.tail(7))
#print(ventas.info())
#print(ventas.describe())
#print(ventas["Precio_Unitario"])
ventas["Facturacion"]=ventas["Precio_Unitario"]*ventas["Unidades"]
#print(ventas["Facturacion"])
print(f"\n=== Totales de {nombre_planilla} ===")
print(f"Unidades Vendidas: {ventas["Unidades"].sum()}")
print(f"Total: ${ventas["Facturacion"].sum()}")
negocios=pd.read_excel(nombre_planilla,sheet_name="Negocios")
ventas=ventas.merge(negocios, on="Negocio", how="left")
print(ventas)
