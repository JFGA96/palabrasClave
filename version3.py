
import spacy
import re
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist
############################################################################
#contexto1="La sentencia condicional if se usa para tomar decisiones, este evaluá básicamente una operación lógica, es decir una expresión que de como resultado True o False, y ejecuta la pieza de código siguiente siempre y cuando el resultado sea verdadero."

#deficnicion ="La sentencia if es un condicional que decide si toma un camino u otro"#muy buena
#contexto1="Es una sentencia por la cual se puede comparar una variable y establecer que desicion tomar de acuerdo a la variable"#buena
#contexto1="es una sentencia para definir un ciclo y cuantas iteraciones haya dentro del ciclo"#regular
#contexto1="es una sentencia para imprimir el valor en especial los caracteres"#fuera de base
############################################################################

stopwordsplus=['a','actualmente','adelante','además','afirmó','agregó','ahora','ahí','al','algo','alguna','algunas','alguno','algunos','algún','alrededor','ambos','ampleamos','ante','anterior','antes','apenas','aproximadamente','aquel','aquellas','aquellos','aqui','aquí','arriba','aseguró','así','atras','aunque','ayer','añadió','aún','bajo','bastante','bien','buen','buena','buenas','bueno','buenos','cada','casi','cerca','cierta','ciertas','cierto','ciertos','cinco','comentó','como','con','conocer','conseguimos','conseguir','considera','consideró','consigo','consigue','consiguen','consigues','contra','cosas','creo','cual','cuales','cualquier','cuando','cuanto','cuatro','cuenta','cómo','da','dado','dan','dar','de','debe','deben','debido','decir','dejó','del','demás','dentro','desde','después','dice','dicen','dicho','dieron','diferente','diferentes','dijeron','dijo','dio','donde','dos','durante','e','ejemplo','el','ella','ellas','ello','ellos','embargo','empleais','emplean','emplear','empleas','empleo','en','encima','encuentra','entonces','entre','era','erais','eramos','eran','eras','eres','es','esa','esas','ese','eso','esos','esta','estaba','estabais','estaban','estabas','estad','estada','estadas','estado','estados','estais','estamos','estan','estando','estar','estaremos','estará','estarán','estarás','estaré','estaréis','estaría','estaríais','estaríamos','estarían','estarías','estas','este','estemos','esto','estos','estoy','estuve','estuviera','estuvierais','estuvieran','estuvieras','estuvieron','estuviese','estuvieseis','estuviesen','estuvieses','estuvimos','estuviste','estuvisteis','estuviéramos','estuviésemos','estuvo','está','estábamos','estáis','están','estás','esté','estéis','estén','estés','ex','existe','existen','explicó','expresó','fin','fue','fuera','fuerais','fueran','fueras','fueron','fuese','fueseis','fuesen','fueses','fui','fuimos','fuiste','fuisteis','fuéramos','fuésemos','gran','grandes','gueno','ha','haber','habida','habidas','habido','habidos','habiendo','habremos','habrá','habrán','habrás','habré','habréis','h','habríais','habríamos','habrían','habrías','habéis','había','habíais','habíamos','habían','habías','hace','haceis','hacemos','hacen','hacer','hacerlo','haces','hacia','haciendo','hago','han','has','hasta','hay','haya','hayamos','hayan','hayas','hayáis','he','hecho','hemos','hicieron','hizo','hoy','hube','hubiera','hubierais','hubieran','hubieras','hubieron','hubiese','hubieseis','hubiesen','hubieses','hubimos','hubiste','hubisteis','hubiéramos','hubiésemos','hubo','igual','incluso','indicó','informó','intenta','intentais','intentamos','intentan','intentar','intentas','intento','ir','junto','la','lado','largo','las','le','les','llegó','lleva','llevar','lo','los','luego','lugar','manera','manifestó','mayor','me','mediante','mejor','mencionó','menos','mi','mientras','mio','mis','misma','mismas','mismo','mismos','modo','momento','mucha','muchas','mucho','muchos','muy','más','mí','mía','mías','mío','míos','nada','nadie','ni','ninguna','ningunas','ninguno','ningunos','ningún','no','nos','nosotras','nosotros','nue','nuestras','nuestro','nuestros','nueva','nuevas','nuevo','nuevos','nunca','o','ocho','os','otra','otras','otro','otros','para','parece','parte','partir','pasada','pasado','pero','pesar','poca','pocas','poco','pocos','podeis','podemos','poder','podria','podriais','podriamos','podrian','podrias','podrá','podrán','podría','podrían','poner','por','por qué','porque','posible','primer','primera','primero','primeros','principalmente','propia','propias','propio','propios','próximo','próximos','pudo','pueda','puede','pueden','puedo','pues','que','quedó','queremos','quien','quienes','quiere','quién','qué','realizado','realizar','realizó','respecto','sabe','sabeis','sabemos','saben','saber','sabes','se','sea','seamos','sean','seas','segunda','segundo','según','seis','ser','seremos','será','serán','serás','seré','seréis','sería','seríais','seríamos','serían','serías','seáis','señaló','si','sido','siempre','siendo','siete','sigue','siguiente','sin','sino','sobre','sois','sola','solamente','solas','solo','solos','somos','n','soy','su','sus','suya','suyas','suyo','suyos','sí','sólo','tal','también','tampoco','tan','tanto','te','tendremos','tendrá','tendrán','tendrás','tendré','tendréis','tendría','tendríais','tendríamos','tendrían','tendrías','tened','teneis','tenemos','tener','tenga','tengamos','tengan','tengas','tengo','tengáis','tenida','tenidas','tenido','tenidos','teniendo','tenéis','tenía','teníais','teníamos','tenían','tenías','tercera','ti','tiempo','tiene','tienen','tienes','toda','todas','todavía','todo','todos','total','trabaja','trabajais','trabajamos','trabajan','trabajar','trabajas','trabajo','tras','trata','través','tres','tu','tus','tuve','tuviera','tuvierais','tuvieran','tuvieras','tuvieron','tuviese','tuvieseis','tuviesen','tuvieses','tuvimos','tuviste','tuvisteis','tuviéramos','tuviésemos','tuvo','tuya','tuyas','tuyo','tuyos','tú','ultimo','un','una','unas','uno','unos','usa','usais','usamos','usan','usar','usas','uso','usted','va','vais','valor','vamos','van','varias','varios','vaya','veces','ver','verdad','ra','verdadero','vez','vosotras','vosotros','voy','vuestra','vuestras','vuestro','vuestros','y','ya','yo','él','éramos','ésta','éstas','éste','éstos','última','últimas','último','últimos','0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','w','u','x','y','z','enero','febrero','marzo','abril','mayo','junio','julio','agosto','septiembre','noviembre','diciembre','in','the','of','et','and','re','áreas']


