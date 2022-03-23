# Hace una busqueda
# Trae URL de google
# Trae texto de pagina web
# Saca palabras clave de texto 
# Trae sinonimos de acuerdo a palabras clave
# Ingresa texto a evaluar
# Saca palabras clave del texto a evaluar
# Evalua que palabras se encuentran dentro del banco de palabras y dentro del banco de sinonimos 

import requests
import re
from re import I
from googlesearch import search
from bs4 import BeautifulSoup
from newspaper import Article
from nltk.tokenize import RegexpTokenizer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.tokenize import RegexpTokenizer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist
import spacy

 
vector=[]
lista_sinonimos=[]
palabras_repetidas=[]
textos=[]
valor = []

def cantBusquedas():
    numeroBusquedas= input("# de paginas a buscar (1-9) \n")
    if len(numeroBusquedas)>1:
        print("ingresar un numero entre 1 y 9")
        cantBusquedas()
    elif re.match("^[a-z]*$", numeroBusquedas):
        print ("Solo ingresar numeros")
        cantBusquedas()
    else:
        nuevoNumero=(int(numeroBusquedas))
        return (nuevoNumero)
    

def search_in_google(query,numerores):
	results = search(busqueda, num_results=numerores, lang="es")
	return results

def urls(numBusqueda):
    if (len(results))>int(numBusqueda):
        results.pop((len(results)-1))
        results.pop((len(results)-1))
    num=len(results)
    for s in range(num):
        #print(s)
        if (results[s].endswith('pdf')):
            valor.append(s)
            #print("true")
    print("Paginas donde busca: \n"+ str(results))
    #print(valor)
    num=len(valor)
    if (num==1):
        results.remove(results[valor[0]])
    elif (num==2):
        results.remove(results[valor[0]])	
        results.remove(results[(valor[1]-1)])
    elif (num==3):
        results.remove(results[valor[0]])	
        results.remove(results[(valor[1]-1)])
        results.remove(results[(valor[2]-2)])
    else:
        pass

    #print(results)

    return results

def palabras_clave(texto,numpalabras):
    tokenizer = RegexpTokenizer(r'\w+')
    text = tokenizer.tokenize(texto)
    text = ' '.join(word for word in text)
    tokenized_word=word_tokenize(text)
    tokenized_word = [word.lower() for word in tokenized_word]

    stop_words = set(stopwords.words('Spanish'))
    all_stopwords = stopwords.words('Spanish')
    all_stopwords.append('si')
    all_stopwords.append('min')
    all_stopwords.append('tan')
    #print(stop_words)

    #filtrado de palabras que estan en stopword

    filtered_word = []
    for word in tokenized_word:
        if word not in all_stopwords:
            filtered_word.append(word)

    ####Frecuencia de palabras dentro de las palabras claves####
    fdist = FreqDist(filtered_word)
    most_common = fdist.most_common(numpalabras)
    data=(fdist.most_common(numpalabras))
    return data

def traer_texto(urls):
    for url in urls:
        toi_article = Article(url, language="es") 
        toi_article.download()
        toi_article.parse()
        texto=toi_article.text
        key=palabras_clave(texto,20)
        for key in key:
            if key not in vector:
                vector.append((key))
    return vector
    #palabras(vector)
     
def palabras(vector):
    numero=len(vector)
    for i in range(numero):
        vector[i]=str(vector[i][0])
    print("Palabras clave: \n" + str(vector)) 
    return vector
    #sinonimos(vector)


def sinonimos(vector):
    numero=len(vector)
    for i in range(numero):
        sinonimo=str(vector[i])
        #print(sinonimo)
        url="https://www.wordreference.com/sinonimos/"
        buscar= url+sinonimo
        resp=requests.get(buscar)
        soup=BeautifulSoup(resp.text)
        lista=soup.find(class_='trans clickable')
        if lista==None:
            pass
        else:
            sino=lista.find('li')
            lista_sinonimos.append(sino.next_element)

        tokenizer = RegexpTokenizer(r'\w+')
        text = tokenizer.tokenize(str(lista_sinonimos))
        text = ' '.join(word for word in text)
        tokenized_word=word_tokenize(text)
        tokenized_word = [word.lower() for word in tokenized_word]

        stop_words = set(stopwords.words('Spanish'))
        all_stopwords = stopwords.words('Spanish')
        all_stopwords.append('si')
        all_stopwords.append('min')
        all_stopwords.append('tan') 

        filtered_word = []
        for word in tokenized_word:
            if word not in all_stopwords:
                filtered_word.append(word)

        #print(str(filtered_word[1])) 
        #lista_sinonimos=str(filtered_word)
    return filtered_word
    
def entrada_texto(entrada):
    datos=palabras_clave(entrada,15)
    keywords=palabras_texto(datos)
    #print(keywords)
    return keywords

def palabras_texto(vector):
    numero=len(vector)
    for i in range(numero):
        vector[i]=str(vector[i][0])
    print("Palabras encontradas \n" + str(vector)) 
    return vector

def buscar_palabras_vector(palabrasinput,palabrasclave,sinonimos):
    numero=len(palabrasinput)
    for s in range(numero):
        if palabrasinput[s] in (palabrasclave):
            palabras_repetidas.append(palabrasinput[s])
    #print("lista de sinonimos \n"+str(sinonimos))
    for s in range(numero):
        if palabrasinput[s] in sinonimos:
            palabras_repetidas.append(palabrasinput[s]) 

    print("Palabras encontradas dentro de sinonimos y palabras clave: \n" + str(palabras_repetidas))
    return palabras_repetidas

