import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt
import nltk
from sklearn.feature_extraction.text import CountVectorizer,TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB,MultinomialNB,BernoulliNB
from sklearn.metrics import accuracy_score,confusion_matrix,precision_score


nltk.download('punkt')
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords

from .helper import transform_text
from .Firebase import person
from .Firebase import db




df= pd.read_csv('/root/PycharmProjects/professional/API/web/spam.csv')
df.drop(columns=['Unnamed: 2','Unnamed: 3','Unnamed: 4'],inplace=True)
df.rename(columns={'v1':'target','v2':'text'},inplace=True)

encoder = LabelEncoder()
df = df.drop_duplicates(keep='first')
df['transformed_text'] = df['text'].apply(transform_text)
print(df.head)

cv = CountVectorizer()
x = cv.fit_transform(df['transformed_text'].values)
print(x.shape)
y = df['target'].values

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=2)
classifier= MultinomialNB()
classifier.fit(x_train,y_train)

predicting= classifier.predict(x_test)
print(accuracy_score(y_test,predicting))
print(confusion_matrix(y_test,predicting))

Example= [' help']
print(Example)
exam= cv.transform(Example)
print(classifier.predict(exam))

for i in person.each():
    values = i.val()
    st = (values['reply'])
    incoming = [str(st)]
    print(incoming)
    modify = cv.transform(incoming)
    classified = classifier.predict(modify)
    print(classified)
    if classified == 'spam':
        print("it has to be deleted")
        data = {"Reply": st}
        db.child("Spammed").push(data)
