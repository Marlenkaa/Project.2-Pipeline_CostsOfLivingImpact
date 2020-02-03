# *Costs of Living vs. Happiness

El objetivo de este proyecto es crear un pipeline que muestre la relación entre el coste de vida y el índice de felicidad por país.

### EXTRACCIÓN DE DATOS

1. Indice de felicidad por país reportado para el año 2019 (INPUT/2019.csv): https://www.kaggle.com/unsdsn/world-happiness#2019.csv
2. Web scraping para obtener una tabla con precios de diferentes costes de vida y el salario medio neto mensual por país (webScraping_CostOfLife.ipynb): https://www.numbeo.com/cost-of-living/prices_by_country.jsp


### DATA CLEANING

cleaning.py(scr) -> funciones que recogen la limpieza y organización de datos de ambas tablas. Resumen:

    - Se ha renombrado columnas para un uso más cómodo de los parámetros.
    - Se ha creado una nueva columna 'supermarket' resultante de la suma de productos de supermercado simulando una cesta de la compra. De esta manera simplificamos columnas
    - Se retira del análisis a Venezuela, que debido a su situación económica, genera grandes desviaciones en los datos.
    - Se fusiona las dos tablas para incluir el índice de felicidad.
    - Se reorganiza la tabla final para obtener el porcentaje de sueldo que supone cada coste.
    
### ANALYSIS
    
analysis.py(scr) -> funciones que recogen el análisis de los datos. Resumen:

    - Se compara el coste sobre salario de cada país con la media de coste de los 96 países analizados.
    - Se compara el índice de felicidad de cada país con la media del índice de felicidad de los 96 países analizados.
    - Se muestra un diagrama de dispersión que busca la relación entre el coste elegido y el índice de felicidad para cada uno de los países.
    
### OUTPUT

pdf.py(scr) -> función para la creación de un pdf con la información analizada.
output.py(scr) -> función que contiene todas las funciones anteriores para automatizar y ejecutar el proceso en un único paso.
main.py(scr) -> contiene la configuración del pipeline


## HOW IT WORKS:

Comando: *python3 main.py -x Spain -y fitness

*-x identifica el país elegido.
*-y identifica el coste elegido.

Es necesario que el país se indique con la primera letra en mayúscula y el tipo de coste con todas las letras en minúscula (a mejorar).

Resultado: se genera un archivo pdf en la carpeta OUTPUT con el resultado de los argumentos introducidos.

##### A MEJORAR:

    - Incluir una línea de tendencia en el diagrama de dispersión.
    - Gestionar los posibles errores al introducir valores en la terminal, como aceptar tanto mayúsculas como minúsculas, lanzar un mensaje de error con texto de ayuda en caso de introducir un país no analizado o un parámetro diferente...
    - Mejor diseño del pdf.