nlp = spacy.load("es_core_news_lg")


definiciones=["Mamífero carnívoro doméstico de la familia de los cánidos que se caracteriza por tener los sentidos del olfato y el oído muy finos, por su inteligencia y por su fidelidad al ser humano, que lo ha domesticado desde tiempos prehistóricos; hay muchísimas razas, de características muy diversas.",
"Un perro es un animal domestico que tiene bastante pelo y 4 patas.Son muy fieles y tienen sentidos muy agudos",
"Un perro es una mascota que juega mucho y que le gusta ir al parque"]
#"Un perro es un animal grandisimo que no les gustan los humanos y no es muy amigable",
#"Es un animal peludo que ademas es domestico y le gusta el pescado y tiene garras muy largas por lo general no le gusta salir a las calles"] 

#definiciones=["Un for en programación se usa cuando queremos repetir un conjunto de instrucciones un número finito de veces. ... En programación existen los bucles, como puede ser escribir con while o for.",
#"El bucle for es una estructura de control en programación en la que se puede indicar de antemano el número máximo de iteraciones",
#"El ciclo for es uno de los más utilizados en programación debido a que permite repetir varias instrucciones (pasos) un cierto número de ocasiones (por ejemplo, 10 veces). Se emplea en el recorrido de vectores, matrices y estructuras, entre otros."]
#"A menudo queremos ser capaces de hacer cosas ""condicionalmente"" en nuestros programas: queremos ser capaces de decir ""si esta cosa es verdad, entonces haz X, pero si esta otra cosa es verdad, entonces haz Y"". Es como cuando despertamos por la mañana: ""si afuera está lloviendo, entonces llevo un paraguas, pero si está soleado, me pongo lentes de sol"". Podemos hacer cosas condicionalmente en nuestros programas al usar declaraciones if y declaraciones if/else combinadas con expresiones condicionales.",
#"Un perro es un animal grandisimo que no les gustan los humanos y no es muy amigable"] 
#respuesta="Una sentencia if es utilizada en programacion para repetir o hacer bucles infinitos sobre el espacio de codigo"
#respuesta="Una camiseta es una prenda de vestir que se utiliza por los humanos que les gustan los perros"
respuesta="Los lobos poseen las siguientes características generales: Son animales cuadrúpedos, mamíferos, con cuerpos de entre 60 y 90 cm de alto y un peso de entre 32 y 70 kg. Suelen medir entre 1,30 y 2 metros de largo. Poseen una cola larga, y no son, en principio, demasiado diferentes anatómicamente de un perro."

