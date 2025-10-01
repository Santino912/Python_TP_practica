import matplotlib.pyplot as plt
import requests
import csv


url_coffee_survey = "https://raw.githubusercontent.com/rfordatascience/tidytuesday/refs/heads/main/data/2024/2024-05-14/coffee_survey.csv"
archivo_salida_coffee_survey = "coffee_survey.csv"

def descargarCSV(url, archivo_salida):
    print("Descargando archivo...")
    consulta = requests.get(url)
    contenido = consulta.content

    print("Guardando archivo...")
    # Abrir conexion en modo escritura
    with open(archivo_salida, "w", encoding="utf-8") as archivo:
        # Escribir el contenido de la consulta
        archivo.write(contenido.decode("utf-8"))

    print("¡Archivo descargado con éxito!")

descargarCSV(url_coffee_survey,archivo_salida_coffee_survey)


# Defina una función que le sirva para manipular los datos del archivo

# Consigna 3: Analizar la columna 'age'
def contar_rangos_edad(nombre_archivo:str, nombre_columna:str) -> dict[str,int]:

  conteo = {} #Creamos un dict vacio para almacenar valor

  with open(nombre_archivo, 'r') as archivo: #Lector del archivo que deseamos leer y lo identificamos como 'archivo' y se guarda

    lector = csv.DictReader(archivo) #guardamos el resultado de la funcion DictReader en una variable

    for fila in lector: #bucle para recorrer el objeto lector
      edad = fila[nombre_columna]

      if edad == "NA": #si edad no tiene valor
        continue #sigue con la siguiente key


      elif edad in conteo: #si encuentra la key en el diccionario creado
        conteo[edad] += 1 #se suma

      else: #sino
        conteo[edad] = 1 #se crea una key con ese valor dentro del diccionario

  return conteo #retornamos el diccionario completo

# Prueba
#print("Conteo de rangos de edad:", contar_rangos_edad("coffee_survey.csv"))
#Respuesta:
# Conteo de rangos de edad: {'18-24 years old': 461, '25-34 years old': 1986,
# '35-44 years old': 960, '55-64 years old': 187, '<18 years old': 20, '>65 years old': 95, '45-54 years old': 302}

print("Conteo de rangos de edad:", contar_rangos_edad("coffee_survey.csv", "age"))



# Consigna 4: Analizar la columna 'where_drink'
def contar_lugares_consumo(nombre_archivo: str, nombre_columna: str) -> dict[str, int]:

    conteo = {}  # Diccionario donde se almacenarán los resultados

    # Abrimos el archivo CSV en modo lectura
    with open(nombre_archivo, 'r') as archivo:
        lector = csv.DictReader(archivo)  # Creamos un lector que interpreta cada fila como un diccionario

        # Iteramos sobre cada fila del archivo
        for fila in lector:
            # Obtenemos el valor de la columna indicada, que puede tener varios lugares separados por coma
            lugares = fila[nombre_columna].split(", ")

            # Iteramos sobre cada lugar en la lista de lugares
            for lugar in lugares:
                if lugar == "NA":      # Ignoramos los valores "NA" (no aplica/dato faltante)
                    continue
                elif lugar in conteo:  # Si el lugar ya está en el diccionario, sumamos uno al contador
                    conteo[lugar] += 1
                else:                  # Si es la primera vez que aparece, lo agregamos con valor 1
                    conteo[lugar] = 1

    return conteo  # Devolvemos el diccionario con los conteos


# Prueba
#print("Conteo de lugares de consumo:", contar_lugares_consumo("coffee_survey.csv"))

#Respuesta:
#Conteo de lugares de consumo: {'On the go': 705, 'At a cafe': 1170,
# 'At the office': 1430, 'At home': 3644, 'None of these': 36}
contar_lugares_consumo("coffee_survey.csv", "education_level")
{"Bachelor's degree": 1759,
 "Master's degree": 738,
 'Less than high school': 22,
 "Some college or associate's degree": 461,
 'Doctorate or professional degree': 340,
 'High school graduate': 118}


# Consigna 5: Función procesamiento_columna

def procesamiento_columna(nombre_archivo: str, nombre_columna: str) -> dict[str,int]:
  conteo = {}
  #completar para responder a la consigna

  # Abrimos el archivo CSV en modo lectura
  with open(nombre_archivo, 'r') as archivo:
    lector = csv.DictReader(archivo) # Creamos un lector que interpreta cada fila como un diccionario

    # Iteramos sobre cada fila del archivo
    for fila in lector: # Recorre los valores del objeto

      keys = fila[nombre_columna].split(", ") # Separa los valores que se encuentren dentro de la key

      for key in keys: #recorremos keys con un bucle

        if key == "NA": # Ignoramos los valores "NA" (no aplica/dato faltante)
          continue

        elif key in conteo: # Si el lugar ya está en el diccionario, sumamos uno al contador
          conteo[key] += 1

        else: # Si es la primera vez que aparece, lo agregamos con valor 1
          conteo[key] = 1


  return conteo # Devolvemos el diccionario con los conteos


