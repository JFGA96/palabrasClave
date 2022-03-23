import jieba.analyse  # Importar biblioteca de extracción de palabras clave
import pandas as pd  # Importar pandas
import newspaper
import nltk

nltk.download('punkt')
# Leer datos de texto
# Obtenga el artículo La Comisión Reguladora Bancaria de China presentó una nueva política como ejemplo
article = newspaper.Article('https://elpais.com/cultura/2021-10-25/la-pirateria-baja-un-7-en-espana-pero-sigue-provocando-perdidas-millonarias.html', language='es')

# Descargar artículo
article.download()
# Analizar artículo
article.parse()
# NLP procesando el artículo
article.nlp()
# cosido de artículos procesados ​​nlp
string_data = "".join(article.keywords)
# Extracción de palabras clave
def get_key_words(string_data, how=''):
    # topK: El número de palabras clave extraídas, si no se especifica, se extraerán todas;
    # withWeight: establezca True para especificar el peso IF-IDF correspondiente a la palabra de salida
    if how == 'textrank':
        # Use el algoritmo TextRank
        tags_pairs = jieba.analyse.textrank(string_data,  topK=5,  withWeight=True)  # Extraer etiquetas de palabras clave
    else:
        # Utilice el algoritmo TF-IDF
        tags_pairs = jieba.analyse.extract_tags(string_data,  topK=5,  withWeight=True)  # Extraer etiquetas de palabras clave
    tags_list = []  # La lista vacía se usa para almacenar los tres valores después de dividir
    for i in tags_pairs:  # Imprimir etiqueta, grupo y peso TF-IDF
        tags_list.append((i[0], i[1]))  # Divide los tres valores de campo
    tags_pd = pd.DataFrame(tags_list, columns=['word', 'weight'])  # Crear marco de datos
    return tags_pd

keywords = get_key_words(string_data)
print("#####################TF-IDF####################")
print(keywords)

keywords_tr = get_key_words(string_data, how='textrank')
print("#####################textrank####################")
print(keywords_tr)