def tokenizacion(textos):
    vector = []
    for s in range(3):
        eliminarpunt = re.sub(r'[^\w\s]','',textos[s])
        minusculas=eliminarpunt.lower()
        docnlp=nlp(minusculas)
        for token in docnlp:
            vector.append(token.lemma_)
            #lemmatized_sentence = " ".join([token.lemma_ for token in vector]) 
        #print(lemmatized_sentence)
    print(vector)
    return vector
    
def tokenizacion_resp(textos):
    vector1= []
    eliminarpunt = re.sub(r'[^\w\s]','',str(textos))
    minusculas=eliminarpunt.lower()
    docnlp=nlp(minusculas)
    for token in docnlp:
        vector1.append(token.lemma_)
    print(vector1)

    return vector1 

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

def libreria_spacy(contexto1,texto):
    
    notas_spacy=[]
    for definicion in contexto1: 
        doc2 = (str(definicion))
        doc3=nlp(doc2)
        doc = nlp(str(texto))
        var= doc.similarity(doc3)
        notas_spacy.append(var)
    print(notas_spacy) 
    return notas_spacy

def libreria_sklearn(contexto1, texto):
    notas_sklearn=[]
    contexto1.append(texto)
    vectorizer = CountVectorizer()
    x=vectorizer.fit_transform(contexto1)
    tfidf = TfidfVectorizer().fit_transform(contexto1)
    notas=[cosine_similarity(tfidf[0:1],tfidf[3:4]),cosine_similarity(tfidf[1:2],tfidf[3:4]),cosine_similarity(tfidf[2:3],tfidf[3:4])]
    #notas=[cosine_similarity(tfidf[0:1],tfidf[1:])]
    
    for s in range(len(notas)):
        notas_sklearn.append(notas[s][0][0])
    print(notas_sklearn)

    return notas_sklearn

def evalua(valor1,valor2):
    totalnotas=[]
    for s in range(len(valor1)):
        total=valor1[s]+valor2[s]
        totalnotas.append(total)
        print(total)

    buenas_notas=(totalnotas[0]+totalnotas[1]+totalnotas[2])/3
    #malas_notas=(totalnotas[3]+totalnotas[4])/2

    print(buenas_notas)

def palabras_sinnumero(palabras):
    totalpalabras=[]
    numero=len(palabras)
    for s in range(numero):
        totalpalabras.append(palabras[s][0])
    print(totalpalabras)
    return totalpalabras

def comparacion_palabras(palabras_t,palabras_r):
    palabras_repetidas=[]
    numero=len(palabras_r)
    for s in range(numero):
        if palabras_r[s] in palabras_t:
            palabras_repetidas.append(palabras_r[s])
    print(palabras_repetidas)

def analisistexto(texto):
    doc = nlp(texto)
    analisis=[]
    for token in doc:
        analisis.append(token.pos_)
    longitud=len(analisis)
    for pos in range(longitud):
        if longitud-2>pos:#Determina al menos tres espacios para que pueda ser leido y determinar si es un verbo repetido
            if analisis[pos]=='VERB':
                if analisis[pos]==analisis[pos+1]==analisis[pos+2]:
                    print("Verbos sin sentido")
        if longitud-1>pos:#Determina al menos dos espacios para que pueda ser leido y determinar si es un determinante repetido
            if analisis[pos]=='DET':
                if analisis[pos]==analisis[pos+1]:
                    print("Determinante sin sentido")
    for token1 in doc:
        pass
        #print(token1.text,token1.dep_,token1.ent_id_,token1.ent_type_,token1.norm_)
        #print(token.lemma_)
    

nota1=libreria_spacy(definiciones,respuesta)
nota2=libreria_sklearn(definiciones,respuesta)
evalua(nota1,nota2)
red_palabras=tokenizacion(definiciones)
words_clave=palabras_clave(red_palabras)
palabras_respuesta=tokenizacion_resp(respuesta)
words_resp=palabras_clave(palabras_respuesta)
palabrasok=palabras_sinnumero(words_clave)
palabrasok1=palabras_sinnumero(words_resp)
analisistexto(respuesta)
comparacion_palabras(palabrasok,palabrasok1)


