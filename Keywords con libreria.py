texto='toda actividad humana libre material  intelectual permanente  transitoria persona natural ejecuta conscientemente servicio otra cualquiera finalidad siempre efectúe ejecución contrato trabajo.trabajo economía horas dedican personas producción bienes servicios. trabajo factores producción capital, tierra tecnología. esfuerzo humano producción  venta  bienes  servicios.trabajo actividades realizadas objetivo alcanzar meta, solucionar problema producir bienes servicios  necesidades humanas.denomina trabajo actividad manual  intelectual cambio compensación económica labores concretadas.'

from typing import TextIO
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

"""article = newspaper.Article("https://elpais.com/cultura/2021-10-25/la-pirateria-baja-un-7-en-espana-pero-sigue-provocando-perdidas-millonarias.html", language='es')
# Descargar artículo
article.download()
# Analizar artículo
article.parse()
# NLP procesando el artículo
article.nlp()
# cosido de artículos procesados ​​nlp
data = "".join(article.keywords)
print(type(data))"""


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
print("#####################TF-IDF####################")
print(keywords)

"""
keywords_tr = get_key_words(string_data, how='textrank')
print("#####################textrank####################")
print(keywords_tr)"""