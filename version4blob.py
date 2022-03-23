
####Comparacion, PalabrasClave, Estructuracion
#### Se quiere tambien mas adelante obtener ortografia


import json
from numpy import insert
import spacy
import re
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from textblob.classifiers import NaiveBayesClassifier

stopwordsplus=['a','actualmente','adelante','además','afirmó','agregó','ahora','ahí','al','algo','alguna','algunas','alguno','algunos','algún','alrededor','ambos','ampleamos','ante','anterior','antes','apenas','aproximadamente','aquel','aquellas','aquellos','aqui','aquí','arriba','aseguró','así','atras','aunque','ayer','añadió','aún','bajo','bastante','bien','buen','buena','buenas','bueno','buenos','cada','casi','cerca','cierta','ciertas','cierto','ciertos','cinco','comentó','como','con','conocer','conseguimos','conseguir','considera','consideró','consigo','consigue','consiguen','consigues','contra','cosas','creo','cual','cuales','cualquier','cuando','cuanto','cuatro','cuenta','cómo','da','dado','dan','dar','de','debe','deben','debido','decir','dejó','del','demás','dentro','desde','después','dice','dicen','dicho','dieron','diferente','diferentes','dijeron','dijo','dio','donde','dos','durante','e','ejemplo','el','ella','ellas','ello','ellos','embargo','empleais','emplean','emplear','empleas','empleo','en','encima','encuentra','entonces','entre','era','erais','eramos','eran','eras','eres','es','esa','esas','ese','eso','esos','esta','estaba','estabais','estaban','estabas','estad','estada','estadas','estado','estados','estais','estamos','estan','estando','estar','estaremos','estará','estarán','estarás','estaré','estaréis','estaría','estaríais','estaríamos','estarían','estarías','estas','este','estemos','esto','estos','estoy','estuve','estuviera','estuvierais','estuvieran','estuvieras','estuvieron','estuviese','estuvieseis','estuviesen','estuvieses','estuvimos','estuviste','estuvisteis','estuviéramos','estuviésemos','estuvo','está','estábamos','estáis','están','estás','esté','estéis','estén','estés','ex','existe','existen','explicó','expresó','fin','fue','fuera','fuerais','fueran','fueras','fueron','fuese','fueseis','fuesen','fueses','fui','fuimos','fuiste','fuisteis','fuéramos','fuésemos','gran','grandes','gueno','ha','haber','habida','habidas','habido','habidos','habiendo','habremos','habrá','habrán','habrás','habré','habréis','h','habríais','habríamos','habrían','habrías','habéis','había','habíais','habíamos','habían','habías','hace','haceis','hacemos','hacen','hacer','hacerlo','haces','hacia','haciendo','hago','han','has','hasta','hay','haya','hayamos','hayan','hayas','hayáis','he','hecho','hemos','hicieron','hizo','hoy','hube','hubiera','hubierais','hubieran','hubieras','hubieron','hubiese','hubieseis','hubiesen','hubieses','hubimos','hubiste','hubisteis','hubiéramos','hubiésemos','hubo','igual','incluso','indicó','informó','intenta','intentais','intentamos','intentan','intentar','intentas','intento','ir','junto','la','lado','largo','las','le','les','llegó','lleva','llevar','lo','los','luego','lugar','manera','manifestó','mayor','me','mediante','mejor','mencionó','menos','mi','mientras','mio','mis','misma',
'mismas','mismo','mismos','modo','momento','mucha','muchas','mucho','muchos','muy','más','mí','mía','mías','mío','míos','nada','nadie','ni','ninguna','ningunas','ninguno','ningunos','ningún','no','nos','nosotras','nosotros','nue','nuestras','nuestro','nuestros','nueva','nuevas','nuevo','nuevos','nunca','o','ocho','os','otra','otras','otro','otros','para','parece','parte','partir','pasada','pasado','pero','pesar','poca','pocas','poco','pocos','podeis','podemos','poder','podria','podriais','podriamos','podrian','podrias','podrá','podrán','podría','podrían','poner','por','por qué','porque','posible','primer','primera','primero','primeros','principalmente','propia','propias','propio','propios','próximo','próximos','pudo','pueda','puede','pueden','puedo','pues','que','quedó','queremos','quien','quienes','quiere','quién','qué','realizado','realizar','realizó','respecto','sabe','sabeis','sabemos','saben','saber','sabes','se','sea','seamos','sean','seas','segunda','segundo','según','seis','ser','seremos','será','serán','serás','seré','seréis','sería','seríais','seríamos','serían','serías','seáis','señaló','si','sido','siempre','siendo','siete','sigue','siguiente','sin','sino','sobre','sois','sola','solamente','solas','solo','solos','somos','n','soy','su','sus','suya','suyas','suyo','suyos','sí','sólo','tal','también','tampoco','tan','tanto','te','tendremos','tendrá','tendrán','tendrás','tendré','tendréis','tendría','tendríais','tendríamos','tendrían','tendrías','tened','teneis','tenemos','tener','tenga','tengamos','tengan','tengas','tengo','tengáis','tenida','tenidas','tenido','tenidos','teniendo','tenéis','tenía','teníais','teníamos','tenían','tenías','tercera','ti','tiempo','tiene','tienen','tienes','toda','todas','todavía','todo','todos','total','trabaja','trabajais','trabajamos','trabajan','trabajar','trabajas','trabajo','tras','trata','través','tres','tu','tus','tuve','tuviera','tuvierais','tuvieran','tuvieras','tuvieron','tuviese','tuvieseis','tuviesen','tuvieses','tuvimos','tuviste','tuvisteis','tuviéramos','tuviésemos','tuvo','tuya','tuyas','tuyo','tuyos','tú','ultimo','un','una','unas','uno','unos','usa','usais','usamos','usan','usar','usas','uso','usted','va','vais','valor','vamos','van','varias','varios','vaya','veces','ver','verdad','ra','verdadero','vez','vosotras','vosotros','voy','vuestra','vuestras','vuestro','vuestros','y','ya','yo','él','éramos','ésta','éstas','éste','éstos','última','últimas','último','últimos','0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','w','u','x','y','z','enero','febrero','marzo','abril','mayo','junio','julio','agosto','septiembre','noviembre','diciembre','in','the','of','et','and','re','áreas']

