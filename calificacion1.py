
####Comparacion, PalabrasClave, Estructuracion
#### Se quiere tambien mas adelante obtener ortografia

#from textblob import TextBlob
from textblob.classifiers import NaiveBayesClassifier


def data(text1,text2,text3,text4):
   datos=[
      (text1,'Exelente'),
      (text2,'Muy bueno'),
      (text3,'Bueno'),
      (text4,'Regular'),
      #(text5,'Mucho por mejorar'),
   ]
   return datos
complete=data("la inteligencia artificial es un compuesto de software y procesamiento para lograr una similitud al pensamiento humano y de esta forma realizar procesos mas rapidos y eficaces ","La inteligencia artificial (IA) es la base a partir de la cual se imitan los procesos de inteligencia humana mediante la creación y la aplicación de algoritmos creados en un entorno dinámico de computación. O bien, dicho de forma sencilla, la IA consiste en intentar que los ordenadores piensen y actúen como los humanos."
,"La inteligencia artificial (IA) es, en informática, la inteligencia expresada por máquinas, sus procesadores y sus softwares, que serían los análogos al cuerpo, el cerebro y la mente, respectivamente, a diferencia de la inteligencia natural demostrada por humanos y ciertos animales con cerebros complejos. 1​ Se considera que el origen de la IA se remonta a los intentos del hombre desde la antigüedad por incrementar sus potencialidades físicas e intelectuales, creando artefactos con automatismos y simulando la forma y las habilidades de los seres humanos","La computacion nace desde hace muchos años y ahora se quiere dar una revolucion para asi alcanzar desarrollos nunca antes visto")

def califi(datos,respuesta):
   cl=NaiveBayesClassifier(datos)
   print(cl.classify(respuesta))
   return cl.classify(respuesta)

califi(complete,"Son robots que buscan acabar con el mundo a traves de su pensamiento critico y analitico para matar")