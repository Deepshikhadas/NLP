import nltk
from nltk.book import *
from nltk.corpus import brown
print(brown.categories())
cfd = nltk.ConditionalFreqDist((genre,word)
    for genre in brown.categories()
    for word in brown.words(categories=genre))
genres =['news','religion','hobbies','science_fiction','romance','humor']
modals = ['can','could','may','might','must','will']
cfd.tabulate(conditions= genres,samples = modals)
