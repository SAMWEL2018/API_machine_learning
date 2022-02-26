import pyrebase
import pandas as pd
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt
import nltk
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from main import classifier
from Firebase import person

nltk.download('punkt')
from helper import transform_text
from Firebase import db

df = pd.read_csv('spam.csv')
df.drop(columns=['Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4'], inplace=True)
df.rename(columns={'v1': 'target', 'v2': 'text'}, inplace=True)

encoder = LabelEncoder()
df = df.drop_duplicates(keep='first')
df['transformed_text'] = df['text'].apply(transform_text)
print(df.head)

# not to deleted
cv = CountVectorizer()
x = cv.fit_transform(df['transformed_text'].values)
y = df['target'].values

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

