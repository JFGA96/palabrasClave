# Extracting results from google

from googlesearch import search
import urllib3
from bs4 import BeautifulSoup

results=[]
def search_in_google(query):
	results = search(busqueda, num_results=2, lang="es")
	return results
busqueda = input("Inserte su busqueda\n")
results = search_in_google(busqueda)
for result in results:
	pass


print(results)

num=len(results)
results.remove(results[num-1])
num=len(results)

valor=[]

print(num)

print(results)
print(valor)



print(results)





