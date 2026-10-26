
#pip install pandas
#pip install openpyxl
import matplotlib.pyplot as plt
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
#print(ventas)
print(f"\n=== Facturación por barrio del mes {nombre_planilla} ===")
por_barrio=ventas.groupby("Barrio")["Facturacion"].sum()
print(por_barrio.to_frame)
plt.pie(por_barrio,labels=por_barrio.index, autopct="%1.1f%%")
#plt.title("Compras de cada Barrio")
#plt.savefig("torta_sucursales.pdf")
plt.show()