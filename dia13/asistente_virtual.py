import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia

#opciones de voz / idioma
id1= 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0'
id2='HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'
id3='HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-MX_SABINA_11.0'

# Escuchar nuestro micrófono y devolver el audio como texto
def transformar_audio_text():

    # almacenar recognizer en variable
    r = sr.Recognizer()

    # configurar el micrófono
    with sr.Microphone() as origen:
        # tiempo de espera
        r.pause_threshold = 0.8

        # informar que comenzó la grabación
        print('Ya puedes hablar...')
        
        # guardar lo que escuche
        audio = r.listen(origen)

        try:
            # reconocer audio con Google
            pedido = r.recognize_google(audio, language='es-CO')

            # prueba de que pudo ingresar
            print('Dijiste:', pedido)

            # devolver pedido
            return pedido

        # en caso de que no comprenda el audio
        except sr.UnknownValueError:
            print('Ups, no entendí')
            return 'sigo esperando'

        except sr.RequestError:
            print('Ups, error con el servicio')
            return 'sigo esperando'

        # error inesperado
        except Exception as e:
            print('Ups, algo ha salido mal:', e)
            return 'sigo esperando'


# Ejecutar función
#transformar_audio_text()


#funcion para que el asistente pueda ser escuchado


def hablar(mensaje):
    #encender el motor de pyttsx3
    engine= pyttsx3.init()
    engine.setProperty('voice',id3)
    #pronunciar mensaje 
    engine.say(mensaje)
    engine.runAndWait()


#informar el dia de la semana
def pedir_dia():
    #crear variable con datos de hoy
    dia= datetime.date.today()
    print(dia)
    #crear variable para dia de la semana
    dia_semana= dia.weekday()
    print(dia_semana)

    #diccionario con nombres de dias
    calendario= {0:'lunes',
                 1:'Martes',
                 2:'Miércoles',
                 3:'Jueves',
                 4:'Viernes',
                 5:'Sábado',
                 6:'Domingo'}
    #decir el dia de la semana
    hablar(f'hoy es {calendario[dia_semana]}')


def pedir_hora():
    #crear una variable con los datos de la hora 
    hora = datetime.datetime.now()
    hora = f'En este momento son las {hora.hour} horas con {hora.minute} minutos'
    print(hora)
    # decir la hora 
    hablar(hora)


def saludo_inicial():
    #decir el saludo 
    hablar('Hola, soy elena tu asistente personal, como te puedo ayudar el día de hoy?')

def pedir_cosas():
    #activar saludo 
    saludo_inicial()
    # variable de corte 
    comenzar = True 


    #loop central 
    while comenzar:
        #activar el micro y guardar el pedido en un string
        pedido = transformar_audio_text().lower()
        if 'abrir youtube' in pedido:
            hablar('Con gusto, estoy abriendo youTube')
            webbrowser.open('https://www.youtube.com')
            continue
        elif 'abrir navegador' in pedido:
            hablar ('Claro, estoy en eso')
            webbrowser.open('https://www.google.com')
            continue
        elif 'qué dia es hoy' in pedido:
            pedir_dia()
            continue
        elif 'qué hora es' in pedido:
            pedir_hora()
        continue
pedir_cosas()