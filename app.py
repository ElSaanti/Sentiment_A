from textblob import TextBlob
import streamlit as st
from googletrans import Translator
from streamlit_lottie import st_lottie
import json


st.title('Análisis de Sentimiento')
st.subheader("Por favor escribe en el campo de texto la frase que deseas analizar")

with open('graficos.json') as source:
    animation=json.load(source)
    st.lottie(animation,width = 350)

translator = Translator()

with st.sidebar:
    st.subheader("Polaridad y Subjetividad")
    st.write("""
    Polaridad: Indica si el sentimiento expresado en el texto es positivo, negativo o neutral. 
    Su valor oscila entre -1 (muy negativo) y 1 (muy positivo), con 0 representando un sentimiento neutral.

    Subjetividad: Mide cuánto del contenido es subjetivo frente a objetivo.
    Va de 0 a 1, donde 0 es objetivo y 1 es subjetivo.
    """)


def cargar_lottie(ruta_json):
    with open(ruta_json, "r", encoding="utf-8") as source:
        return json.load(source)


with st.expander('Analizar texto'):
    text = st.text_input('Escribe por favor: ')

    if text:
        translation = translator.translate(text, src="es", dest="en")
        trans_text = translation.text

        blob = TextBlob(trans_text)

        polarity = round(blob.sentiment.polarity, 2)
        subjectivity = round(blob.sentiment.subjectivity, 2)

        st.write('Polarity: ', polarity)
        st.write('Subjectivity: ', subjectivity)

        # Selección del archivo JSON según el sentimiento
        if polarity > 0:
            st.write('Es un sentimiento Positivo')
            archivo_json = 'Emoji - Happy.json'
        elif polarity < 0:
            st.write('Es un sentimiento Negativo')
            archivo_json = 'sad.json'
        else:
            st.write('Es un sentimiento Neutral')
            archivo_json = 'Error 404 - Facebook Style.json'

        animation = cargar_lottie(archivo_json)
        st_lottie(animation, width=350)