# Prueba
#print("Conteo de rangos de edad:", procesamiento_columna("coffee_survey.csv","age"))
#print("Conteo de lugares de consumo:", procesamiento_columna("coffee_survey.csv","where_drink"))

#Respuestas:
#Conteo de rangos de edad: {'18-24 years old': 461, '25-34 years old': 1986, '35-44 years old': 960, '55-64 years old': 187, '<18 years old': 20, '>65 years old': 95, '45-54 years old': 302}
#Conteo de lugares de consumo: {'At a cafe': 1170, 'At the office': 1430, 'At home': 3644, 'On the go': 705, 'None of these': 36}



# Prueba
# Complete para que la respuestas sean las que figuran aqui debajo
print(procesamiento_columna("coffee_survey.csv","cups")) # Ejecutamos la funcion con el parametro "coffee_survey.csv","cups"
print(procesamiento_columna("coffee_survey.csv","brew")) # Ejecutamos la funcion con el parametro "coffee_survey.csv","brew"
#Respuestas esperadas:
#Conteo de cups: {'Less than 1': 348, '2': 1663, '1': 1277, '3': 473, 'More than 4': 67, '4': 121}
#Conteo de brew: {'Pod/capsule machine (e.g. Keurig/Nespresso)': 336, 'Bean-to-cup machine': 84, 'Coffee brewing machine (e.g. Mr. Coffee)': 663, 'Pour over': 2295, 'Espresso': 1518, 'French press': 735, 'Instant coffee': 130, 'Other': 677, 'Coffee extract (e.g. Cometeer)': 186, 'Cold brew': 525}



class Consumidor:
  #inicializamos la clase consumidor y utilizamos la funcion __init__ para recibir parametros
  def __init__(self, submission_id: str, age:str, gender:str, cups: str, where_drink: list[str], favorite: str, roast_level: str, caffeine: str, education_level:str, employment:str ):
    #guardamos los valores de los parametros
    self.submission_id = submission_id
    self.age = age
    self.gender = gender
    self.cups = cups
    self.where_drink = where_drink
    self.favorite = favorite
    self.roast_level = roast_level
    self.caffeine = caffeine
    self.education_level = education_level
    self.employment  = employment
  #creamos la funcion __str__ para devolver los valores de la clase como string
  def __str__(self):
    return f"submission_id {self.submission_id} age {self.age} gender {self.gender} cups {self.cups} where_drink  {self.where_drink} favorite {self.favorite} roast_level {self.roast_level} caffeine {self.caffeine} education_level  {self.education_level} employment {self.employment}"



def cargar_consumidores(archivo:str) -> dict[str, Consumidor]:

  dicc={}

  with open(archivo, 'r') as csvfile: #Lee el archivo y lo asigna a la variable "csvfile"

    #Usa la funcion DictReader del modulo csv para convertir el texto del archivo a un diccionario
    reader = csv.DictReader(csvfile)

    #Navega el diccionario creado
    for row in reader:

      # definimos los valores del diccionario creando una key 'submission_id' y como valor una instancia de la clase Consumidor, ej primer bucle:{"gMR29l": (clase)}
      dicc[row['submission_id']] = Consumidor(row['submission_id'], row['age'], row['gender'], row['cups'], row['where_drink'].split(','), row['favorite'], row['roast_level'], row['caffeine'], row['education_level'], row['employment_status'])

  return dicc


# dict[str, Consumidor] hace referencia a que recibe un diccionario con clave "str" o string y como valor una clase creada que se Consumidor
# algo como esto {"gMR29l": (clase), ..... }
def filtrar_por_atributo_valor(cons:dict[str, Consumidor], atributo:str, valor:str) -> dict[str, Consumidor]:

  dicc={}

  # Navega el diccionario de {str: (clase)}
  for key in cons:
    if getattr(cons[key], atributo) == valor:
      dicc[key] = cons[key]

  return dicc

#filtrar_por_atributo_valor(cargar_consumidores('coffee_survey.csv'),'age','25-34 years old')

# este seria "crear un diccionario que corresponda a los consumidores de género femenino (Female) cuya edad supere los 44 años"

obj = filtrar_por_atributo_valor(cargar_consumidores('coffee_survey.csv'),'gender','Female')

diccionario= filtrar_por_atributo_valor(obj,'age','45-54 years old')
diccionario1= filtrar_por_atributo_valor(obj,'age','55-64 years old')
diccionario2= filtrar_por_atributo_valor(obj,'age','>65 years old')
#'update' une diccionarios
diccionario.update(diccionario1)
diccionario.update(diccionario2)

print(diccionario)



def dibujar_grafico_torta(titulo, edades, porcentajes):
    # Dibuja un gráfico de torta (pie chart) usando matplotlib, mostrando la distribución porcentual de los grupos etarios.
    plt.figure(figsize = (12,12))
    plt.title(titulo, fontsize=25)
    plt.pie(porcentajes, labels=edades, autopct="%0.1f %%")  # Grafica la torta

