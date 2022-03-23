from csv import reader
import re
from PyPDF2 import PdfFileReader
import PyPDF2
from numpy import append, extract
import spacy
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist
import string
from nltk.tokenize import RegexpTokenizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

stopwordsplus=['a','actualmente','adelante','además','afirmó','agregó','ahora','ahí','al','algo','alguna','algunas','alguno','algunos','algún','alrededor','ambos','ampleamos','ante','anterior','antes','apenas','aproximadamente','aquel','aquellas','aquellos','aqui','aquí','arriba','aseguró','así','atras','aunque','ayer','añadió','aún','bajo','bastante','bien','buen','buena','buenas','bueno','buenos','cada','casi','cerca','cierta','ciertas','cierto','ciertos','cinco','comentó','como','con','conocer','conseguimos','conseguir','considera','consideró','consigo','consigue','consiguen','consigues','contra','cosas','creo','cual','cuales','cualquier','cuando','cuanto','cuatro','cuenta','cómo','da','dado','dan','dar','de','debe','deben','debido','decir','dejó','del','demás','dentro','desde','después','dice','dicen','dicho','dieron','diferente','diferentes','dijeron','dijo','dio','donde','dos','durante','e','ejemplo','el','ella','ellas','ello','ellos','embargo','empleais','emplean','emplear','empleas','empleo','en','encima','encuentra','entonces','entre','era','erais','eramos','eran','eras','eres','es','esa','esas','ese','eso','esos','esta','estaba','estabais','estaban','estabas','estad','estada','estadas','estado','estados','estais','estamos','estan','estando','estar','estaremos','estará','estarán','estarás','estaré','estaréis','estaría','estaríais','estaríamos','estarían','estarías','estas','este','estemos','esto','estos','estoy','estuve','estuviera','estuvierais','estuvieran','estuvieras','estuvieron','estuviese','estuvieseis','estuviesen','estuvieses','estuvimos','estuviste','estuvisteis','estuviéramos','estuviésemos','estuvo','está','estábamos','estáis','están','estás','esté','estéis','estén','estés','ex','existe','existen','explicó','expresó','fin','fue','fuera','fuerais','fueran','fueras','fueron','fuese','fueseis','fuesen','fueses','fui','fuimos','fuiste','fuisteis','fuéramos','fuésemos','gran','grandes','gueno','ha','haber','habida','habidas','habido','habidos','habiendo','habremos','habrá','habrán','habrás','habré','habréis','h','habríais','habríamos','habrían','habrías','habéis','había','habíais','habíamos','habían','habías','hace','haceis','hacemos','hacen','hacer','hacerlo','haces','hacia','haciendo','hago','han','has','hasta','hay','haya','hayamos','hayan','hayas','hayáis','he','hecho','hemos','hicieron','hizo','hoy','hube','hubiera','hubierais','hubieran','hubieras','hubieron','hubiese','hubieseis','hubiesen','hubieses','hubimos','hubiste','hubisteis','hubiéramos','hubiésemos','hubo','igual','incluso','indicó','informó','intenta','intentais','intentamos','intentan','intentar','intentas','intento','ir','junto','la','lado','largo','las','le','les','llegó','lleva','llevar','lo','los','luego','lugar','manera','manifestó','mayor','me','mediante','mejor','mencionó','menos','mi','mientras','mio','mis','misma','mismas','mismo','mismos','modo','momento','mucha','muchas','mucho','muchos','muy','más','mí','mía','mías','mío','míos','nada','nadie','ni','ninguna','ningunas','ninguno','ningunos','ningún','no','nos','nosotras','nosotros','nue','nuestras','nuestro','nuestros','nueva','nuevas','nuevo','nuevos','nunca','o','ocho','os','otra','otras','otro','otros','para','parece','parte','partir','pasada','pasado','pero','pesar','poca','pocas','poco','pocos','podeis','podemos','poder','podria','podriais','podriamos','podrian','podrias','podrá','podrán','podría','podrían','poner','por','por qué','porque','posible','primer','primera','primero','primeros','principalmente','propia','propias','propio','propios','próximo','próximos','pudo','pueda','puede','pueden','puedo','pues','que','quedó','queremos','quien','quienes','quiere','quién','qué','realizado','realizar','realizó','respecto','sabe','sabeis','sabemos','saben','saber','sabes','se','sea','seamos','sean','seas','segunda','segundo','según','seis','ser','seremos','será','serán','serás','seré','seréis','sería','seríais','seríamos','serían','serías','seáis','señaló','si','sido','siempre','siendo','siete','sigue','siguiente','sin','sino','sobre','sois','sola','solamente','solas','solo','solos','somos','n','soy','su','sus','suya','suyas','suyo','suyos','sí','sólo','tal','también','tampoco','tan','tanto','te','tendremos','tendrá','tendrán','tendrás','tendré','tendréis','tendría','tendríais','tendríamos','tendrían','tendrías','tened','teneis','tenemos','tener','tenga','tengamos','tengan','tengas','tengo','tengáis','tenida','tenidas','tenido','tenidos','teniendo','tenéis','tenía','teníais','teníamos','tenían','tenías','tercera','ti','tiempo','tiene','tienen','tienes','toda','todas','todavía','todo','todos','total','trabaja','trabajais','trabajamos','trabajan','trabajar','trabajas','trabajo','tras','trata','través','tres','tu','tus','tuve','tuviera','tuvierais','tuvieran','tuvieras','tuvieron','tuviese','tuvieseis','tuviesen','tuvieses','tuvimos','tuviste','tuvisteis','tuviéramos','tuviésemos','tuvo','tuya','tuyas','tuyo','tuyos','tú','ultimo','un','una','unas','uno','unos','usa','usais','usamos','usan','usar','usas','uso','usted','va','vais','valor','vamos','van','varias','varios','vaya','veces','ver','verdad','ra','verdadero','vez','vosotras','vosotros','voy','vuestra','vuestras','vuestro','vuestros','y','ya','yo','él','éramos','ésta','éstas','éste','éstos','última','últimas','último','últimos','0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','w','u','x','y','z','enero','febrero','marzo','abril','mayo','junio','julio','agosto','septiembre','noviembre','diciembre','in','the','of','et','and','re','áreas']

