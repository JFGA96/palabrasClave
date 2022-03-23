from newspaper import Article
import jieba
 
#A new article from TOI
url = "https://elpais.com/deportes/2021-10-24/el-barca-muere-de-realidad.html"
url1 = "https://elpais.com/deportes/2021-10-27/el-barca-toca-fondo.html"
#For different language newspaper refer above table
articulo1 = Article(url, language="es") # en for English
articulo2 = Article(url1, language="es") # en for English
 
#To download the article
articulo1.download()
articulo2.download()
#To parse the article
articulo1.parse()
articulo2.parse()
#To perform natural language processing ie..nlp
articulo1.nlp()
articulo2.nlp()
#To extract title

print("Article's Title:")
#print(toi_article.title)


#To extract text
print("Article's Text:")
#print(toi_article.text)

 
#To extract summary
print("Article's Summary:")
#print(toi_article.summary)

 
#To extract keywords
print("Article's Keywords1:")
print(articulo1.keywords)
#processed_text=articulo1.keywords

print("Article's Keywords2:")
print(articulo2.keywords)
#processed_text=articulo2.keywords

#vocabulary = list(set(processed_text))
#print(vocabulary)

data=articulo1.keywords
data2=articulo2.keywords


from sklearn.feature_extraction.text import CountVectorizer
vectorizer = CountVectorizer()

x1=vectorizer.fit_transform(data)
x2=vectorizer.fit_transform(data2)
print("get")
print(x1,x2)
numeraciondata=vectorizer.vocabulary_
numeraciondata2=vectorizer.vocabulary_


#print("vocabulary")
print (numeraciondata,numeraciondata2) 

from sklearn.feature_extraction.text import TfidfVectorizer
vectordata = TfidfVectorizer().fit_transform(data)
vectordata2 = TfidfVectorizer().fit_transform(data2)
#print(vectordata)

from sklearn.metrics.pairwise import cosine_similarity
print(cosine_similarity(vectordata[0:1],vectordata2).flatten())