from nltk import text
from sklearn.feature_extraction.text import CountVectorizer
from tkinter import *
import tkinter as tk
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

import nltk
from nltk.tokenize import RegexpTokenizer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.probability import FreqDist
from nltk.stem.wordnet import WordNetLemmatizer
import jieba.analyse  # Importar biblioteca de extracción de palabras clave
import pandas as pd  # Importar pandas

def palabras_clave_contexto():
    data='Como trabajo denominamos al conjunto de actividades que son realizadas con el objetivo de alcanzar una meta, solucionar un problema o producir bienes y servicios para atender las necesidades humanas. Es toda actividad humana libre, ya sea material o intelectual, permanente o transitoria, que una persona natural ejecuta conscientemente al servicio de otra, y cualquiera que sea su finalidad, siempre que se efectúe en ejecución de un contrato de trabajo.El trabajo es el esfuerzo realizado por los seres humanos con la finalidad de producir riqueza. Desde el punto de vista teórico, este tópico ha sido abordado desde diferentes aristas, ya sean económicas, sociales o históricas, principalmente a causa de sus relevantes alcances en lo que hace el desarrollo de la humanidad.'
    tokenizer = RegexpTokenizer(r'\w+')
    text = tokenizer.tokenize(data)
    text = ' '.join(word for word in text)
    tokenized_word=word_tokenize(text)
    tokenized_word = [word.lower() for word in tokenized_word]

    stop_words = set(stopwords.words('Spanish'))
    all_stopwords = stopwords.words('Spanish')
    all_stopwords.append('si')
    all_stopwords.append('min')
    all_stopwords.append('tan')
    all_stopwords.append('trabajo')
#print(stop_words)

#filtrado de palabras que estan en stopword

    filtered_word = []
    for word in tokenized_word:
        if word not in all_stopwords:
            filtered_word.append(word)

    string_data =str(filtered_word)
    string_data = "".join(string_data)
    print(string_data)

    def get_key_words(string_data, how=''):
    # topK: El número de palabras clave extraídas, si no se especifica, se extraerán todas;
    # withWeight: establezca True para especificar el peso IF-IDF correspondiente a la palabra de salida
        if how == 'textrank':
        # Use el algoritmo TextRank
            tags_pairs = jieba.analyse.textrank(string_data,  topK=15,  withWeight=True)  # Extraer etiquetas de palabras clave
        else:
        # Utilice el algoritmo TF-IDF
            tags_pairs = jieba.analyse.extract_tags(string_data,  topK=15,  withWeight=True)  # Extraer etiquetas de palabras clave
        tags_list = []  # La lista vacía se usa para almacenar los tres valores después de dividir
        for i in tags_pairs:  # Imprimir etiqueta, grupo y peso TF-IDF
            tags_list.append((i[0], i[1]))  # Divide los tres valores de campo
        tags_pd = pd.DataFrame(tags_list, columns=['word', 'weight'])  # Crear marco de datos
        return tags_pd

    
    keywords = get_key_words(string_data)
    #print(keywords.loc[0].at['word'])
    print("#####################TF-IDF####################")
    #clave.set("Keywords:  "+str(keywords['word']))
    #mesajeTxt2.delete(1.0,"end")
    #mesajeTxt2.insert(1.0,"Keywords: "+str(keywords['word']))
    print(keywords)
    return(keywords)
###########################################################################################################
def verificacion(mensaje):
    tokenizer = RegexpTokenizer(r'\w+')
    text = tokenizer.tokenize(mensaje)
    text = ' '.join(word for word in text)
    tokenized_word=word_tokenize(text)
    tokenized_word = [word.lower() for word in tokenized_word]

    stop_words = set(stopwords.words('Spanish'))
    all_stopwords = stopwords.words('Spanish')
    all_stopwords.append('si')
    all_stopwords.append('min')
    all_stopwords.append('tan')
    all_stopwords.append('trabajo')
#print(stop_words)

