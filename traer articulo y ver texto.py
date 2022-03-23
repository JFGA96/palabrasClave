from newspaper import Article
import jieba
 
#A new article from TOI
url = "https://es.wikipedia.org/wiki/Radamel_Falcao"
#For different language newspaper refer above table
articulo1 = Article(url, language="es") # en for English
 
#To download the article
articulo1.download()
#To parse the article
articulo1.parse()
#To perform natural language processing ie..nlp
articulo1.nlp()
#To extract title

print("Article's Title:")
#print(toi_article.title)


#To extract text
print("Article's Text:")
texto=articulo1.text
print(articulo1.text)
print(type(texto))

 
#To extract summary
print("Article's Summary:")
#print(toi_article.summary)

 
#To extract keywords
print("Article's Keywords1:")
#print(articulo1.keywords)
#processed_text=articulo1.keywords

print("Article's Keywords2:")
#print(articulo2.keywords)
#processed_text=articulo2.keywords

#vocabulary = list(set(processed_text))
#print(vocabulary)