nlp = spacy.load("es_core_news_lg")



""" def data(lista):
    datos
    datos=[
        (lista[0],'5.0'),
        (lista[1],'5.0'),
        (lista[2],'3.0'),
        (lista[3],'3.0'),
        (lista[4],'1.0'),
        (lista[5],'1.0'),
    ]
    print(datos)
    return datos """



def tokenizacion_resp(textos):
    vector1= []
    eliminarpunt = re.sub(r'[^\w\s]','',str(textos))
    minusculas=eliminarpunt.lower()
    docnlp=nlp(minusculas)
    for token in docnlp:
        vector1.append(token.lemma_)
    #print(vector1)


    return vector1 

def palabras_clave(palabras):
    palabrasclave = []
    palabrasfind=[]
    palabrasfind=palabras
    #print("palabrase"+str(palabrasfind))
    stop_words = set(stopwords.words('Spanish'))
    all_stopwords = stopwords.words('Spanish')
    all_stopwords.append('si')
    all_stopwords.append('min')
    all_stopwords.append('tan')
    all_stopwords.append('trabajo') 
    all_stopwords.append('\n') 
    all_stopwords.append('\n ')
    all_stopwords.append('\n  ')
    all_stopwords.append('\n   ')   
    all_stopwords.append('\n\n')  
    all_stopwords.append('\n               ')  
    all_stopwords.append('')
    all_stopwords.append(' ')
    all_stopwords.append('  ')  
    all_stopwords.append('etc')  
    for i in stopwordsplus:
        all_stopwords.append(i)
    #print(all_stopwords)

    #filtrado de palabras que estan en stopword

    filtered_word = []
    for word in palabrasfind:
        if word not in all_stopwords:
            filtered_word.append(word)

    string_data =str(filtered_word)
    string_data = "".join(string_data)
    #print(string_data)

    fdist = FreqDist(filtered_word)
    most_common = fdist.most_common(40)
    data=(fdist.most_common(40))
    #print(data)
    for s in range(len(data)):
        palabrasclave.append(data[s][0])
    #print(palabrasclave)  
    return palabrasclave

