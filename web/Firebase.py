import pyrebase
import json
import requests
import nltk
from nltk .stem import SnowballStemmer

firebaseconfig= {
    'apiKey': "AIzaSyCs8lE-FeHDDi4hMQ5Cyl4L35oY9HjkXkE",
    'authDomain': "farmers-cb48f.firebaseapp.com",
    'databaseURL': "https://farmers-cb48f.firebaseio.com",
    'projectId': "farmers-cb48f",
    'storageBucket': "farmers-cb48f.appspot.com",
    'messagingSenderId': "714091151538",
    'appId': "1:714091151538:web:d9f6dbbf5675e272d849ab"

}

firebase= pyrebase.initialize_app(firebaseconfig)
db= firebase.database()

person= db.child("Replies").get()
print(person)

for i in person.each():
    values= i.val()
    st=(values['reply'])
    #print(st)
    stemming = SnowballStemmer('english')
    #print(stemming.stem(st))