def grafico_barras(titulo, etiquetas, cantCafe):
    #Dibuja un gráfico de barras usando matplotlib, mostrando cuántos consumidores prefieren cada tipo de café por grupo.
    plt.figure(figsize = (20,10))
    plt.title(titulo, fontsize=25)
    plt.bar(etiquetas, cantCafe)

class Encuesta:
    def __init__(self, archivo: str):
        #Inicializa la clase Encuesta y preprocesa varias métricas de interés a partir del archivo indicado.
        self.archivo = archivo  # Guarda el nombre/ruta del archivo
        self.consumidores = cargar_consumidores(archivo)  # Carga un diccionario de consumidores (objeto Consumidor)
        self.cantidades_grupos_etarios = self.analizar_rangos_edades()  # Calcula las cantidades por grupo etario
        self.cantidades_generos = self.analizar_generos()  # Calcula las cantidades por género
        self.cafe_favorito_por_grupo_etario = self.analizar_cafe_favorito_por_grupos_etarios()  # Calcula café favorito por edad
        self.nivel_de_tueste_preferido_por_genero = self.analizar_nivel_de_tueste_por_genero()  # Calcula tueste preferido por género
        self.maximo_nivel_educativo = self.calcular_maximo_nivel_educativo()  # Encuentra el nivel educativo máximo

    def analizar_rangos_edades(self) -> dict[str, int]:
        #Devuelve un conteo de los distintos grupos etarios presentes en el archivo de la encuesta.
        return procesamiento_columna(self.archivo, "age")

    def analizar_generos(self) -> dict[str, int]:
        #Devuelve un conteo de los distintos géneros presentes en el archivo de la encuesta.
        return procesamiento_columna(self.archivo, "gender")

    def analizar_cafe_favorito_por_grupos_etarios(self) -> dict[str, dict[str, int]]:
        #Devuelve un diccionario con la cantidad de consumidores que prefieren cada tipo de café, agrupados por edad.
        #Estructura: {edad: {cafe_favorito: cantidad}}
        test = {}
        for consumidor in self.consumidores:
            claseConsumidor = self.consumidores[consumidor]
            if claseConsumidor.age != "NA" and claseConsumidor.favorite != "NA":
                if claseConsumidor.age not in test:
                    test[claseConsumidor.age] = {}
                if claseConsumidor.favorite not in test[claseConsumidor.age]:
                    test[claseConsumidor.age][claseConsumidor.favorite] = 1
                else:
                    test[claseConsumidor.age][claseConsumidor.favorite] += 1
        return test

    def analizar_nivel_de_tueste_por_genero(self) -> dict[str, dict[str, int]]:
        #Devuelve un diccionario con la cantidad de consumidores que prefieren cada tipo de tueste, agrupados por género.
        #Estructura: {genero: {nivel_tueste: cantidad}}
        test = {}
        for consumidor in self.consumidores:
            claseConsumidor = self.consumidores[consumidor]
            if claseConsumidor.gender != "NA" and claseConsumidor.roast_level != "NA":
                if claseConsumidor.gender not in test:
                    test[claseConsumidor.gender] = {}
                if claseConsumidor.roast_level not in test[claseConsumidor.gender]:
                    test[claseConsumidor.gender][claseConsumidor.roast_level] = 1
                else:
                    test[claseConsumidor.gender][claseConsumidor.roast_level] += 1
        return test

    def calcular_maximo_nivel_educativo(self) -> str:
        #Devuelve un string que indica cuál es el nivel educativo que más se repite entre los encuestados.
        values = procesamiento_columna(self.archivo, "education_level")
        valorMaximo = 0
        keyMaximo = ""
        for key in values:
            if valorMaximo < values[key]:
                valorMaximo = values[key]
                keyMaximo = key
        return f"El maximo nivel educativo de la mayoria de personas que respondieron la encuesta es: {keyMaximo}"

    def graficar_grupos_etarios(self) -> None:
        #Realiza y muestra un gráfico de torta con la proporción de cada grupo etario en la encuesta.
        diccionarioGruposEtarios = procesamiento_columna(self.archivo, "age")
        titulo = "Grupos Etarios"
        dicc = {}
        valorTotal = sum(diccionarioGruposEtarios.values())

        # Calcula el porcentaje de cada grupo etario
        for key in diccionarioGruposEtarios:
            resultado = diccionarioGruposEtarios[key] / valorTotal
            dicc[key] = resultado

        edades = dicc.keys()
        porcentajes = dicc.values()
        dibujar_grafico_torta(titulo, edades, porcentajes)

    def graficar_cafe_favorito_por_grupos_etarios(self) -> None:
        #Dibuja un gráfico de barras para cada grupo etario, mostrando la preferencia de café de cada grupo.
        dicc = self.cafe_favorito_por_grupo_etario
        for grupEtario in dicc:
            grafico_barras(grupEtario, dicc[grupEtario].keys(), dicc[grupEtario].values())





#guardamos en una variable la instancia de la clase encuesta
encuesta1 = Encuesta("coffee_survey.csv")



#mostramos en pantalla los graficos
print(encuesta1.graficar_grupos_etarios())
print(encuesta1.graficar_cafe_favorito_por_grupos_etarios())
