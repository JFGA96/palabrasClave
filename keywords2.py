from newspaper import Article
import jieba
 
#A new article from TOI
url = "https://elpais.com/cultura/2021-10-25/la-pirateria-baja-un-7-en-espana-pero-sigue-provocando-perdidas-millonarias.html"
 
#For different language newspaper refer above table
toi_article = Article(url, language="es") # en for English
 
#To download the article
toi_article.download()
 
#To parse the article
toi_article.parse()
 
#To perform natural language processing ie..nlp
toi_article.nlp()
 
#To extract title
print("Article's Title:")
#print(toi_article.title)
print("n")

#To extract text
print("Article's Text:")
#print(toi_article.text)
print("n")
 
#To extract summary
print("Article's Summary:")
#print(toi_article.summary)
print("n")
 
#To extract keywords
print("Article's Keywords:")
print(toi_article.keywords)
processed_text=toi_article.keywords

vocabulary = list(set(processed_text))
print(vocabulary)

import numpy as np
import math
vocab_len = len(vocabulary)

weighted_edge = np.zeros((vocab_len,vocab_len),dtype=np.float32)

score = np.zeros((vocab_len),dtype=np.float32)
window_size = 3
covered_coocurrences = []

for i in range(0,vocab_len):
    score[i]=1
    for j in range(0,vocab_len):
        if j==i:
            weighted_edge[i][j]=0
        else:
            for window_start in range(0,(len(processed_text)-window_size+1)):
                
                window_end = window_start+window_size
                
                window = processed_text[window_start:window_end]
                
                if (vocabulary[i] in window) and (vocabulary[j] in window):
                    
                    index_of_i = window_start + window.index(vocabulary[i])
                    index_of_j = window_start + window.index(vocabulary[j])
                    
                    # index_of_x is the absolute position of the xth term in the window 
                    # (counting from 0) 
                    # in the processed_text
                      
                    if [index_of_i,index_of_j] not in covered_coocurrences:
                        weighted_edge[i][j]+=1/math.fabs(index_of_i-index_of_j)
                        covered_coocurrences.append([index_of_i,index_of_j])

inout = np.zeros((vocab_len),dtype=np.float32)

for i in range(0,vocab_len):
    for j in range(0,vocab_len):
        inout[i]+=weighted_edge[i][j]

MAX_ITERATIONS = 50
d=0.85
threshold = 0.0001 #convergence threshold

for iter in range(0,MAX_ITERATIONS):
    prev_score = np.copy(score)
    
    for i in range(0,vocab_len):
        
        summation = 0
        for j in range(0,vocab_len):
            if weighted_edge[i][j] != 0:
                summation += (weighted_edge[i][j]/inout[j])*score[j]
                
        score[i] = (1-d) + d*(summation)
    
    if np.sum(np.fabs(prev_score-score)) <= threshold: #convergence condition
        print ("Converging at iteration "+str(iter)+"....")
        break

    for i in range(0,vocab_len):
        print ("Score of "+vocabulary[i]+": "+str(score[i]))
        
    