import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia

#escuchar nuestro microfono y devolver el audio como texto


def transformar_audio_text():
    
    # almacenar recognizer en variable
    r= sr.Regonizer()
    #configurar el micforno 
    with sr.Microfone() as origin:
        #tiempo de espera 
        r.pause_threshold= 0.8
        #informar que comenzo la grabacion
        print('ya puedes hablar')