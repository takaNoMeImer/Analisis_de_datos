# Carga de datos


```python
# Importacion de las librerias usadas.
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
```


```python
# Lectura de datos
datos = pd.read_csv('./online_retail_II.csv')
```

## 1 - Determinar el país que más productos consume
Usaremos las siguientes columnas
- Country: Pais
- Quantity: Cantidad


```python
consumo = datos.groupby("Country")["Quantity"].sum().idxmax()
```


```python
print("Pais que mas productos consume es: ", consumo)
```

    Pais que mas productos consume es:  United Kingdom
    


```python
print("Aqui podemos ver los paises y su consumo")
print(datos.groupby("Country")["Quantity"].sum().reset_index())
```

    Aqui podemos ver los paises y su consumo
                     Country  Quantity
    0              Australia     20053
    1                Austria      6479
    2                Bahrain      1015
    3                Belgium     11980
    4                Bermuda      2798
    5                 Brazil       189
    6                 Canada       894
    7        Channel Islands     10994
    8                 Cyprus      4371
    9                Denmark    227030
    10                  EIRE    188704
    11               Finland      3651
    12                France     74471
    13               Germany    107133
    14                Greece      6151
    15             Hong Kong      2306
    16               Iceland       828
    17                Israel      1132
    18                 Italy      7310
    19                 Japan      6604
    20                 Korea       598
    21               Lebanon        71
    22             Lithuania      2306
    23                 Malta      1547
    24           Netherlands    181823
    25               Nigeria        56
    26                Norway      7863
    27                Poland      1991
    28              Portugal     11878
    29                   RSA      1618
    30             Singapore      1753
    31                 Spain     18332
    32                Sweden     52238
    33           Switzerland     22053
    34              Thailand      2552
    35                   USA      2666
    36  United Arab Emirates      5746
    37        United Kingdom   4429046
    38           Unspecified      3416
    39           West Indies       395
    

## 2 - Identificar los productos más vendidos o los más populares en términos de ganancias o cantidad de ventas.

Primero vamos a crear una nueva columna en el dataset.
- Profits: Quantity * Price

Luego sacamos los productos en terminos de ganancias y ventas


```python
datos["Profits"] = datos["Quantity"] * datos["Price"]
```


```python
productos_vendidos_profits = datos.groupby("Description")["Profits"].sum().reset_index()

productos_vendidos_profits = productos_vendidos_profits.sort_values(by="Profits", ascending=False)
```


```python
productos_vendidos_quantity = datos.groupby("Description")["Quantity"].sum().reset_index()

productos_vendidos_quantity = productos_vendidos_quantity.sort_values(by="Quantity",ascending=False)
```


```python
print("Mas vendidos por ganancias:")
print(productos_vendidos_profits.head())

print("\nMas vendidos por cantidad:")
print(productos_vendidos_quantity.head())
```

    Mas vendidos por ganancias:
                                 Description    Profits
    3371            REGENCY CAKESTAND 3 TIER  163051.46
    4402  WHITE HANGING HEART T-LIGHT HOLDER  157865.43
    1297                      DOTCOM POSTAGE  116401.99
    279        ASSORTED COLOUR BIRD ORNAMENT   72454.12
    2780     PAPER CHAIN KIT 50'S CHRISTMAS    57870.20
    
    Mas vendidos por cantidad:
                                 Description  Quantity
    4402  WHITE HANGING HEART T-LIGHT HOLDER     57733
    4509   WORLD WAR 2 GLIDERS ASSTD DESIGNS     54698
    721                  BROCADE RING PURSE      47647
    2744    PACK OF 72 RETRO SPOT CAKE CASES     46106
    279        ASSORTED COLOUR BIRD ORNAMENT     44925
    

## 3 - Detectar patrones y tendencias, por ejemplo, identificar si hay picos de ventas durante ciertos meses del año.

### Aqui lo que podemos hacer es usar pandas para convertir la columna InvoiceDate en un datetime y poder trabajar con ella.


```python
datos["InvoiceDate"] = pd.to_datetime(datos["InvoiceDate"])

# Creamos la columna Month para almacenar el mes correspondiente
datos["Month"] = datos["InvoiceDate"].dt.month
```

Ahora simplemente sumamos las ventas para cada mes.


```python
ventas_mes = datos.groupby("Month")["Quantity"].sum().reset_index()
```


```python
print(ventas_mes)
```

        Month  Quantity
    0       1    375363
    1       2    368402
    2       3    489370
    3       4    351971
    4       5    364095
    5       6    388253
    6       7    302201
    7       8    451803
    8       9    478262
    9      10    601729
    10     11    673856
    11     12    586736
    

Aqui usamos matplotlib para poder visualizar los datos de mejor manera.


```python
plt.figure(figsize=(10, 6))
plt.plot(ventas_mes["Month"], ventas_mes["Quantity"])
plt.xlabel("Mes")
plt.ylabel("Ventas")
plt.title("Picos de Ventas por Mes")
plt.xticks(range(1, 13))
plt.show()

```


    
![png](/images/output_18_0.png)
    


#### Podemos hacer otro tipo de analisis para ver los picos de ventas por dia

Como ya hemos transformado InvoiceDate, podemos trabajar mas facilmente con el


```python
datos["Hour"] = datos["InvoiceDate"].dt.hour
ventas_por_hora = datos.groupby("Hour")["Quantity"].sum().reset_index()
```


```python
plt.figure(figsize=(10, 6))
plt.plot(ventas_por_hora["Hour"], ventas_por_hora["Quantity"])
plt.xlabel("Hora del día")
plt.ylabel("Ventas")
plt.title("Patrones diarios de ventas")
plt.xticks(range(24))
plt.show()
```


    
![png](/images/output_21_0.png)
    


## 4 - Análisis de correlación para determinar la relación entre las variables, por ejemplo, si existe una correlación entre el precio y la cantidad de ventas

Usamos las columnas:
- Price
- Quantity


```python
cols = ["Price", "Quantity"]
interes = datos[cols]
```


```python
correlacion = interes.corr()
```


```python
print(correlacion)
```

                 Price  Quantity
    Price     1.000000 -0.001931
    Quantity -0.001931  1.000000
    

##### Usamos seanborn ya que este nos provee de mapas de calor para poder visualizar mas adecuadamente la correlacion


```python
sns.heatmap(correlacion, annot=True, cmap="coolwarm")
plt.title("Analisis de Correlacion")
plt.show()
print("No hay correlacion entre el precio y la cantidad de ventas de productos")
```


    
![png](/images/output_28_0.png)
    


    No hay correlacion entre el precio y la cantidad de ventas de productos
    
