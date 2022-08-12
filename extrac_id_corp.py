import pandas as pd #pip install pandas 
from pytube import extract #pip install pytube 
from youtube_transcript_api import YouTubeTranscriptApi #pip install youtube_transcript_api


archivo_excel = pd.read_excel(r"") #Hay que definir ruta del archivo excel después de r"

#print(archivo.columns) <-- Verifica las columnas 

values_url = archivo_excel["URL"].values

urls = [i for i in values_url]

lista_ids = []

try: 
    for url in urls:
        id = extract.video_id(url)  
        lista_ids.append(id)
        #print(id) <-- checa cada una de las id
except TypeError: 
    print("He terminado de extraer ids de urls del excel... :)") 

#print(lista_ids) <-- Imprime los ids, si lo deseas 

print("----------------------------------------------------------")
print("Escribe un número entre 0 y " + str(len(lista_ids)-1))

continuar = False

while not continuar: 
    try:
        numero_transcripcion = int(input())
        transcribir = YouTubeTranscriptApi.get_transcript(lista_ids[numero_transcripcion], languages = ['es']) 
        #print(transcribir)
        continuar = True
    except ValueError:
        print("Vuelve a intentarlo de nuevo")

print("----------------------------------------------------------")
print("Ahora guardaremos el texto... ")
print("----------------------------------------------------------")

nombre_de_texto = input("Elige un nombre para guardarlo: ")

with open(nombre_de_texto, "w",  encoding="utf-8") as f:
    for i in transcribir:
        f.write("{}\n".format(i)) 

print("El programa ha terminado :)") 

       
