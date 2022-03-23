
import io
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
 
# word_tokenize accepts
# a string as an input, not a file.
stop_words = str(stopwords.words('spanish'))
file1 = open("C:/Users/Felipe/OneDrive/Escritorio/Doc la gran colombia/Programas python/Palabras clave/lista2.txt")

all_stopwords = stopwords.words('Spanish')
# Use this to read file content as a stream:

appendFile = open("C:/Users/Felipe/OneDrive/Escritorio/Doc la gran colombia/Programas python/Palabras clave/lista1.txt",'a')
appendFile.write(stop_words)
appendFile.close()