#filtrado de palabras que estan en stopword

    filtered_word = []
    for word in tokenized_word:
        if word not in all_stopwords:
            filtered_word.append(word) 

    string_data =str(filtered_word)
    string_data = "".join(string_data)
    print(string_data)

###########################################################################################################

    def get_key_words(string_data, how=''):
    # topK: El número de palabras clave extraídas, si no se especifica, se extraerán todas;
    # withWeight: establezca True para especificar el peso IF-IDF correspondiente a la palabra de salida
        if how == 'textrank':
        # Use el algoritmo TextRank
            tags_pairs = jieba.analyse.textrank(string_data,  topK=10,  withWeight=True)  # Extraer etiquetas de palabras clave
        else:
        # Utilice el algoritmo TF-IDF
            tags_pairs = jieba.analyse.extract_tags(string_data,  topK=10,  withWeight=True)  # Extraer etiquetas de palabras clave
        tags_list = []  # La lista vacía se usa para almacenar los tres valores después de dividir
        for i in tags_pairs:  # Imprimir etiqueta, grupo y peso TF-IDF
            tags_list.append((i[0], i[1]))  # Divide los tres valores de campo
        tags_pd = pd.DataFrame(tags_list, columns=['word', 'weight'])  # Crear marco de datos
        return tags_pd

    
    keywords = get_key_words(string_data)
    #print(keywords.loc[0].at['word'])
    print("#####################TF-IDF####################")
    #clave.set("Keywords:  "+str(keywords['word']))
    mesajeTxt2.delete(1.0,"end")
    mesajeTxt2.insert(1.0,""+str(keywords['word']))
    banco_palabras=keywords
    print(keywords)
    return banco_palabras


###########################################################################################################


def comparacion(mensaje):
    vectorizer = CountVectorizer()
    data=['Como trabajo denominamos al conjunto de actividades que son realizadas con el objetivo de alcanzar una meta, solucionar un problema o producir bienes y servicios para atender las necesidades humanas.','es toda actividad humana libre, ya sea material o intelectual, permanente o transitoria, que una persona natural ejecuta conscientemente al servicio de otra, y cualquiera que sea su finalidad, siempre que se efectúe en ejecución de un contrato de trabajo.','El trabajo es el esfuerzo realizado por los seres humanos con la finalidad de producir riqueza. Desde el punto de vista teórico, este tópico ha sido abordado desde diferentes aristas, ya sean económicas, sociales o históricas, principalmente a causa de sus relevantes alcances en lo que hace el desarrollo de la humanidad.',''+str(mensaje)]
    #data=['toda actividad humana libre material  intelectual permanente  transitoria persona natural ejecuta conscientemente servicio otra cualquiera finalidad siempre efectúe ejecución contrato trabajo.trabajo economía horas dedican personas producción bienes servicios. trabajo factores producción capital, tierra tecnología. esfuerzo humano producción  venta  bienes  servicios.trabajo actividades realizadas objetivo alcanzar meta, solucionar problema producir bienes servicios  necesidades humanas.denomina trabajo actividad manual  intelectual cambio compensación económica labores concretadas.',str(mensaje)]
    x=vectorizer.fit_transform(data)
    #print (data[3:4])
    #print("get")
    #print (vectorizer.get_feature_names())

    #print("vocabulary")
    #print (vectorizer.vocabulary_) 

    
    tfidf = TfidfVectorizer().fit_transform(data)
    print(tfidf)
    notas=[cosine_similarity(tfidf[0:1],tfidf[3:4]),cosine_similarity(tfidf[1:2],tfidf[3:4]),cosine_similarity(tfidf[2:3],tfidf[3:4])]
    #notas=[cosine_similarity(tfidf[0:1],tfidf[3:4]).flatten(),cosine_similarity(tfidf[1:2],tfidf[3:4]).flatten(),cosine_similarity(tfidf[2:3],tfidf[3:4]).flatten()]
    print(notas)
    #sumaDeNotas=notas[0]+notas[1]+notas[2]
    if(float(notas[0]<0.4)) and (float(notas[1]<0.4)) and (float(notas[2]<0.4)):
        
        if(notas[0]>notas[1] and notas[0]>notas[2]):
            sumaDeNotas=(float(notas[0]*100))
            entrada.set("Su similaridad fue de: "+str(sumaDeNotas)+"%")
        if(notas[1]>notas[2] and notas[1]>notas[0]):
            sumaDeNotas=(float(notas[1]*100))
            entrada.set("Su similaridad fue de: "+str(sumaDeNotas)+"%")
        if(notas[2]>notas[0] and notas[2]>notas[1]):
            sumaDeNotas=(float(notas[2]*100))
            entrada.set("Su similaridad fue de: "+str(sumaDeNotas)+"%")
    else:
        similitud='su definicion es copiada'
        entrada.set("Su similaridad fue:  "+str(similitud))

    print(sumaDeNotas)
    
    """print(cosine_similarity(tfidf[0:1],tfidf[3:4]).flatten())
    print(cosine_similarity(tfidf[1:2],tfidf[3:4]).flatten())
    print(cosine_similarity(tfidf[2:3],tfidf[3:4]).flatten())"""



