import requests
from bs4 import BeautifulSoup
import requests
from re import I
from googlesearch import search
from nltk import text
import urllib3
from bs4 import BeautifulSoup
from newspaper import Article
import jieba
import nltk
from nltk.tokenize import RegexpTokenizer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.probability import FreqDist
from nltk.stem.wordnet import WordNetLemmatizer
import jieba.analyse  # Importar biblioteca de extracción de palabras clave
import pandas as pd  # Importar pandas
import newspaper
import numpy as np

lista_sinonimos=[]

url="https://www.wordreference.com/sinonimos/"
buscar= url+'actividad'
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

print(str(filtered_word[1])) 

