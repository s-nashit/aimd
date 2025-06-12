import streamlit as st
import pickle
import spacy

with open('data.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

nlp = spacy.load('en_core_web_lg')
st.title("News Detection App")

a = st.text_input('Enter news')
doc = nlp(a)
vector = doc.vector
prediction = model.predict([vector])
if prediction[0] == 1:
    st.write("This news is **real**.")
else:
    st.write("This news is **fake**.")