nlp = spacy.load("es_core_news_lg")


def traer_texto_pdf():
    vector=[]
    pdf=open(r'C:\Users\Felipe\OneDrive\Escritorio\Doc la gran colombia\Programas python\Palabras clave\inteligencia.pdf','rb')
    reader = PyPDF2.PdfFileReader(pdf)
    for pag in range(reader.numPages):
        page1=reader.getPage(pag)
        #print(reader.numPages)
        data=page1.extractText()
        eliminarpunt = re.sub(r'[^\w\s]','',data)
        minusculas=eliminarpunt.lower()
        docnlp=nlp(minusculas)
    for token in docnlp:
        vector.append(token.text)
    #print(vector)
    return vector

def extraccionpalabras(textoentrada):
    vector=[]
    eliminarpunt = re.sub(r'[^\w\s]','',textoentrada)
    minusculas=eliminarpunt.lower()
    docnlp=nlp(minusculas)
    for token in docnlp:
        vector.append(token.text)
    print(vector)
    
    return vector

def palabras_clave(palabras):
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
    print(string_data)

    fdist = FreqDist(filtered_word)
    most_common = fdist.most_common(40)
    data=(fdist.most_common(40))
    print(data)
    return data

def entrada_texto(entrada):
    palabrasencontradas=extraccionpalabras(entrada)
    print("si entra a esta parte")
    keywords=palabras_clave(palabrasencontradas)
    #print(keywords)
    return keywords

def comparacion(palabrasClave,clavespdf):
    totalpalabras=[]
    numero=len(palabrasClave)
    for s in range(numero):
        totalpalabras.append(palabrasClave[s][0])
    print(totalpalabras)

    tfidf = TfidfVectorizer().fit_transform(totalpalabras)
    print((tfidf))
    print(cosine_similarity(tfidf[0:1],tfidf[2:3]))
    
    #print(len(palabrasClave[0]))
    #print(len(clavespdf))


pdf=traer_texto_pdf()
clavespdf=palabras_clave(pdf)
entrada=input("Inserte su texto\n")
palabrasClave=entrada_texto(entrada)
comparacion(palabrasClave,clavespdf)

