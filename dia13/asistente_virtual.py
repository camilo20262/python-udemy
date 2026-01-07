import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia

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
transformar_audio_text()
