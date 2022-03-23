from tkinter.constants import Y
from sklearn.feature_extraction.text import CountVectorizer
import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = CountVectorizer()

data=['Como trabajo denominamos al conjunto de actividades que son realizadas con el objetivo de alcanzar una meta, solucionar un problema o producir bienes y servicios para atender las necesidades humanas.','El trabajo en economía se refiere a las horas que dedican las personas a la producción de bienes o servicios. El trabajo uno de los factores de producción junto con el capital, la tierra y la tecnología. Así, consiste en el esfuerzo humano puesto en la producción y venta de bienes y servicios.']
data1=['El trabajo es producir un bien o servicio por un valor']
#x=vectorizer.fit_transform(data)
#y=vectorizer.fit_transform(data1)

def alistamiento():
  x=vectorizer.fit_transform(data)
  print("get")
  #print (vectorizer.get_feature_names())
  vocabulario=(vectorizer.get_feature_names())

  
  stop_words = set(stopwords.words('Spanish'))
  all_stopwords = stopwords.words('Spanish')
  all_stopwords.append('si')
  all_stopwords.append('min')
  all_stopwords.append('tan')
  all_stopwords.append('uno')
  all_stopwords.append('así')

  filtered_word = []
  for vocabulario in vocabulario:
    if vocabulario not in all_stopwords:
      filtered_word.append(vocabulario)
      
  vocabulario=(filtered_word)
  print(vocabulario)
  return(vocabulario)

  #x=vectorizer.fit_transform(vocabulario)

  #print("vocabulary")
  #print (vectorizer.vocabulary_) 
  
  #tfidf = TfidfVectorizer().fit_transform(vocabulario)

def nuevaspalabras():
  x=vectorizer.fit_transform(data1)
  vocabularionuevo=(vectorizer.get_feature_names())

  
  stop_words = set(stopwords.words('Spanish'))
  all_stopwords = stopwords.words('Spanish')
  all_stopwords.append('si')
  all_stopwords.append('min')
  all_stopwords.append('tan')
  all_stopwords.append('uno')
  all_stopwords.append('así')

  filtered_word = []
  for vocabularionuevo in vocabularionuevo:
    if vocabularionuevo not in all_stopwords:
      filtered_word.append(vocabularionuevo)
      
  vocabularionuevo=(filtered_word)
  #print(vocabularionuevo)
  return vocabularionuevo

bancodepalabras=alistamiento()
nuevas=nuevaspalabras()
print(nuevas)
filtered_word = []
for nuevas in nuevas:
  if  nuevas in bancodepalabras:
    filtered_word.append(nuevas)
      
totales=(filtered_word)
print (len(totales))
print(totales)

from nltk.stem.wordnet import WordNetLemmatizer
lem = WordNetLemmatizer()

lem_words = []
for w in filtered_word:
  lem_words.append(lem.lemmatize(w,'v'))

from nltk.probability import FreqDist
fdist = FreqDist(data)
#palabras=fdist.get(2)
most_common = fdist.most_common(10)
data=(fdist.most_common(10))
print(data)

"""filtrado = []
for vocabulario in vocabulario:
  if vocabulario not in palabrasclave:
    filtrado.append(palabrasclave)"""


