from newspaper import Article
import jieba
from numpy.core.arrayprint import str_format
from scipy.sparse import data
from scipy.sparse.sputils import getdtype
 
#A new article from TOI
url = "https://elpais.com/cultura/2021-10-25/la-pirateria-baja-un-7-en-espana-pero-sigue-provocando-perdidas-millonarias.html"
 
#For different language newspaper refer above table
toi_article = Article(url, language="es") # en for English
 
#To download the article
toi_article.download()
 
#To parse the article
toi_article.parse()
 
#To perform natural language processing ie..nlp
toi_article.nlp()
 
#To extract title
print("Article's Title:")
#print(toi_article.title)
print("n")

#To extract text
print("Article's Text:")
#text=toi_article.text
text='toda actividad humana libre material  intelectual permanente  transitoria persona natural ejecuta conscientemente servicio otra cualquiera finalidad siempre efectúe ejecución contrato trabajo.trabajo economía horas dedican personas producción bienes servicios. trabajo factores producción capital, tierra tecnología. esfuerzo humano producción  venta  bienes  servicios.trabajo actividades realizadas objetivo alcanzar meta, solucionar problema producir bienes servicios  necesidades humanas.denomina trabajo actividad manual  intelectual cambio compensación económica labores concretadas.'
#print(toi_article.text)
print("n")
 
#To extract summary
print("Article's Summary:")
#print(toi_article.summary)
print("n")
 
#To extract keywords
print("Article's Keywords:")
keywords=toi_article.keywords
#print(toi_article.keywords)



import nltk
#nltk.download()

from nltk.tokenize import RegexpTokenizer

tokenizer = RegexpTokenizer(r'\w+')
text = tokenizer.tokenize(text)

text = ' '.join(word for word in text)

from nltk.tokenize import word_tokenize
tokenized_word=word_tokenize(text)


tokenized_word = [word.lower() for word in tokenized_word]


from nltk.corpus import stopwords
stop_words = set(stopwords.words('Spanish'))
all_stopwords = stopwords.words('Spanish')
all_stopwords.append('si')
all_stopwords.append('min')
all_stopwords.append('tan')
print(stop_words)

#filtrado de palabras que estan en stopword


filtered_word = []
for word in tokenized_word:
  if word not in all_stopwords:
    filtered_word.append(word)



from nltk.stem import PorterStemmer

ps = PorterStemmer()

stemmed_words = []
for w in filtered_word:
  stemmed_words.append(ps.stem(w))

#See how stemming works
for word in ['5', 'sintiendo', 'preguntar','retar','devoto']:
    print(ps.stem(word))

from nltk.stem.wordnet import WordNetLemmatizer
lem = WordNetLemmatizer()

lem_words = []
for w in filtered_word:
  lem_words.append(lem.lemmatize(w,'v'))


for word in ['5', 'sentir', 'preguntar','retar','devoto']:
    print(lem.lemmatize(word,'v'))

from nltk.probability import FreqDist
fdist = FreqDist(lem_words)
#palabras=fdist.get(2)
most_common = fdist.most_common(10)
data=(fdist.most_common(10))
print(data)
nuevos=[data[1][1],data[2][1],data[3][1],data[4][1]]
#list(nuevos)
print(nuevos)