def texto_comparacion(paginas):
    results=paginas
    for s in range(len(results)):
        toi_article = Article(results[s], language="es") 
        #print(url)
        toi_article.download()
        toi_article.parse()
        texto=toi_article.text
        #print(texto)
        textos.insert(s,texto)   
    #print(len(textos))

    return textos

def comparacion(mensaje,entrada):
    vectorizer = CountVectorizer()
    nuevoVector=[]
    nuevoVector=entrada
    #entrada=input("Inserte su texto\n")
    mensaje.append(nuevoVector)
    tfidf = TfidfVectorizer().fit_transform(mensaje)
    #print(len(mensaje))
    if len(mensaje)==10:
        notas=[cosine_similarity(tfidf[0:1],tfidf[9:10]),cosine_similarity(tfidf[1:2],tfidf[9:10]),cosine_similarity(tfidf[2:3],tfidf[9:10]),cosine_similarity(tfidf[3:4],tfidf[9:10]),cosine_similarity(tfidf[4:5],tfidf[9:10]),cosine_similarity(tfidf[5:6],tfidf[9:10]),cosine_similarity(tfidf[6:7],tfidf[9:10]),cosine_similarity(tfidf[7:8],tfidf[9:10]),cosine_similarity(tfidf[8:9],tfidf[9:10])]
        print(notas)
    if len(mensaje)==9:
        notas=[cosine_similarity(tfidf[0:1],tfidf[8:9]),cosine_similarity(tfidf[1:2],tfidf[8:9]),cosine_similarity(tfidf[2:3],tfidf[8:9]),cosine_similarity(tfidf[3:4],tfidf[8:9]),cosine_similarity(tfidf[4:5],tfidf[8:9]),cosine_similarity(tfidf[5:6],tfidf[8:9]),cosine_similarity(tfidf[6:7],tfidf[8:9]),cosine_similarity(tfidf[7:8],tfidf[8:9])]
        print(notas)
    if len(mensaje)==8:
        notas=[cosine_similarity(tfidf[0:1],tfidf[7:8]),cosine_similarity(tfidf[1:2],tfidf[7:8]),cosine_similarity(tfidf[2:3],tfidf[7:8]),cosine_similarity(tfidf[3:4],tfidf[7:8]),cosine_similarity(tfidf[4:5],tfidf[7:8]),cosine_similarity(tfidf[5:6],tfidf[7:8]),cosine_similarity(tfidf[6:7],tfidf[7:8])]
        print(notas)
    if len(mensaje)==7:
        notas=[cosine_similarity(tfidf[0:1],tfidf[6:7]),cosine_similarity(tfidf[1:2],tfidf[6:7]),cosine_similarity(tfidf[2:3],tfidf[6:7]),cosine_similarity(tfidf[3:4],tfidf[6:7]),cosine_similarity(tfidf[4:5],tfidf[6:7]),cosine_similarity(tfidf[5:6],tfidf[6:7])]
        print(notas)
    if len(mensaje)==6:
        notas=[cosine_similarity(tfidf[0:1],tfidf[5:6]),cosine_similarity(tfidf[1:2],tfidf[5:6]),cosine_similarity(tfidf[2:3],tfidf[5:6]),cosine_similarity(tfidf[3:4],tfidf[5:6]),cosine_similarity(tfidf[4:5],tfidf[5:6])]
        print(notas)
    if len(mensaje)==5:
        notas=[cosine_similarity(tfidf[0:1],tfidf[4:5]),cosine_similarity(tfidf[1:2],tfidf[4:5]),cosine_similarity(tfidf[2:3],tfidf[4:5]),cosine_similarity(tfidf[3:4],tfidf[4:5])]
        print(notas)
    if len(mensaje)==4:
        notas=[cosine_similarity(tfidf[0:1],tfidf[3:4]),cosine_similarity(tfidf[1:2],tfidf[3:4]),cosine_similarity(tfidf[2:3],tfidf[3:4])]
        print(notas)
    if len(mensaje)==3:
        notas=[cosine_similarity(tfidf[0:1],tfidf[2:3]),cosine_similarity(tfidf[1:2],tfidf[2:3])]
        print(notas)
    if len(mensaje)==2:
        notas=[cosine_similarity(tfidf[0:1],tfidf[1:2])]
        print(notas)
    return nuevoVector

def analisistexto(texto):
    nlp = spacy.load("es_core_news_sm")
    doc = nlp(texto)
    for token in doc:
        pass
        #print(token.text, token.pos_, token.dep_) 


####base##################################
busqueda = input("Inserte su busqueda\n")
numeroBusquedas=cantBusquedas()
print(numeroBusquedas)
results = search_in_google(busqueda,int(numeroBusquedas))
for result in results:
    pass
paginas=[]
paginas=urls(int(numeroBusquedas))
#######Tratamiento de palabras########
palabrastexto=traer_texto(paginas)
palabrassolas=palabras(palabrastexto)
sinoni=sinonimos(palabrassolas)
######################################

#########Ingresar texto nuevo#########
entrada=input("Inserte su texto\n")
palabrasinput=entrada_texto(entrada)
buscar_palabras_vector(palabrasinput,palabrassolas,sinoni) 
######################################

########Comparacion###############
compa=texto_comparacion(paginas)
textos=comparacion(compa,entrada)
analisistexto(entrada)


##########################################


