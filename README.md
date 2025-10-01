# Python_TP_practica
Trabajo Práctico: La Gran Prueba de Sabor

Consignas

Etapa 0.
Conociendo los datos

1- Descargar el archivo de la encuesta ejecutando el código que se propone a continuación.

2- Una vez descargado el archivos analice su contenido. ¿Qué información brinda de cada persona encuestada? ¿Todos los encuestados respondieron a todas las preguntas?
3- Analice la columna 'age' que indica el rango de edad del encuestado. ¿Qué cantidad de los encuestados que brindaron esta información pertenecen a los rangos '<18 years old'*, *'18-24 years old'*, *'25-34 years old'*, *'35-44 years old'*, *'45-54 years old'*, *'55-64 years old'* y *'>65 years old', respectivamente? Para responder a esta pregunta implemente una función contar_rangos_edad que reciba el nombre del archivo de datos de la encuesta y devuelva un diccionario que le ayude a contar la cantidad de respuestas de cada rango etario.

4- Analice la columna 'where_drink' que indica dónde toman café los encuestados. ¿Qué diferencia encuentra entre esta columna de la anterior? ¿Qué cantidad de los encuestados que respondieron a esta pregunta toman el café 'On the go', 'At a cafe', 'At the office', 'At home', 'None of these', respectivamente? Para responder a esta pregunta implemente una función contar_lugares_consumo que reciba el nombre del archivo de datos de la encuesta y devuelva un diccionario que le ayude a contar la cantidad de respuestas de cada lugar de consumo.
5- Analicen los códigos propuestos para responder a las consignas 3 y 4. Son similares, ¿verdad? Proponga una función procesamiento_columna, que recibiendo el nombre del archivo y el nombre de la columna a analizar, sirva para resolver los dos casos anteriores. La función debe devolver un diccionario con las cantidades asociadas a cada uno de los valores posibles de las respuestas brindadas por los encuestados.


6- Pruebe la función anterior, analizando las columnas 'cups' y 'brew'. ¿Funciona?


Etapa 2.
Carga de la Información de los Consumidores

7- Definir una clase Consumidor que tenga los siguientes

Atributos:

submission_id: Identificador único del consumidor.

age: Rango de edad (str).

gender: Género (str).

cups: Número de tazas que consume por día (str).

where_drink: Lugares donde consume café (list[str]).

favorite: Café preferido (str).

roast_level: Nivel de tueste (str).

caffeine: Tipo de cafeína (str).

education_level: Nivel de educación (str).

employment_status: Estado o situación laboral (str).

Métodos:

__init__: Para inicializar los atributos.

__str__: Para representar al consumidor de manera legible.

Complete el siguiente código. Agregue todos los argumentos que necesite a los métodos.
8- Implemente una función llamada cargar_consumidores que reciba como argumento el nombre del archivo de la encuesta y devuelva un diccionario donde la clave sea el submission_id (ID del consumidor) y el valor sea una instancia de la clase Consumidor.

9- Implemente una función llamada filtrar_por_atributo_valor que reciba un diccionario de consumidores como el creado en el punto anterior, un nombre de atributo (cualquiera de los atributos presentes en la clase Consumidor) y un valor de dicho atributo como argumentos. La función debe recorrer el diccionario y filtrar los consumidores, devolviendo otro diccionario cuyos consumidores hayan pasado el filtro aplicado.

10- Invocando a las funciones anteriores, ¿podría crear un diccionario que corresponda a los consumidores de género femenino (Female) cuya edad supere los 44 años?

Etapa 3.
Análisis de la Encuesta

En esta sección, nos proponemos obtener información relevante sobre las preferencias de los consumidores, considerando diferentes criterios como el rango etario y el género.

Desarrolle una clase en Python que permita gestionar las respuestas de la encuesta sobre preferencias de café. Esta clase será capaz de almacenar, analizar y visualizar datos relacionados con las preferencias de café de distintos consumidores, agrupándolos por rangos de edad y género.

Nota: En los análisis que realice, deberá considerar únicamente las respuestas proporcionadas, ignorando los valores NA.
11- Definir una clase Encuesta que tenga los siguientes

Atributos:

consumidores: Diccionario que almacena los datos de los consumidores que respondieron a la encuesta. La clave es el submission_id (ID del consumidor) y el valor es una instancia de la clase Consumidor

cantidades_grupos_etarios: Diccionario que contiene la cantidad de consumidores en cada grupo etario. La clave es el grupo etario y el valor es la cantidad de consumidores que respondieron a la encuesta en ese grupo.

cantidades_generos: Diccionario que refleja la cantidad de consumidores de cada género. La clave es el género y el valor es la cantidad de consumidores que respondieron a la encuesta de ese género.

cafe_favorito_por_grupo_etario: Diccionario que tiene como claves cada uno de los grupos etarios y como valor otro diccionario. Este último tiene como claves los cafés favoritos y como valor la cantidad de consumidores que prefieren ese café dentro de ese grupo etario.

nivel_de_tueste_preferido_por_genero: Diccionario que contiene como claves cada uno de los géneros y como valor otro diccionario. Este segundo diccionario tiene como claves los niveles de tueste preferidos y como valor la cantidad de consumidores que prefieren ese nivel de tueste para el género considerado.

maximo_nivel_educativo: El nivel educativo al que pertenece la mayor parte de los consumidores que respondieron a la encuesta.

Métodos:

__init__: Para inicializar los atributos.

analizar_rangos_edades: Método que cuenta la cantidad de consumidores en cada rango etario.

analizar_generos: Método que cuenta la cantidad de consumidores de cada género.

analizar_cafe_favorito_por_grupos_etarios: Método que, para cada grupo etario, cuenta cuántos consumidores prefieren cada tipo de café.

analizar_nivel_de_tueste_por_genero: Método que, para cada género, cuenta cuántos consumidores prefieren cada nivel de tueste.

calcular_maximo_nivel_educativo: Método que calcula el nivel educativo que posee la mayor cantidad de consumidores.

graficar_grupos_etarios: Método que realiza un gráfico de torta que muestra el porcentaje de consumidores pertenecientes a cada grupo etario.

graficar_cafe_favorito_por_grupos_etarios: Método que realiza un gráfico de barras para cada grupo etario, mostrando cuántos consumidores prefieren cada tipo de café.

12- Cree un objeto de tipo Encuesta y cargue los datos del archivo coffee_survey.csv.

13- Conclusiones:

Realice un análisis exhaustivo de los datos cargados en el objeto de tipo Encuesta recién creado. ¿Qué información relevante se puede extraer? Puede ayudarse de métodos del objeto para ver los gráficos o imprimir en pantalla información de este objeto. Reflexione sobre las conclusiones que se pueden obtener a partir de esta información.

Además, ¿qué recomendaciones ofrecería a su cliente para optimizar su cafetería? Por ejemplo, ¿a qué segmentos de clientes debería orientar su campaña de marketing para maximizar el impacto y atraer a más consumidores?

¿qué recomendaciones ofrecería a su cliente para optimizar su cafetería? Por ejemplo, ¿a qué segmentos de clientes debería orientar su campaña de marketing para maximizar el impacto y atraer a más consumidores?

Que Oriente su marketing a los clientes de entre 25 y 44 años y que promocione la venta de pourover ya que esta es la mas vendida en estos rangos de edad












