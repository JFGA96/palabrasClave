#text='toda actividad humana libre material  intelectual permanente  transitoria persona natural ejecuta conscientemente servicio otra cualquiera finalidad siempre efectúe ejecución contrato trabajo.trabajo economía horas dedican personas producción bienes servicios. trabajo factores producción capital, tierra tecnología. esfuerzo humano producción  venta  bienes  servicios.trabajo actividades realizadas objetivo alcanzar meta, solucionar problema producir bienes servicios  necesidades humanas.denomina trabajo actividad manual  intelectual cambio compensación económica labores concretadas.'

import nltk
from nltk.tokenize import RegexpTokenizer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.probability import FreqDist
from nltk.stem.wordnet import WordNetLemmatizer

from newspaper import Article
import jieba
import nltk



url="https://elpais.com/cultura/2021-10-25/la-pirateria-baja-un-7-en-espana-pero-sigue-provocando-perdidas-millonarias.html"
toi_article = Article(url, language="es") 
toi_article.download()
toi_article.parse()
toi_article.nlp()
# cosido de artículos procesados ​​nlp
texto=toi_article.text

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
most_common = fdist.most_common(15)
data=(fdist.most_common(15))
print(data)


