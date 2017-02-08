## Diana Bonilla
## Polaridad de una palabra
## Python 2.7
## 07/02/2017
import nltk
from textblob import TextBlob
frases='''Never give up on your dreams.
        Now or never.
        Be happy and smile.
        People make mistakes,nobody is perfect.
        Life does not have to be perfect to be wonderful.
        Sometimes yo win sometimes you learn.
        Work hard dream big.
        Every day is a second chance.
        Thank you for the gift of another day.
        You just have to try.
        '''
blob=TextBlob(frases)
for p in blob.sentences:
    print(p.sentiment.polarity)
