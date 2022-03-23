def data(lista):
   datos=[
      (lista[0],'5'),
      (lista[1],'5'),
      (lista[2],'3'),
      (lista[3],'3'),
      (lista[4],'1'),
      (lista[5],'1'),
   ]
   #print(datos)
   return datos

lista=["hola","buena","es","nuevo","hello","deber"]

tupla1=data(lista)
tupla1.append(("hola","2"))

print(tupla1)