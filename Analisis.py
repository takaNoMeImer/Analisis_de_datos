# Importacion de las librerias usadas.
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

datos = pd.read_csv('./online_retail_II.csv')

# 1 - Determinar el país que más productos consume
consumo = datos.groupby("Country")["Quantity"].sum().idxmax()
print("Pais que mas productos consume es: ", consumo)

print("Aqui podemos ver los paises y su consumo")
print(datos.groupby("Country")["Quantity"].sum().reset_index())


# 2 - Identificar los productos más vendidos o los más populares en términos de ganancias o cantidad de ventas.

    # Primero vamos a crear una nueva columna en el dataset.
    # - Profits: Quantity * Price
    # Luego sacamos los productos en terminos de ganancias y ventas


datos["Profits"] = datos["Quantity"] * datos["Price"]

productos_vendidos_profits = datos.groupby("Description")["Profits"].sum().reset_index()

productos_vendidos_profits = productos_vendidos_profits.sort_values(by="Profits", ascending=False)

productos_vendidos_quantity = datos.groupby("Description")["Quantity"].sum().reset_index()

productos_vendidos_quantity = productos_vendidos_quantity.sort_values(by="Quantity",ascending=False)

print("Mas vendidos por ganancias:")
print(productos_vendidos_profits.head())

print("\nMas vendidos por cantidad:")
print(productos_vendidos_quantity.head())


# 3 - Detectar patrones y tendencias, por ejemplo, identificar si hay picos de ventas durante ciertos meses del año.

    # Aqui lo que podemos hacer es usar pandas para convertir la columna InvoiceDate en un datetime y poder trabajar con ella.

datos["InvoiceDate"] = pd.to_datetime(datos["InvoiceDate"])
    # Creamos la columna Month para almacenar el mes correspondiente
datos["Month"] = datos["InvoiceDate"].dt.month
    # Ahora simplemente sumamos las ventas para cada mes.
ventas_mes = datos.groupby("Month")["Quantity"].sum().reset_index()
print(ventas_mes)


    # Aqui usamos matplotlib para poder visualizar los datos de mejor manera.
plt.figure(figsize=(10, 6))
plt.plot(ventas_mes["Month"], ventas_mes["Quantity"])
plt.xlabel("Mes")
plt.ylabel("Ventas")
plt.title("Picos de Ventas por Mes")
plt.xticks(range(1, 13))
plt.show()

    # Podemos hacer otro tipo de analisis para ver los picos de ventas por dia
    # Como ya hemos transformado InvoiceDate, podemos trabajar mas facilmente con el

datos["Hour"] = datos["InvoiceDate"].dt.hour
ventas_por_hora = datos.groupby("Hour")["Quantity"].sum().reset_index()

plt.figure(figsize=(10, 6))
plt.plot(ventas_por_hora["Hour"], ventas_por_hora["Quantity"])
plt.xlabel("Hora del día")
plt.ylabel("Ventas")
plt.title("Patrones diarios de ventas")
plt.xticks(range(24))
plt.show()


# 4 - Análisis de correlación para determinar la relación entre las variables, por ejemplo, si existe una correlación entre el precio y la cantidad de ventas

    # Usamos las columnas:
    # - Price
    # - Quantity

cols = ["Price", "Quantity"]
interes = datos[cols]
correlacion = interes.corr()

print(correlacion)

    # Usamos seanborn ya que este nos provee de mapas de calor para poder visualizar mas adecuadamente la correlacion
sns.heatmap(correlacion, annot=True, cmap="coolwarm")
plt.title("Analisis de Correlacion")
plt.show()
print("No hay correlacion entre el precio y la cantidad de ventas de productos")