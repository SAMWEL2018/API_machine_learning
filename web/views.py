from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import status
from .Serial import Serializers
#from .main import classifier
from .models import comments
from rest_framework.response import Response

from sklearn.feature_extraction.text import CountVectorizer
import pickle

@api_view(['GET','POST'])
def classify(request):

    if request.method=='GET':
        data= comments.objects.all()
        ser= Serializers(data,many=True)
        return Response(ser.data)

    elif request.method=='POST':
        dat=Serializers(data=request.data)

        if dat.is_valid():
            msg= request.data['message']
            Ext_msg = f'{msg}'
            ctx = [Ext_msg]


            import pandas as pd
            from sklearn.feature_extraction.text import CountVectorizer
            from .helper import transform_text


            df = pd.read_csv('/root/PycharmProjects/professional/API/web/spam.csv')
            df.rename(columns={'v1': 'target', 'v2': 'text'}, inplace=True)

            df['transformed_text'] = df['text'].apply(transform_text)

            cv = CountVectorizer()
            x = cv.fit_transform(df['transformed_text'].values)

            print(ctx)
            exam = cv.transform(ctx)

            with open('/root/PycharmProjects/professional/API/web/model_pickle', 'rb') as f:
                model = pickle.load(f)

            pred= model.predict(exam)
            print(pred)
            if pred=='ham':
                bool= request.data['is_positive']
                print(bool)
                record=comments()
                record.message= request.data['message']
                record.is_positive= True
                record.email=request.data['email']
                record.save()
                return Response(status=status.HTTP_201_CREATED)

            else:
                dat.save()
                return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)