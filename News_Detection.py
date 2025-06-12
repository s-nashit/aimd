import streamlit as st
import pandas as pd
import spacy

df = pd.read_csv('Fake_Real_Data.csv')

st.title("News Detection")
st.write("This is a simple news detection app.")

user = st.text_input('Enter news')

nlp = spacy.load('en_core_web_lg')
df['vector'] = df['Text'].apply(lambda text: nlp(text).vector)
df['Label'] = df['label'].map({'Fake':0, 'Real':1})
import numpy as np
x_train_2d = np.stack(x_train)
x_test_2d = np.stack(x_test)
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(df.vector.values, df.Label)

from sklearn.naive_bayes import MultinomialNB
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
x_train_s = scaler.fit_transform(x_train_2d)
x_test_s = scaler.fit_transform(x_test_2d)
model = MultinomialNB()
model.fit(x_train_s, y_train)

vec = nlp(user).vector
v = vec.reshape(1, -1)
x = model.predict(v)
if x == 1:
    st.write('Real News')
else:
    st.write('Fake News')