def guardardatos():
    global newmensaje
    mensaje=mesajeTxt.get(1.0, "end-1c")
    
    if botonguardar:
        comparacion(mensaje)
        palabras_contexto=verificacion(mensaje)
        banco_palabras=palabras_clave_contexto()
        #comparacion_palabras_clave(palabras_contexto)
        

        #print(veri)
        




ventana= Tk()
ventana.title("Definiciones")
ventana.geometry("400x500")
ventana.maxsize(400, 500)

miframe=Frame(ventana)
miframe.grid()

labelTitle = tk.Label(miframe, text="Realice una definicion de trabajo", font=('Microsoft Sans Serif',14, 'bold'))
labelTitle.grid(row=0, column=0,padx=20,pady=0)


#labelpregunta= tk.Label(miframe,text="Pregunta",font=("Poppins",12))
#labelpregunta.grid(row=1, column=0,padx=0,pady=5)

labelestado= tk.Label(miframe,text="",font=("Poppins",12),fg='red')
labelestado.grid(row=5, column=0,padx=5,pady=5)

labelrespuesta= tk.Label(miframe,text="Respuesta",font=("Poppins",12),fg='red')
labelrespuesta.grid(row=7, column=0,padx=5,pady=5)

labelrespuesta= tk.Label(miframe,text="Palabras clave",font=("Poppins",12),fg='red')
labelrespuesta.grid(row=9, column=0,padx=5,pady=5)

mesajeTxt= Text(miframe,width=45,height=7)
mesajeTxt.grid(row=3, column=0,padx=10,pady=1)

#labelrespuesta= Label(miframe,font=("Poppins",12),fg='red')
#labelrespuesta.grid(row=7, column=0,padx=0,pady=5)
entrada=StringVar()
clave=StringVar()

mesajeTxt2= Text(miframe,width=45,height=7)
mesajeTxt2.grid(row=11, column=0,padx=10,pady=1)

#campo_palabras_clave=Entry(miframe,textvariable=clave,width=50,fg='red')
#campo_palabras_clave.grid(row=10, column=0,padx=10,pady=1)

campo=Entry(miframe,textvariable=entrada,width=50,fg='red')
campo.grid(row=8, column=0,padx=10,pady=10)

mensajeNombre = StringVar()

etiquetacombo=Label(fg="red",font=("Popinns",12))
#etiquetacombo.grid(row=8, column=0,padx=20,pady=1)

botonguardar= Button(miframe,text="comparar",fg="black",font=("Poppins",12), command=guardardatos)
botonguardar.grid(row=4, column=0,padx=0,pady=5)

#botonEscuchar= Button(miframe,text="escuchar",fg="black",font=("Poppins",12), command=escuchardatos)
#botonEscuchar.grid(row=6, column=0,padx=0,pady=50)

ventana.mainloop()