def comparacion(claves,clavestext):
    compara=[]
    #print(claves)
    for clave in claves:
        if clave in clavestext:
            compara.append(clave)
    num=len(compara)
    if num == 5:
        valor= 1
    elif num == 4:
        valor= 0.8
    elif num == 3:
        valor= 0.6
    elif num == 2:
        valor= 0.4
    elif num == 1:
        valor= 0.2
    else:
        valor=0

    return valor

def libreria_spacy(contextos,respuesta):
    contextos1=[]
    vector=[]
    for n in range(len(contextos)):
        contextos1.append(contextos[n][0])
    
    for definicion in contextos1: 
        doc2 = (str(definicion))
        doc3=nlp(doc2)
        doc = nlp(str(respuesta))
        var= doc.similarity(doc3)
        vector.append(var)
    print(vector)  
    for valor in vector:
        if valor>=0.975:
            copia = True
            break
        else:
            copia = False
    #print(copia)
    return copia

def califi(datos,respuesta):
   cl=NaiveBayesClassifier(datos)
   print(cl.classify(respuesta))
   nota = int(cl.classify(respuesta))
   return nota

def lema(complete):
    for s in range(len(complete)):
        vector1 = []
        textos=complete[s][0]
        eliminarpunt = re.sub(r'[^\w\s]','',str(textos))
        minusculas=eliminarpunt.lower()
        docnlp=nlp(minusculas)
        for token in docnlp:
            vector1.append(token.lemma_)
        definicion = str(" ".join(vector1))
        (complete[s][0])=str(definicion)
    print(complete)
    
    return complete

def lemaresp(respuesta):
    vector1 = []
    if type(respuesta)==str:
        eliminarpunt = re.sub(r'[^\w\s]','',str(respuesta))
        minusculas=eliminarpunt.lower()
        docnlp=nlp(minusculas)
        for token in docnlp:
            vector1.append(token.lemma_)
        definicion = str(" ".join(vector1))
        respuesta=str(definicion)
        print(respuesta)
        print(type(respuesta))
    elif type(respuesta)==list:
        for resp in respuesta:
            eliminarpunt = re.sub(r'[^\w\s]','',str(resp))
            minusculas=eliminarpunt.lower()
            docnlp=nlp(minusculas)
            for token in docnlp:
                vector1.append(token.lemma_)
            respuesta=vector1
        print(type(respuesta))
        print(respuesta)
    return respuesta

#complete= lista de tuplas que contiene las definiciones y las notas establecidas


def calificacion(complete,clavestext,respuesta):
    #print(complete[1][0])
    
    complete1=lema(complete)                                    #lematizacion de tuplas
    lista=tuple(complete1)                                      #transformacion a tupla
    respuesta=lemaresp(respuesta)                               #lematizacion respuesta
    palabras = tokenizacion_resp(respuesta)                     #Tokenikacion de respuestas
    toltalwords = palabras_clave(palabras)                      #lista de palabras clave
    wordslema=lemaresp(toltalwords)
    extras = comparacion(wordslema,clavestext)                  #Comparacion entre palabras clave de textos y definidas
    nota_de_calificacion=califi(lista,respuesta)                #Calificacion
    copia=libreria_spacy(lista,respuesta)                       #verificacion de copia (si la nota es 0 es porque es copia)
    suma_notas = float(nota_de_calificacion) + float(extras)    #suma de notas
    if suma_notas>=5.0:
        suma_notas=5.0
    if copia :
        suma_notas=0
    print(suma_notas)
    return suma_notas

#respuesta()