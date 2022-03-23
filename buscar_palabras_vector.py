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

url1="https://definicion.de/motor/"
url2="https://es.wikipedia.org/wiki/Motor"

toi_article = Article(url1, language="es") 
toi_article.download()
toi_article.parse()
toi_article.nlp()
# cosido de artículos procesados ​​nlp
texto1=toi_article.text

tokenizer = RegexpTokenizer(r'\w+')
text = tokenizer.tokenize(texto1)
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
data1=(fdist.most_common(15))
print(data1)

toi_article = Article(url2, language="es") 
toi_article.download()
toi_article.parse()
toi_article.nlp()
# cosido de artículos procesados ​​nlp
texto2=toi_article.text

tokenizer = RegexpTokenizer(r'\w+')
text = tokenizer.tokenize(texto2)
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
data2=(fdist.most_common(15))
print(data2)

def palabras_texto(vector):
    numero=len(vector)
    for i in range(numero):
        vector[i]=str(vector[i][0])
    print(vector) 

palabras1=palabras_texto(data1)
palabras2=palabras_texto(data2)

print(data1,data2)

countdata1=len(data1)
countdata2=len(data2)

#data1='nuevo','caro'
#data2='nuevo','caro','dificil'
nuevo=[]
for s in range(countdata1):
    if data2[s] in data1:
        nuevo.append(data2[s])

print(nuevo)
